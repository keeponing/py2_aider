import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd

import model.database.query.database_query.QueryJTE as qjte
import model.database.query.database_query.QueryJSS as qjss
import model.database.query.database_query.QueryJLC as qjlc
import model.database.query.database_query.QueryJLM as qjlm
import model.database.query.database_query.QueryJLW as qjlw
import model.database.query.database_query.QueryJLCPC as qjlcpc
import model.database.query.database_query.QueryJLMPC as qjlmpc
import model.database.query.database_query.QueryJLWPC as qjlwpc
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
from sklearn.model_selection import train_test_split
from tqdm import trange
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GATConv, global_mean_pool


class Net(torch.nn.Module):
    def __init__(self, feature_size):
        super(Net, self).__init__()
        hidden_size = 60
        hidden_size2 = 30
        self.conv1 = GATConv(feature_size, hidden_size, heads=16, concat=False)
        self.conv2 = GATConv(hidden_size, hidden_size2, heads=16, concat=False)
        self.fc1 = nn.Linear(hidden_size2, 1)  # 出力を1ユニットに変更
        self.bn1 = nn.BatchNorm1d(feature_size)
        self.bn2 = nn.BatchNorm1d(hidden_size)
        self.dropout = nn.Dropout(0.3)

    def forward(self, data):
        x, edge_index, batch = data.x, data.edge_index, data.batch
        x = self.bn1(x)
        x = F.leaky_relu(self.conv1(x, edge_index))
        x = self.dropout(x)
        x = self.bn2(x)
        x = F.leaky_relu(self.conv2(x, edge_index))
        x = self.dropout(x)
        x = global_mean_pool(x, batch)
        x = self.fc1(x)
        return x  # シグモイドを削除
    
def get_parent_smooth_rank( df_horses):
	df_horses['rr_r_rank2'] = df_horses['rr_r_rank'].astype(float)
	ret = df_horses.groupby(['rr_m_blood01', 'rr_m_blood02'])['rr_r_rank2'].agg(['mean', 'count']).reset_index()

	mean_master = df_horses['rr_r_rank2'].astype(float).mean()

	ret['smooth_mean'] = ret.apply(lambda row: row['mean'] if row['count'] > 3 else (row['count'] * row['mean'] + (4 - row['count']) * mean_master) / 4, axis=1)
	return ret	

