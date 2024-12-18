import sys
sys.path.append(r"C:\Dev\py2")
import os
import pandas as pd
import numpy as np
import model.database.query.database_query.QueryJTE as qjte
import model.database.query.database_query.QueryJSS as qjss
import model.database.query.database_query.QueryJLC as qjlc
import model.database.query.database_query.QueryJLM as qjlm
import model.database.query.database_query.QueryJLW as qjlw
import model.database.query.database_query.QueryJLCPC as qjlcpc
import model.database.query.database_query.QueryJLMPC as qjlmpc
import model.database.query.database_query.QueryJLWPC as qjlwpc
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tqdm import trange
import torch
import torch.nn as nn
import torch.nn.functional as F
import model.database.query.database_query.QueryJRH as qjrh
import model.database.query.database_query.QueryJRE as qjre
from torch_geometric.data import Data
import inspect
from model.features.onehot_encoding.current.Cat117BDst import Cat117BDst
from model.features.onehot_encoding.current.Cat105CTrk2 import Cat105CTrk2
from torch.nn import Linear
import IPython.display as display

class Net(torch.nn.Module):
    def __init__(self, feature_size):
        super(Net, self).__init__()
        hidden_size = feature_size*4
        hidden_size2 = feature_size*2
        hidden_size3 = int(feature_size/2)
        hidden_size4 =  int(feature_size/4)
        input_size = feature_size
        self.fc1 = Linear(input_size, hidden_size)
        self.fc2 = Linear(hidden_size, hidden_size2)
        self.fc3 = Linear(hidden_size2, hidden_size3)
        self.fc4 = Linear(hidden_size3, hidden_size4)  
        self.fc5 = Linear(hidden_size4, 1)  

        self.bn1 = nn.BatchNorm1d(input_size)
        self.bn2 = nn.BatchNorm1d(hidden_size)
        self.bn3 = nn.BatchNorm1d(hidden_size2)
        self.bn4 = nn.BatchNorm1d(hidden_size3)  
        self.bn5 = nn.BatchNorm1d(hidden_size4) 
        self.dropout = nn.Dropout(0.7)

    def forward(self, data):
        x = data.x
        x = x.view(data.batch_size, -1)
        x = self.bn1(x)
        x = F.leaky_relu(self.fc1(x))
        x = self.dropout(x)
        x = self.bn2(x)
        x = F.leaky_relu(self.fc2(x))
        x = self.dropout(x)
        x = self.bn3(x)
        x = F.leaky_relu(self.fc3(x))
        x = self.dropout(x)
        x = self.bn4(x)
        x = F.leaky_relu(self.fc4(x))
        x = self.fc5(x)
        return torch.sigmoid(x)
    

def train(model, device, loader, optimizer, criterion):
	model.train()
	total_loss = 0
	for batch in loader:
		try:
			batch = batch.to(device)
			optimizer.zero_grad()
			out = model(batch)
			loss = criterion(out.squeeze(), batch.y.float())
			loss.backward()
			optimizer.step()
			total_loss += loss.item()
		except Exception as e:
			print(f'{e}')	
	return total_loss / len(loader)

def validate(model, device,  loader, criterion):
	model.eval()
	total_loss = 0
	all_preds, all_labels = [], []
	with torch.no_grad():
		for batch in loader:
			try:
				batch = batch.to(device)
				out = model(batch)
				loss = criterion(out.squeeze(), batch.y.float())
				total_loss += loss.item()
				preds = (out > 0.5).float()  
				all_preds.extend(preds.cpu().numpy())
				all_labels.extend(batch.y.cpu().numpy())
			except Exception as e:
				print(f'{e}')		
	
	avg_loss = total_loss / len(loader)
	accuracy = accuracy_score(all_labels, all_preds)
	precision = precision_score(all_labels, all_preds, average='binary')
	recall = recall_score(all_labels, all_preds, average='binary')
	f1 = f1_score(all_labels, all_preds, average='binary')
	return avg_loss, accuracy, precision, recall, f1

