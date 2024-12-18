import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseVRpc import CatBaseVRpc
import os
import inspect
#006-開催回符号化
class Cat006VRpc(CatBaseVRpc):
	KEY = "cat_rpc"
	KEYS = "cats_rpc"
	KEY_XX="cat_rpc_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_rpc_1"
 
	def __init__(self):
		self.foo = 0 

	#006-開催回符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseVRpc.to_onehot(input, Cat006VRpc.KEY_LIST, Cat006VRpc.KEYS, Cat006VRpc.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		

	#006-開催回符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseVRpc.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(max):
		
		CatBaseVRpc.prepare(max)
		Cat006VRpc.KEY_LIST=[]
		max = len(CatBaseVRpc.CAT_LIST)-1
		for i in range(0,max):
			key = Cat006VRpc.KEY_XX.format(i+1)
			Cat006VRpc.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseVRpc.create_zeros(Cat006VRpc.KEY_LIST)
		temp[Cat006VRpc.DEFAULT_CAT]=1
		return pd.concat([output, temp])

if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	from model.database.drivers.mdb_driver.MdbAccessor import MdbAccessor
	import model.database.query.database_query.QueryJPH as qjph
	accessor = MdbAccessor()
	accessor.open(conf.KJDB_MDB_FILE)
	Cat006VRpc.prepare(accessor)
	handle =codecs.open('Cat006VRpc.txt', 'w')

	max = qjph.get_max_place_count(accessor)
	lst=list(range(1,max))
	inputs=[]
	for i in lst:
		temp = f'{i:02}'
		inputs.append(temp)

	for input in inputs:
		index = Cat006VRpc.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat006VRpc.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat006VRpc.KEY_LIST, dtype=int)
		df_input[Cat006VRpc.KEYS]=input
		ret = Cat006VRpc.to_onehot(df_input,output)
		print(df_input[Cat006VRpc.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

