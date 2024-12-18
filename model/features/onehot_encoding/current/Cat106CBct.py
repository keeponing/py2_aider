import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCBc import CatBaseCBc
import os
import inspect
#106-芝馬場状態符号化
class Cat106CBct(CatBaseCBc):
	KEY = "cat_bct"
	KEYS = "cats_bct"
	KEY_XX="cat_bct_{0}"
	KEY_LIST = []

	def __init__(self):
		self.foo = 0 
			
	#106-馬場状態符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp= CatBaseCBc.to_onehot(input, Cat106CBct.KEY_LIST, Cat106CBct.KEYS, Cat106CBct.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		
	#106-馬場状態符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCBc.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		CatBaseCBc.prepare(df_code)
		max = len(CatBaseCBc.CAT_LIST)-1
		for i in range(0,max):
			key = Cat106CBct.KEY_XX.format(i+1)
			Cat106CBct.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCBc.create_zeros(Cat106CBct.KEY_LIST)
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat106CBct.prepare(df_code)
	handle =codecs.open('Cat106CBct.txt', 'w')
	inputs = ['0','1','2','3','4',]
	for input in inputs:
		index = Cat106CBct.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat106CBct.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat106CBct.KEY_LIST, dtype=int)

		df_input[Cat106CBct.KEYS]=input
		ret = Cat106CBct.to_onehot(df_input,output)
		print(df_input[Cat106CBct.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