def create_mlp_train_data(accessor_acc, accessor_scr, df_rh, target_place, data_size=0):
	def get_horses_by_pdt_to_df(accessor_acc, place, dstance, track):
		ret = qjre.get_horse_by_pdt_to_df(accessor_acc, place, dstance, track)
		query = f"rr_r_rank<='08' and rr_r_rank!='00' "
		ret = ret.query(query, engine='python')
		ret = ret.drop_duplicates(subset=['rr_m_blood01', 'rr_m_blood02'])
		return ret

	ret = []
	for i in trange(len(df_rh), desc='data {}'.format(target_place)):
		sr_rh = df_rh.iloc[i]
		place = sr_rh['rh_id'][8:]
		distance = sr_rh['rh_distance']
		track = sr_rh['rh_track']
		condition = create_condition_feature(distance, track)

		df_horses = get_horses_by_pdt_to_df(accessor_acc, place,distance, track)

		gdata = create_mlp_data(
				accessor_acc, accessor_scr, 
    			condition, 
				df_horses,
				is_self_include=False,
				data_size = data_size)
			
		temp_list = [Data(x=gdata['node'][i], 
							y=gdata['rank'][i], 
       						condition = condition.clone()
       						) for i in range(len(gdata['horse_id']))
               ]
		ret.extend(temp_list)   
	return ret

def check_score(model, accessor_acc, accessor_scr,device, place, track, distance):
	def get_horses_pr_to_df(accessor_acc, program_id, race):
		ret = qjre.get_horse_by_ir_to_df(accessor_acc, program_id, race)
		ret = ret[ret['rr_r_rank'] != "00"]
		ret = ret.sort_values(by='rr_r_horse_no')
		return ret
	df_rh = qjrh.get_race_at_by_ptd_to_df(accessor_acc, place, track, distance)
	condition = create_condition_feature(distance, track)
	for _, sr_rh in df_rh.iterrows():

		if(place== sr_rh['rh_id'][8:]  ):
			df_target = get_horses_pr_to_df(accessor_acc, sr_rh['rh_id'], sr_rh['rh_race'])
			if(len(df_target)):
				nodes=  create_mlp_data(accessor_acc, accessor_scr, condition, df_target, is_self_include=False)
				
				prd_list = []
				for i in range(len(nodes)):
					new_data = Data(x=nodes[i])
					predicted_proba = predict(model, device, new_data)
					
					prd_list.append(predicted_proba.item())
				
				df_target['la_prd'] = prd_list
				df_target_sorted = df_target.sort_values(by='la_prd', ascending=False)
				df_target_sorted['マーク'] = df_target_sorted['rr_r_rank'].apply(lambda x: '●' if x in ['01', '02', '03'] else '')      
				df_target_sorted = df_target_sorted[[ 'rr_r_horse_no','rr_r_rank', 'rr_r_vote', 'la_prd', 'マーク']]
				df_target_sorted.columns = ['馬番','順位','人気','予測','３着内']
				display.display(df_target_sorted)
    
def get_parent_smooth_rank( df_horses):
	df_horses['rr_r_rank2'] = df_horses['rr_r_rank'].astype(float)
	ret = df_horses.groupby(['rr_m_blood01', 'rr_m_blood02'])['rr_r_rank2'].agg(['mean', 'count']).reset_index()

	mean_master = df_horses['rr_r_rank2'].astype(float).mean()
	threshold =3 
	ret['smooth_mean'] = ret.apply(lambda row: row['mean'] if row['count'] > threshold else (row['count'] * row['mean'] + ((threshold+1) - row['count']) * mean_master) / (threshold+1), axis=1)
	return ret	