def create_train_data(accessor_acc, accessor_scr, accessor_lac, accessor_lap, df_horses, is_self_include=True, data_size =0):

	cols_with_te=qjte.get_te_col()
	cols = [col.replace('te_', '') for col in cols_with_te]
	df_horses_ex=df_horses[
		['ph_place',
		'rh_distance',
		'rh_track',
		'rr_r_id',
		'rr_r_horse_id',
		'rr_r_gender',
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
	node_features = {}
	edge_attrs = {}
	ranks = {}
	df_rank_means = get_parent_smooth_rank(df_horses)

	for i in trange(len(df_horses_ex), desc="create data"):
		sr_horse = df_horses_ex.iloc[i]
		horse_id = sr_horse['rr_r_horse_id']
		node = create_features_element(accessor_acc, accessor_scr, sr_horse)
		edge = create_edge_attr_element(accessor_lac, accessor_lap, sr_horse)
		rank = float(sr_horse['rr_r_rank'])  # ランクを浮動小数点数に変更
		if len(node) and len(edge):
			node_features[horse_id] = node
			edge_attrs[horse_id] = edge
			ranks[horse_id] = create_mean_rank(sr_horse, df_rank_means)

		if((data_size != 0) and (i==data_size)): #TODO
			print(f"TODO {data_size}")
			break
	ret1 = create_features_list(node_features)
	ret2 = create_target_list(list(ranks.values()))
	ret3 = create_edge_attr_list(edge_attrs)
	return ret1, ret2, ret3

def append_race_header(sr_horse, features):
	rh_distance = float(sr_horse['rh_distance'])
	rh_track = float(sr_horse['rh_track'])
	
	# featuresの各子リストに値を追加
	for feature in features:
		feature.extend([rh_distance, rh_track])
	return  features
	
def get_lineage_edge_own():
	# #馬･父･母･父父･父母･母父･母母･父父父･父父母･父母父･父母母･母父父･母父母･母母父･母母母の順に設定
	# エッジの定義（親子関係）
	edges = [
		(0, 1),  # 馬 -> 父
		(0, 2),  # 馬 -> 母
		(1, 3),  # 父 -> 父父
		(1, 4),  # 父 -> 父母
		(2, 5),  # 母 -> 母父
		(2, 6),  # 母 -> 母母
		(3, 7),  # 父父 -> 父父父
		(3, 8),  # 父父 -> 父父母
		(4, 9),  # 父母 -> 父母父
		(4, 10), # 父母 -> 父母母
		(5, 11), # 母父 -> 母父父
		(5, 12), # 母父 -> 母父母
		(6, 13), # 母母 -> 母母父
		(6, 14),  # 母母 -> 母母母

		# 父母の関係を追加
		(1, 2),  # 父 -> 母
		(3, 4),  # 父父 -> 父母
		(5, 6),  # 母父 -> 母母
		(7, 8), # 父父父 -> 父父母
		(9, 10),# 父母父 -> 父母母
		(11, 12), # 母父父 -> 母父母
		(13, 14) # 母母父 -> 母母母
	]


	edge_attr = [
		1,  # 0: 父 -> 父父
		1,  # 1: 父 -> 父母
		1,  # 2: 母 -> 母父
		1,  # 3: 母 -> 母母
		1,  # 4: 父父 -> 父父父
		1,  # 5: 父父 -> 父父母
		1,  # 6: 父母 -> 父母父
		1,  # 7: 父母 -> 父母母
		1,  # 8: 母父 -> 母父父
		1,  # 9: 母父 -> 母父母
		1,  # 10: 母母 -> 母母父
		1,  # 11: 母母 -> 母母母

		# 夫婦関係
		1,  # 12: 父 -> 母
		1,  # 13: 父父 -> 父母
		1,  # 14: 母父 -> 母母
		1,  # 15: 父父父 -> 父父母
		1,  # 16: 父母父 -> 父母母
		1,  # 17: 母父父 -> 母父母
		1   # 18: 母母父 -> 母母母
	]
	# edge_indexの作成
	edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
	return edge_index, edge_attr

def get_lineage_edge_only():
	# #馬･父･母･父父･父母･母父･母母･父父父･父父母･父母父･父母母･母父父･母父母･母母父･母母母の順に設定
	# エッジの定義（親子関係）
	edges = [
		(0, 2),  # 父 -> 父父
		(0, 3),  # 父 -> 父母
		(1, 4),  # 母 -> 母父
		(1, 5),  # 母 -> 母母
		(2, 6),  # 父父 -> 父父父
		(2, 7),  # 父父 -> 父父母
		(3, 8),  # 父母 -> 父母父
		(3, 9), # 父母 -> 父母母
		(4, 10), # 母父 -> 母父父
		(4, 11), # 母父 -> 母父母
		(5, 12), # 母母 -> 母母父
		(5, 13),  # 母母 -> 母母母

		# 父母の関係を追加
		(0, 1),  # 父 -> 母
		(2, 3),  # 父父 -> 父母
		(4, 5),  # 母父 -> 母母
		(6, 7), # 父父父 -> 父父母
		(8, 9),# 父母父 -> 父母母
		(10, 11), # 母父父 -> 母父母
		(12, 13) # 母母父 -> 母母母
	]

	# edge_attr = [
	# 	1,  # 0: 父 -> 父父
	# 	1,  # 1: 父 -> 父母
	# 	1,  # 2: 母 -> 母父
	# 	1,  # 3: 母 -> 母母
	# 	1,  # 4: 父父 -> 父父父
	# 	1,  # 5: 父父 -> 父父母
	# 	1,  # 6: 父母 -> 父母父
	# 	1,  # 7: 父母 -> 父母母
	# 	1,  # 8: 母父 -> 母父父
	# 	1,  # 9: 母父 -> 母父母
	# 	1,  # 10: 母母 -> 母母父
	# 	1,  # 11: 母母 -> 母母母

	# 	# 夫婦関係
	# 	1,  # 12: 父 -> 母
	# 	1,  # 13: 父父 -> 父母
	# 	1,  # 14: 母父 -> 母母
	# 	1,  # 15: 父父父 -> 父父母
	# 	1,  # 16: 父母父 -> 父母母
	# 	1,  # 17: 母父父 -> 母父母
	# 	1   # 18: 母母父 -> 母母母
	# ]
	#edge_indexの作成
	edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
	return edge_index


	
def predict(model, device, data):
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
        ret = model(data)
    return ret

def check_graph(data):
	'''グラフ情報を表示'''
	print("グラフ構造:", data)
	print("グラフのキー: ", data.keys)
	print("ノード数:", data.num_nodes)
	print("エッジ数:", data.num_edges)
	print("ノードの特徴量数:", data.num_node_features)
	print("孤立したノードの有無:", data.contains_isolated_nodes())
	print("自己ループの有無:", data.contains_self_loops())
	print("====== ノードの特徴量:x ======")
	print(data['x'])
	print("====== ノードのクラス:y ======")
	print(data['y'])
	print("========= エッジ形状 =========")
	print(data['edge_index'])
import matplotlib.pyplot as plt

def draw_score(train_losses, val_losses, r2_scores, mae_scores):
    epochs = range(1, len(train_losses) + 1)

    plt.figure(figsize=(12, 8))

    # Loss plot
    plt.subplot(2, 1, 1)
    plt.plot(epochs, train_losses, 'b-', label='Training Loss')
    plt.plot(epochs, val_losses, 'r-', label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    # Metrics plot
    plt.subplot(2, 1, 2)
    plt.plot(epochs, r2_scores, 'g-', label='R2 Score')
    plt.plot(epochs, mae_scores, 'm-', label='MAE')
    plt.title('R2 Score and MAE')
    plt.xlabel('Epochs')
    plt.ylabel('Score')
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

def create_features_list(node_features):
	ret =[]
	for key, nodes in node_features.items():
		ret.append(torch.tensor(nodes, dtype=torch.float))
	return ret

def create_edge_attr_list(edge_attrs):
	ret =[]
	for key, atrr in edge_attrs.items():
		ret.append(torch.tensor(atrr, dtype=torch.float))
	return ret

# def create_target_list(df_horses, df_rank_means):
# 	# 条件に一致する行を抽出
# 	matched_rows = df_rank_means[
# 		(df_rank_means['rr_m_blood01'].isin(df_horses['rr_m_blood01'])) &
# 		(df_rank_means['rr_m_blood02'].isin(df_horses['rr_m_blood02']))
# 	]

# 	# 'smooth_mean'列の値をリストとして取得
# 	target = matched_rows['smooth_mean'].tolist()

# 	# リストを出力
# 	#print(target)	
# 	ret = torch.tensor(target, dtype=torch.float)
# 	return ret	

def create_target_list(mean_ranks):

	# リストを出力
	#print(target)	
	ret = torch.tensor(mean_ranks, dtype=torch.float)
	return ret	

def create_mean_rank(sr_horses, df_rank_means):
	# 条件に一致する行を抽出
	matched_rows = df_rank_means[
		(df_rank_means['rr_m_blood01'].isin([sr_horses['rr_m_blood01']])) &
		(df_rank_means['rr_m_blood02'].isin([sr_horses['rr_m_blood02']]))
	]

	# 'smooth_mean'列の値をリストとして取得
	ret = matched_rows['smooth_mean'].tolist()
	return ret	

# def create_features_element(accessor_acc, accessor_scr, sr_horse, cols_with_te, cols, is_self_include):
# 	ret=[]
# 	program_id = sr_horse['rr_r_id']
# 	if(is_self_include):
# 		ret.append(get_horse_te_to_sr(accessor_acc, program_id, sr_horse['rr_r_horse_id'], cols_with_te, cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood01'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood02'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood03'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood04'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood05'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood06'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood07'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood08'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood09'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood10'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood11'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood12'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood13'], cols))
# 	ret.append(get_sire_te_to_sr(accessor_scr, sr_horse['rr_m_blood14'], cols))
# 	#ret = append_race_header(sr_horse, ret) 
# 	return ret

def convert_gender_code_to_onehot(val):
    return int(val)-1

def create_features_element(accessor_acc, accessor_scr, sr_horse):
	ret=[]
	program_id = sr_horse['rr_r_id']
	cols = ['gender']
	
	ret.append(pd.Series(data=[0], index=cols))
	ret.append(pd.Series(data=[1], index=cols))
	ret.append(pd.Series(data=[0], index=cols))
	ret.append(pd.Series(data=[1], index=cols))
	ret.append(pd.Series(data=[0], index=cols))
	ret.append(pd.Series(data=[1], index=cols))
	ret.append(pd.Series(data=[0], index=cols))
	ret.append(pd.Series(data=[1], index=cols))
	ret.append(pd.Series(data=[0], index=cols))
	ret.append(pd.Series(data=[1], index=cols))
	ret.append(pd.Series(data=[0], index=cols))
	ret.append(pd.Series(data=[1], index=cols))
	ret.append(pd.Series(data=[0], index=cols))
	ret.append(pd.Series(data=[1], index=cols))

	return ret

def create_edge_attr_element(accessor_lac, accessor_lap, sr_horse):
	
	ret = create_parent_edge_attr_element(accessor_lap, sr_horse)
	ret2 = create_couple_edge_attr_element(accessor_lac, sr_horse)
	ret.extend(ret2)
	
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
		sr = pd.concat([srw, srm, src], axis=0)
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
		sr = pd.concat([srw, srm, src], axis=0)
		ret.append(sr)

	return ret