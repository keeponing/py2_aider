import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCRcnd import CatBaseCRcnd
import os
import inspect
#116-負担重量条件符号化
class Cat116CRcnd(CatBaseCRcnd):
	KEY = "cat_rcnd"
	KEYS = "cats_rcnd"
	KEY_XX="cat_rcnd_{0}"
	KEY_LIST = []

	def __init__(self):
		self.foo = 0 
  
	#116-負担重量条件符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCRcnd.to_onehot(input, Cat116CRcnd.KEY_LIST, Cat116CRcnd.KEYS, Cat116CRcnd.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#116-負担重量条件符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCRcnd.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		CatBaseCRcnd.prepare(df_code)
		max = len(CatBaseCRcnd.CAT_LIST)-1
		for i in range(0,max):
			key = Cat116CRcnd.KEY_XX.format(i+1)
			Cat116CRcnd.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCRcnd.create_zeros(Cat116CRcnd.KEY_LIST)
		#DEFAULT=0
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE,
				dtype=str	
				)
	Cat116CRcnd.prepare(df_code)
	handle =codecs.open('Cat116CRcnd.txt', 'w')
	inputs = ['0','1','2','3','4']

	for input in inputs:
		index = Cat116CRcnd.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat116CRcnd.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat116CRcnd.KEY_LIST, dtype=int)

		df_input[Cat116CRcnd.KEYS]=input
		ret = Cat116CRcnd.to_onehot(df_input,output)
		print(df_input[Cat116CRcnd.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