def create_mlp_data(accessor_acc, accessor_scr, condition, df_horses, is_self_include=True, data_size =0):

	cols_with_te=qjte.get_te_col()
	cols = [col.replace('te_', '') for col in cols_with_te]
	df_horses_ex=df_horses[
		['ph_place',
		'rh_distance',
		'rh_track',
		'rr_r_id',
		'rr_r_horse_id',
		'rr_r_rank',
		'rr_m_blood01',
		'rr_m_blood02',
		'rr_m_blood03',
		'rr_m_blood04',
		'rr_m_blood05',
		'rr_m_blood06',
		'rr_m_blood07',
		'rr_m_blood08',
		'rr_m_blood09',
		'rr_m_blood10',
		'rr_m_blood11',
		'rr_m_blood12',
		'rr_m_blood13',
		'rr_m_blood14',]
	]
	ret = {
		'horse_id':[],
		'node':[],
		'rank':[],
	}
	condition_t = torch.Tensor(condition) 
	df_rank_means = get_parent_smooth_rank(df_horses)
	for i in trange(len(df_horses_ex), desc="create data"):
		sr_horse = df_horses_ex.iloc[i]
		horse_id = sr_horse['rr_r_horse_id']
		node = create_features_element(accessor_acc, accessor_scr, sr_horse, cols_with_te, cols, is_self_include)
		if len(node):
			node_t = torch.Tensor(node)
			ret['horse_id'].append(horse_id)
			ret['node'].append(torch.cat([node_t, condition_t], dim=-1) ) 
			ret['rank'].append(create_target(create_mean_rank(sr_horse, df_rank_means)))

		if((data_size != 0) and (i==data_size)): #TODO
			print(f"TODO {data_size}")
			break
	#ret['node'] = create_features_list(list(ret['node']))
	return ret

def append_race_header(sr_horse, features):
	rh_distance = float(sr_horse['rh_distance'])
	rh_track = float(sr_horse['rh_track'])
	
	# featuresの各子リストに値を追加
	for feature in features:
		feature.extend([rh_distance, rh_track])
	return  features


	
def predict(model, device, condition, data):
	""" Performs prediction on a single data instance.
	Args:
		model: The trained PyTorch model.
		data: A single Data instance from torch_geometric.data.Data.
	Returns:
		A tensor of predicted values.
	"""
	model.eval()
	with torch.no_grad():
		data = data.to(device)
		ret = model(data, condition)
	return ret

def draw_score(train_losses, val_losses, accuracies, precisions, recalls):
	
	# 学習結果のプロット（変更なし）
	plt.figure(figsize=(12, 8))

	plt.subplot(2, 2, 1)
	plt.plot(train_losses, label='Train Loss')
	plt.plot(val_losses, label='Validation Loss')
	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.title('Loss')
	plt.legend()

	plt.subplot(2, 2, 2)
	plt.plot(accuracies, label='Accuracy')
	plt.xlabel('Epoch')
	plt.ylabel('Accuracy')
	plt.title('Accuracy')
	plt.legend()

	plt.subplot(2, 2, 3)
	plt.plot(precisions, label='Precision')
	plt.xlabel('Epoch')
	plt.ylabel('Precision')
	plt.title('Precision')
	plt.legend()

	plt.subplot(2, 2, 4)
	plt.plot(recalls, label='Recall')
	plt.xlabel('Epoch')
	plt.ylabel('Recall')
	plt.title('Recall')
	plt.legend()

	plt.tight_layout()
	plt.show()

def get_horse_te_to_sr(accessor_acc, program_id, horse_id, cols_with_te, cols):
	ret = pd.Series
	sr_temp = qjte.get_record_to_sr2(accessor_acc,program_id, horse_id)
	if(sr_temp.empty == False):
		ret = sr_temp[cols_with_te]
		ret.index= cols
	else:
		ret = pd.Series(.0,index=cols)	
	return ret.tolist()

def get_sire_te_to_sr(accessor_scr, sire_id, cols):
	ret = pd.Series
	sr_temp = qjss.get_record_at_to_sr(accessor_scr, sire_id)
	if(sr_temp.empty == False):
		ret = sr_temp[cols]
	else:
		ret = pd.Series(.0,index=cols)
		pass
	return ret.tolist()

