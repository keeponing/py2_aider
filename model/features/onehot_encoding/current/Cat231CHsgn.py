import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd

from model.features.onehot_encoding.base.CatBaseCHsgn import CatBaseCHsgn
import os
import inspect
#231-馬記号コード
class Cat231CHsgn(CatBaseCHsgn):
	KEY = "cat_hsgn"
	KEYS = "cats_hsgn"
	KEY_XX="cat_hsgn_{0}"
	KEY_LIST = []

	DEFAULT_CAT = "cat_hsgn_3"
 
	def __init__(self):
		self.foo = 0 

	#231-馬記号コード
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCHsgn.to_onehot(input, Cat231CHsgn.KEY_LIST, Cat231CHsgn.KEYS, Cat231CHsgn.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#231-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCHsgn.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCHsgn.prepare(df_code)
		max = len(CatBaseCHsgn.CAT_LIST)-1
		for i in range(0,max):
			key = Cat231CHsgn.KEY_XX.format(i+1)
			Cat231CHsgn.KEY_LIST.append(key)


	@staticmethod
	def create_zeros(output):
		temp = CatBaseCHsgn.create_zeros(Cat231CHsgn.KEY_LIST)
		temp[Cat231CHsgn.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
			dtype=str	
			)
	Cat231CHsgn.prepare(df_code)
	handle =codecs.open('Cat231CHsgn.txt', 'w')
	inputs = ["0","01","02","03","04","05","06","07","08","09","10","11","12","15","16","17","18","19","20","21","22","23","24","25","26","27","31","40","41",]

	for input in inputs:
		index = Cat231CHsgn.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat231CHsgn.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat231CHsgn.KEY_LIST, dtype=int)

		df_input[Cat231CHsgn.KEYS]=input
		ret = Cat231CHsgn.to_onehot(df_input,output)
		print(df_input[Cat231CHsgn.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

