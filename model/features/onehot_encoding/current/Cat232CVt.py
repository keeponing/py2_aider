import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd

from model.features.onehot_encoding.base.CatBaseCVt import CatBaseCVt
import os
import inspect
#232-品種コード
class Cat232CVt(CatBaseCVt):
	KEY = "cat_vt"
	KEYS = "cats_vt"
	KEY_XX="cat_vt_{0}"
	KEY_LIST = []

	DEFAULT_CAT = "cat_vt_3"
 
	def __init__(self):
		self.foo = 0 

	#232-品種コード
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCVt.to_onehot(input, Cat232CVt.KEY_LIST, Cat232CVt.KEYS, Cat232CVt.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#232-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCVt.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCVt.prepare(df_code)
		max = len(CatBaseCVt.CAT_LIST)-1
		for i in range(0,max):
			key = Cat232CVt.KEY_XX.format(i+1)
			Cat232CVt.KEY_LIST.append(key)


	@staticmethod
	def create_zeros(output):
		temp = CatBaseCVt.create_zeros(Cat232CVt.KEY_LIST)
		temp[Cat232CVt.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
			dtype=str	
			)
	Cat232CVt.prepare(df_code)
	handle =codecs.open('Cat232CVt.txt', 'w')
	inputs = ["0","1","2","3","4","5","6","7","8"]

	for input in inputs:
		index = Cat232CVt.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat232CVt.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat232CVt.KEY_LIST, dtype=int)

		df_input[Cat232CVt.KEYS]=input
		ret = Cat232CVt.to_onehot(df_input,output)
		print(df_input[Cat232CVt.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

