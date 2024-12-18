from nnabla.utils.nnp_graph import NnpLoader
import model.utility.k_jra_util as util
import os
import inspect
import model.utility.k_predict_util as predict_util
import numpy as np
#精度優先モデル
def predict_precision(place_code, class_code, df):
	ret=[]
	try:

		# 予測モデルを復元
		#model_file = conf.NNC_MODELS_FOLDER+"\{}_model.nnp".format(model)
		model_file = predict_util.get_nnc_p_file_at(place_code, class_code)
		nnp = NnpLoader(model_file)
		net = nnp.get_network("MainRuntime", batch_size = 1)
		x=list(net.inputs.values())[0]
		y=list(net.outputs.values())[0]
		df_horse_no=df['desc_horse_no']
		df_program_id = df['key_program_id'] 
		df_horse_id = df['key_horse_id']
		
		df = df.drop(columns=[
			'obj_rank', 
			'desc_horse_no',
			])
		cols = util.convert_dataframe_columns(df)

		df = df.rename(columns=cols)
		index=0
		ret.append(" ,desc_horse_no,predict,class_code,program_id,horse_id")
		temp_list =[]
		for i in range(0,len(df)):
			try:
				dt=df.iloc[i]
				program_id = int(df_program_id[i])
				horse_id = int(df_horse_id[i])
			
				dt=dt.astype('f')
				x.d = dt.values 
				y.forward() 
				pred_index = -1 #int(y.d+0.5)
				#pred_index = int(np.argmax(y.d)) # 分類からの結果取得
				max_probability = y.d[0][0].T
				pred_index+=1
				#クラス1位以上の予想が出たときはそちらの値を採用
				exp_probability =y.d[0][0].T
				# if(pred_index < class_top_index):
				# 	exp_probability = y.d[0][pred_index].T
				#クラス1位以上の予想が出たときはそちらの値を採用
				# else:	
				# 	exp_probability  = y.d[0][class_top_index].T
				#期待値を計算
				#確率変数を設定
				# pv=range(1,4)
				# mat = y.d[0]
				# exp_rank = int(np.dot(pv, mat))
			
				temp_list.append(zip(
					index,
					df_horse_no[index],
					pred_index,
					pred_index,
					exp_probability,
					program_id,
					horse_id,
					max_probability
					))
			except Exception as e:
				temp_list.append(zip(
					index,
					df_horse_no[index],
					0,
					0,
					0,
					0,
					0,
					0
					))		
			index+=1
		temp2_list = temp_list
		ret.append(r"{0},{1},{2},{3},{4:.4f},{5},{6},{7}".format(
				temp2_list[0],
				temp2_list[1],
				temp2_list[2],
				temp2_list[3],
				temp2_list[4],
				temp2_list[5],
				temp2_list[6],
				temp2_list[7]
				))
		nnp= None
		net=None	
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

#精度優先モデル
def predict_rough(place_code, class_code, df):
	ret=[]
	try:

		# 予測モデルを復元
		#model_file = conf.NNC_MODELS_FOLDER+"\{}_model.nnp".format(model)
		model_file = predict_util.get_nnc_r_file_at(place_code, class_code)
		nnp = NnpLoader(model_file)
		#net = nnp.get_network("推論ネットワーク名",batch_size = 1)
		#net = nnp.get_network("MainRuntime", batch_size = 1)
		net = nnp.get_network("MainRuntime", batch_size = 1)
		#print(df_rst)
		x=list(net.inputs.values())[0]
		y=list(net.outputs.values())[0]
		df_horse_no=df['desc_horse_no']
		df_program_id = df['key_program_id'] 
		df_horse_id = df['key_horse_id']
		
		df = df.drop(columns=[
			'obj_rank', 
			'desc_horse_no',
			# 'key_program_id', 
			# 'key_horse_id',
			])
		cols = util.convert_dataframe_columns(df)

		df = df.rename(columns=cols)
		#df.to_csv("aaa.csv")
		#df = drop_columns(df)
		
		#df.to_csv("{0}.csv".format(model))
		index=0
		ret.append(" ,desc_horse_no,predict,class_code,program_id,horse_id")
		for i in range(0,len(df)):
			dt=df.iloc[i]
			program_id = int(df_program_id[i])
			horse_id = int(df_horse_id[i])
			#dt=dt[1]
		
			dt=dt.astype('f')
			x.d = dt.values 
			y.forward() 
			pred_index = -1 #int(y.d+0.5)
			#pred_index = int(np.argmax(y.d)) # 分類からの結果取得
			max_probability = y.d[0][0].T
			pred_index+=1
			#クラス1位以上の予想が出たときはそちらの値を採用
			exp_probability =y.d[0][0].T
			# if(pred_index < class_top_index):
			# 	exp_probability = y.d[0][pred_index].T
			#クラス1位以上の予想が出たときはそちらの値を採用
			# else:	
			# 	exp_probability  = y.d[0][class_top_index].T
			#期待値を計算
			#確率変数を設定
			# pv=range(1,4)
			# mat = y.d[0]
			# exp_rank = int(np.dot(pv, mat))
			ret.append(r"{0},{1},{2},{3},{4:.4f},{5},{6},{7:.4f}".format(
				index,
				df_horse_no[index],
				pred_index,
				pred_index,
				exp_probability,
				program_id,
				horse_id,
				max_probability
				))
			index+=1
		nnp= None
		net=None	
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

def get_max_index(arr):
	ret =0
	temp=0
	count =1
	for val in arr[0] :
		if(temp < val):
			temp =val
			ret = count
		count+=1
	return ret

def calc_variance_mode(temp_list):
	exp_probability = [t[4] for t in temp_list] # exp_probabilityの値だけを取り出す
	mean = np.mean(exp_probability) # 平均値を計算
	std = np.std(exp_probability) # 標準偏差を計算

	# 3σの範囲を定義
	threshold_3sigma = mean + 3 * std
	threshold_2sigma = mean + 2 * std

	result_list = []
	for value in exp_probability:
		if value >= threshold_3sigma:
			result_list.append(2)
		elif value >= threshold_2sigma:
			result_list.append(1)
		else:
			result_list.append(0)
	ret = []
	for i in range(temp_list):
		element = temp_list[i]
		ret.append(zip(
					element[0],
					element[1],
					element[2],
					element[3],
					element[4],
					element[5],
					element[6],
					result_list[i]
					))
	return ret
