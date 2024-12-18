import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd

from model.features.onehot_encoding.base.CatBaseCErr import CatBaseCErr
import os
import inspect
#232-異常区分コード
class Cat268CErr(CatBaseCErr):
	KEY = "cat_err"
	KEYS = "cats_err"
	KEY_01="cat_err_1"
	KEY_LIST = []

	DEFAULT_CAT = "cat_err_1"
 
	def __init__(self):
		self.foo = 0 

	#232-異常区分コード
	@staticmethod
	def to_onehot(input, output):
		try:
			zeros = np.zeros(1)
			temp = pd.Series(data= zeros, index=[Cat268CErr.KEY_01], dtype=int)
			index = int(input[Cat268CErr.KEYS])
			if(0 != index):
				temp[Cat268CErr.KEY_01] =1
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#232-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCErr.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCErr.prepare(df_code)



	@staticmethod
	def create_zeros(output):
		temp = CatBaseCErr.create_zeros(Cat268CErr.KEY_LIST)
		temp[Cat268CErr.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
			dtype=str	
			)
	Cat268CErr.prepare(df_code)
	handle =codecs.open('Cat268CErr.txt', 'w')
	inputs = ["0","1","2","3","4","5","6","7"]

	for input in inputs:
		index = Cat268CErr.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat268CErr.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat268CErr.KEY_LIST, dtype=int)

		df_input[Cat268CErr.KEYS]=input
		ret = Cat268CErr.to_onehot(df_input,output)
		print(df_input[Cat268CErr.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

