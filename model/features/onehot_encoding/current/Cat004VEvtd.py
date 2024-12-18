import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseVEvd import CatBaseVEvd
import os
import inspect
#004-開催日符号化
class Cat004VEvtd(CatBaseVEvd):
	KEY = "cat_evtd"
	KEYS = "cats_evtd"
	KEY_XX="cat_evtd_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_evtd_1"
 
	def __init__(self):
		self.foo = 0 
  
	#004-開催日符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseVEvd.to_onehot(input, Cat004VEvtd.KEY_LIST, Cat004VEvtd.KEYS, Cat004VEvtd.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#004-開催日符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseVEvd.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(max):
		CatBaseVEvd.prepare(max)
		Cat004VEvtd.KEY_LIST=[]
		max = len(CatBaseVEvd.CAT_LIST)-1
		for i in range(0,max):
			key = Cat004VEvtd.KEY_XX.format(i+1)
			Cat004VEvtd.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseVEvd.create_zeros(Cat004VEvtd.KEY_LIST)
		temp[Cat004VEvtd.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	from model.database.drivers.mdb_driver.MdbAccessor import MdbAccessor
	import model.database.query.database_query.QueryJPH as qjph
	accessor = MdbAccessor()
	accessor.open(conf.KJDB_MDB_FILE)
	Cat004VEvtd.prepare(accessor)
	handle =codecs.open('Cat004VEvtd.txt', 'w')

	max = qjph.get_max_count(accessor)
	lst=list(range(1,max))
	inputs=[]
	for i in lst:
		temp = f'{i:02}'
		inputs.append(temp)

	for input in inputs:
		index = Cat004VEvtd.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat004VEvtd.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat004VEvtd.KEY_LIST, dtype=int)
		df_input[Cat004VEvtd.KEYS]=input
		ret = Cat004VEvtd.to_onehot(df_input,output)
		print(df_input[Cat004VEvtd.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
