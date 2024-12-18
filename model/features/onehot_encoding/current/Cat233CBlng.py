import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd

from model.features.onehot_encoding.base.CatBaseCBlng import CatBaseCBlng
import os
import inspect
#233-東西所属コード符号化
class Cat233CBlng(CatBaseCBlng):
	KEY = "cat_blng"
	KEYS = "cats_blng"
	KEY_XX="cat_blng_{0}"
	KEY_LIST = []

	def __init__(self):
		self.foo = 0 
			
	#233-東西所属コード符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp= CatBaseCBlng.to_onehot(input, Cat233CBlng.KEY_LIST, Cat233CBlng.KEYS, Cat233CBlng.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		
	#233-東西所属コード符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCBlng.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		CatBaseCBlng.prepare(df_code)
		max = len(CatBaseCBlng.CAT_LIST)-1
		for i in range(0,max):
			key = Cat233CBlng.KEY_XX.format(i+1)
			Cat233CBlng.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCBlng.create_zeros(Cat233CBlng.KEY_LIST)
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat233CBlng.prepare(df_code)
	handle =codecs.open('Cat233CBlng.txt', 'w')
	inputs = ['0','1','2','3','4',]
	for input in inputs:
		index = Cat233CBlng.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat233CBlng.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat233CBlng.KEY_LIST, dtype=int)

		df_input[Cat233CBlng.KEYS]=input
		ret = Cat233CBlng.to_onehot(df_input,output)
		print(df_input[Cat233CBlng.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
