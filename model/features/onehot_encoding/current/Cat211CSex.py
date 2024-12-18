import sys
sys.path.append(r"C:\Dev\py2")

import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCSex import CatBaseCSex
import os
import inspect
#211-性別符号化
class Cat211CSex(CatBaseCSex):
	KEY = "cat_sex"	
	KEYS = "cats_sex"
	KEY_XX="cat_sex_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_sex_2"
 
	def __init__(self):
		self.foo = 0 

	#211-性別符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp = CatBaseCSex.to_onehot(input, Cat211CSex.KEY_LIST, Cat211CSex.KEYS, Cat211CSex.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#211-性別符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCSex.to_cats(input)
			if  4<ret:
				ii=0
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		CatBaseCSex.prepare(df_code)
		max = len(CatBaseCSex.CAT_LIST)-1
		for i in range(0,max):
			key = Cat211CSex.KEY_XX.format(i+1)
			Cat211CSex.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		#default 
		temp = CatBaseCSex.create_zeros(Cat211CSex.KEY_LIST)
		temp[Cat211CSex.DEFAULT_CAT] =1 
		return pd.concat([output, temp])

if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs

	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat211CSex.prepare(df_code)
	handle =codecs.open('Cat211CSex.txt', 'w')

	inputs = ['0','1','2','3']
	for input in inputs:
		index = Cat211CSex.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))
	for input in inputs:
		zeros = np.zeros(len(Cat211CSex.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat211CSex.KEY_LIST, dtype=int)
		df_input[Cat211CSex.KEYS]=input
		ret = Cat211CSex.to_onehot(df_input,output)
		print(df_input[Cat211CSex.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