def create_features_list(lst):
	ret =[]
	for item in lst:
		ret.append(torch.tensor(item, dtype=torch.float)) 
	return ret

def create_edge_attr_list(lst):
	ret =[]
	for item in lst:
		ret.append(torch.tensor(item, dtype=torch.float)) 
	return ret



def create_target_list(mean_ranks):
	ret = [1 if rank < 3.5 else 0 for rank in mean_ranks]

	return ret

def create_target(rank):
	return 1 if rank < 4.0 else 0 

def create_mean_rank(sr_horses, df_rank_means):
	# 条件に一致する行を抽出
	matched_rows = df_rank_means[
		(df_rank_means['rr_m_blood01'].isin([sr_horses['rr_m_blood01']])) &
		(df_rank_means['rr_m_blood02'].isin([sr_horses['rr_m_blood02']]))
	]

	# 'smooth_mean'列の値をリストとして取得
	mean_list = matched_rows['smooth_mean'].tolist()
	if(len(mean_list)):
		ret = mean_list[0]
	else:
		print('error mean_list = {len(mean_list)}')
	return ret	

def create_features_element(accessor_acc, accessor_scr, sr_horse, cols_with_te, cols, is_self_include):
	ret=[]
	program_id = sr_horse['rr_r_id']
	if(is_self_include):
		ret.append(get_horse_te_to_sr(accessor_acc, program_id, sr_horse['rr_r_horse_id'], cols_with_te, cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood01'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood02'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood03'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood04'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood05'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood06'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood07'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood08'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood09'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood10'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood11'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood12'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood13'], cols))
	ret.extend(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood14'], cols))
	return ret

def create_couple_edge_attr_element(accessor_lac, sr_horse):
	ret =[]
	couple_zip = zip( [
		sr_horse['rr_m_blood01'],
		sr_horse['rr_m_blood03'],
		sr_horse['rr_m_blood05'],
		sr_horse['rr_m_blood07'],
		sr_horse['rr_m_blood09'],
		sr_horse['rr_m_blood11'],
		sr_horse['rr_m_blood13']
	],
	[
		sr_horse['rr_m_blood02'],
		sr_horse['rr_m_blood04'],
		sr_horse['rr_m_blood06'],
		sr_horse['rr_m_blood08'],
		sr_horse['rr_m_blood10'],
		sr_horse['rr_m_blood12'],
		sr_horse['rr_m_blood14']
	])

	for sire_id, mare_id in couple_zip:
		srw = qjlw.get_record_at_to_sr(accessor_lac, sire_id, mare_id)
		if(srw.empty):
			srw = qjlw.get_zero_data_to_sr(accessor_lac)
		srw.drop(['sire_id','mare_id','upd'], inplace=True)

		srm = qjlm.get_record_at_to_sr(accessor_lac, sire_id, mare_id)
		if(srm.empty):
			srm = qjlm.get_zero_data_to_sr(accessor_lac)
		srm.drop(['sire_id','mare_id','upd'], inplace=True)
  
		src = qjlc.get_record_at_to_sr(accessor_lac, sire_id, mare_id)
		if(src.empty):
			src= qjlc.get_zero_data_to_sr(accessor_lac)
		src.drop(['sire_id','mare_id','upd'], inplace=True)
		#sr = pd.concat([srw, srm, src], axis=0)
		sr = pd.concat([srm, src], axis=0)
		ret.append(sr)

	return ret


def create_parent_edge_attr_element(accessor_lac, sr_horse):
	ret=[]
	parent_zip = zip( [
		# sr_horse['rr_m_blood01'],
		# sr_horse['rr_m_blood02'],
		sr_horse['rr_m_blood03'],
		sr_horse['rr_m_blood04'],
		sr_horse['rr_m_blood05'],
		sr_horse['rr_m_blood06'],
		sr_horse['rr_m_blood07'],
		sr_horse['rr_m_blood08'],
		sr_horse['rr_m_blood09'],
		sr_horse['rr_m_blood10'],
		sr_horse['rr_m_blood11'],
		sr_horse['rr_m_blood12'],
		sr_horse['rr_m_blood13'],
		sr_horse['rr_m_blood14']
	]
	,
	[
		# sr_horse['rr_r_horse_id'],
		# sr_horse['rr_r_horse_id'],
		sr_horse['rr_m_blood01'],
		sr_horse['rr_m_blood01'],
		sr_horse['rr_m_blood02'],
		sr_horse['rr_m_blood02'],
		sr_horse['rr_m_blood03'],
		sr_horse['rr_m_blood03'],
		sr_horse['rr_m_blood04'],
		sr_horse['rr_m_blood04'],
		sr_horse['rr_m_blood05'],
		sr_horse['rr_m_blood05'],
		sr_horse['rr_m_blood06'],
		sr_horse['rr_m_blood06']
	])
	for parent_id, child_id in parent_zip:
		srw = qjlwpc.get_record_at_to_sr(accessor_lac, parent_id, child_id)
		if(srw.empty):
			srw = qjlwpc.get_zero_data_to_sr(accessor_lac)
		srw.drop(['parent_id','child_id','upd'], inplace=True)

		srm = qjlmpc.get_record_at_to_sr(accessor_lac, parent_id, child_id)
		if(srm.empty):
			srm = qjlmpc.get_zero_data_to_sr(accessor_lac)
		srm.drop(['parent_id','child_id','upd'], inplace=True)
  
		src = qjlcpc.get_record_at_to_sr(accessor_lac, parent_id, child_id)
		if(src.empty):
			src= qjlcpc.get_zero_data_to_sr(accessor_lac)
		src.drop(['parent_id','child_id','upd'], inplace=True)
		#sr = pd.concat([srw, srm, src], axis=0)
		sr = pd.concat([ srm, src], axis=0)

		ret.append(sr)

	return ret


def predict_precision(model, device, accessor_acc, accessor_scr, accessor_lac, accessor_lap, condition, df_horses):
	ret=[]
	try:
		gdata = create_mlp_data(
			accessor_acc, accessor_scr, accessor_lac, accessor_lap, 
			df_horses, 
			is_self_include=False,
			data_size=0)

		ret.append("index,horse_no,rfu1,rfu2,predict1,program_id,horse_id,predict2")
		for i, sr_horse in df_horses.iterrows():
			try:
				program_id = sr_horse['rr_r_id']
				horse_id = sr_horse['rr_r_horse_id']
				horse_no = sr_horse['rr_r_horse_no']
    
				new_data = Data(x=gdata['node'][i])
				predicted_proba = predict(model, device, condition, new_data)
				pred_index = -1 #int(y.d+0.5)
				max_probability = predicted_proba.item()
				pred_index+=1
				exp_probability = predicted_proba.item()
	
				element = r"{0},{1},{2},{3},{4:.4f},{5},{6},{7:.4f}".format(
					i,
					horse_no,
					pred_index,
					pred_index,
					exp_probability,
					program_id,
					horse_id,
					max_probability
					)
				ret.append(element)
			except Exception as e:
				ret.append(r"{0},0,0,0,0,0,0,0".format(i))
					
	
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

def create_condition_feature(distance, track):
	ret = pd.Series()
	sr_input = pd.Series(data= np.zeros(len(Cat117BDst.KEY_LIST)), index=Cat117BDst.KEY_LIST, dtype=int)
	sr_input[Cat117BDst.KEYS]=Cat117BDst.to_cats(distance)
	ret = Cat117BDst.to_onehot(sr_input, ret)
	sr_input = pd.Series(data= np.zeros(len(Cat105CTrk2.KEY_LIST)), index=Cat105CTrk2.KEY_LIST, dtype=int)
	sr_input[Cat105CTrk2.KEYS]=Cat105CTrk2.to_cats(track)
	ret = Cat105CTrk2.to_onehot(sr_input, ret)
	return torch.from_numpy(ret.values) 