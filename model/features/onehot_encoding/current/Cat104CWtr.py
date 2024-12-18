import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCWtr import CatBaseCWtr
import os
import inspect
#104-天候符号化
class Cat104CWtr(CatBaseCWtr):
	KEY = "cat_wtr"
	KEYS = "cats_wtr"
	KEY_XX="cat_wtr_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_wtr_3"
  
	def __init__(self):
		self.foo=0 

	#104-性別符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp = CatBaseCWtr.to_onehot(input, Cat104CWtr.KEY_LIST, Cat104CWtr.KEYS, Cat104CWtr.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#104-天候符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCWtr.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		CatBaseCWtr.prepare(df_code)
		max = len(CatBaseCWtr.CAT_LIST)-1
		for i in range(0,max):
			key = Cat104CWtr.KEY_XX.format(i+1)
			Cat104CWtr.KEY_LIST.append(key)


	@staticmethod
	def create_zeros(output):
		temp = CatBaseCWtr.create_zeros(Cat104CWtr.KEY_LIST)
		temp[Cat104CWtr.DEFAULT_CAT] =1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat104CWtr.prepare(df_code)
	handle =codecs.open('Cat104CWtr.txt', 'w')
	inputs = ['0','1','2','3','4','5','6']
	print("Cat104CWtr", file=handle)
	for input in inputs:
		index = Cat104CWtr.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat104CWtr.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat104CWtr.KEY_LIST, dtype=int)
		df_input[Cat104CWtr.KEYS]=input
		ret = Cat104CWtr.to_onehot(df_input,output)
		print(df_input[Cat104CWtr.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

