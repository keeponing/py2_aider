from nnabla.utils.nnp_graph import NnpLoader
import numpy as np
import model.conf.KJraConfig as conf
import model.utility.k_jra_util as util
import os
import inspect

#精度優先モデル
def predict_precision(toku_code, df):
	ret=[]
	try:
		#df.to_csv("aaa.csv")
		# 予測モデルを復元
		model_file = conf.NNC_MODELS_FOLDER+f"\\kjvan_model_{toku_code}_p.nnp"
		if(os.path.exists(model_file)):
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
			
			#df = df.drop(columns=get_drop_columns())
			df = df.drop(columns=[
				'obj_rank', 
				'desc_horse_no',
				# 'key_program_id', 
				# 'key_horse_id',
				])		
			cols = util.convert_dataframe_columns(df)

			df = df.rename(columns=cols)
			
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
				#pred = int(y.d+0.5)
				pred_index = int(np.argmax(y.d)) # 分類からの結果取得
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
				pv=range(1,4)
				mat = y.d[0]
				exp_rank = int(np.dot(pv, mat))
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

#精度優先モデル
def predict_rough(model, df):
	ret=[]
	try:

		# 予測モデルを復元
		#model_file = conf.NNC_MODELS_FOLDER+"\{}_model.nnp".format(model)
		model_file = conf.NNC_MODELS_FOLDER+"\\kjvan_model_cls_r.nnp"
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
		
		df = df.drop(columns=get_drop_columns())
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
			#pred = int(y.d+0.5)
			pred_index = int(np.argmax(y.d)) # 分類からの結果取得
			max_probability = y.d[0][pred_index].T
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
			pv=range(1,4)
			mat = y.d[0]
			exp_rank = int(np.dot(pv, mat))
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

def get_drop_columns():
	return [
		'obj_rank', 
		'desc_horse_no',
		'cat_plc_1',
		'cat_plc_2',
		'cat_plc_3',
		'cat_plc_4',
		'cat_plc_4',
		'cat_plc_5',
		'cat_plc_6',
		'cat_plc_7',
		'cat_plc_8',
		'cat_plc_9',
		'cat_plc_10',
		'cat_plc_11',
		'cat_mnt_cos',
		'cat_mnt_sin',
		'cat_trk2_0',
		'cat_trk2_1',
		'cat_trk2_2',
		'cat_trk2_3',
		'cat_trk2_4',
		'cat_trk2_5',
		'cat_dst_1',
		'cat_dst_2',
		'cat_dst_3',
		'cat_dst_4',
		'cat_dst_5',
		'cat_dst_6',
		'cat_dst_7',
		'cat_dst_8',
		'cat_dst_9',
		'cat_dst_10',
		'cat_dst_11',
		'cat_dst_12',
		'cat_dst_13',
		'cat_dst_14',
		'cat_dst_15',
		'cat_dst_16',
		'cat_dst_17',
		'cat_dst_18',
		'cat_dst_19',
		'cat_dst_20',
		'cat_dst_21',
		'cat_dst_22',
		'cat_dst_23',
		'cat_dst_24',
		'cat_dst_25',
		'cat_dst_26',
		'cat_dst_27',
		'cat_clst_1',
		'cat_clst_2',
		'cat_clst_3',
		'cat_clst_4',
		'cat_clst_5',
		'cat_clst_6',
		'cat_grd_1',
		'cat_grd_2',
		'cat_grd_3',
		'cat_grd_4',
		'cat_grd_5',
		'cat_grd_6',
		'cat_grd_7',
		'cat_grd_8',
		'cat_grd_9',
		'cat_jmk_1',
		'cat_jmk_2',
		'cat_jmk_3',

	]
