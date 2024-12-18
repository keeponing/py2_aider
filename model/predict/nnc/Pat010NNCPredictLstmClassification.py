from nnabla.utils.nnp_graph import NnpLoader
import model.conf.KJraConfig as conf
import model.utility.k_jra_util as util
import numpy as np
import os
import inspect
_nnp1 = None
_nnp2 = None
def predict(df):
	lstm_0 = .0
	lstm_1 = .0
	lstm_2 = .0
	lstm_3 = .0
	try:
		global _nnp1

		if(_nnp1 == None):
			# 予測モデルを復元
			model_file = conf.NNC_MODELS_FOLDER+"\kjvan_model_l4.nnp"
			_nnp1 = NnpLoader(model_file)

			#net = nnp.get_network("推論ネットワーク名",batch_size = 1)
		net = _nnp1.get_network("MainRuntime", batch_size = 1)

		#print(df_rst)
		x=list(net.inputs.values())[0]
		y=list(net.outputs.values())[0]
		
		#df.to_csv("aaa.csv")
		df = df.drop(columns=[
			'obj_rank', 
			'desc_horse_no',
			# 'key_program_id', 
			# 'key_horse_id',
			])
		cols = util.convert_dataframe_columns(df)
		#df.to_csv("{0}.csv".format("aaaa"))
		df = df.rename(columns=cols)
		# ファイルに出力する
		#export_column_types(df, 'column_types.csv')
		#dt=df.iloc[0]
	
		# 数値型の列を選択する
		#num_cols = df.select_dtypes(include=np.number).columns

		# 選択した列をfloat型にキャストする
		#df[num_cols] = df[num_cols].astype(float)
		
		df['x__0:key_program_id'] = 0
		df['x__1:key_horse_id'] = 0
		df.fillna(0.0, inplace=True) 
		#df.to_csv("{0}.csv".format("aaaa"))
		df = df.astype(float)
		x.d = df.values 
		y.forward() 
		#pred = int(y.d+0.5)
		lstm_0 = y.d[0][0].T
		lstm_1 = y.d[0][1].T
		lstm_2 = y.d[0][2].T
		lstm_3 = y.d[0][3].T
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return lstm_0,lstm_1,lstm_2,lstm_3




def predict_sc(df):
	lstm_0 = .0
	lstm_1 = .0
	lstm_2 = .0
	lstm_3 = .0
	try:
		global _nnp2

		if(_nnp2 == None):
			# 予測モデルを復元
			
			model_file = conf.NNC_MODELS_FOLDER+"\kjvan_model_sc_l4.nnp"
			_nnp2 = NnpLoader(model_file)
			#net = nnp.get_network("推論ネットワーク名",batch_size = 1)
		net = _nnp2.get_network("MainRuntime", batch_size = 1)

		#print(df_rst)
		x=list(net.inputs.values())[0]
		y=list(net.outputs.values())[0]
		
		#df.to_csv("aaa.csv")
		df = df.drop(columns=[
			'obj_rank', 
			'desc_horse_no',
			# 'key_program_id', 
			# 'key_horse_id',
			])
		cols = util.convert_dataframe_columns(df)

		df = df.rename(columns=cols)
		#df.to_csv("{0}.csv".format(model))
	
		#dt=df.iloc[0]
		df['x__0:key_program_id'] = 0
		df['x__1:key_horse_id'] = 0
		df.fillna(0.0, inplace=True) 
		#df.to_csv("{0}.csv".format("aaaa"))
		df = df.astype(float)
		
		x.d = df.values 
		y.forward() 
		#pred = int(y.d+0.5)
		lstm_0 = y.d[0][0].T
		lstm_1 = y.d[0][1].T
		lstm_2 = y.d[0][2].T
		lstm_3 = y.d[0][3].T
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return lstm_0,lstm_1,lstm_2,lstm_3

# typesをファイルに出力する関数
def export_column_types(df, file_path):
    types = df.dtypes.reset_index()
    types.columns = ['列名', 'データ型']
    types.to_csv(file_path, index=False)


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