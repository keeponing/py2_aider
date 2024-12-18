import sys
sys.path.append(r"C:\Dev\py2")

import numpy as np
import pandas as pd
import os
import inspect
from model.features.onehot_encoding.base.CatBaseCJblng import CatBaseCJblng
import os
import inspect
#241-JRA施設在きゅうフラグ符号化
class Cat241CJblng(CatBaseCJblng):
	KEY = "cat_jblng"
	KEYS = "cats_jblng"
	KEY_XX="cat_jblng_{0}"
	KEY_LIST = []


	def __init__(self):
		self.foo = 0 

	#241-JRA施設在きゅうフラグ符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCJblng.to_onehot(input, Cat241CJblng.KEY_LIST, Cat241CJblng.KEYS, Cat241CJblng.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#241-JRA施設在きゅうフラグ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCJblng.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		Cat241CJblng.KEY_LIST=[]
		for i in range(0,1):
			key = Cat241CJblng.KEY_XX.format(i+1)
			Cat241CJblng.KEY_LIST.append(key)


	@staticmethod
	def create_zeros(output):
		temp = CatBaseCJblng.create_zeros(Cat241CJblng.KEY_LIST)
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat241CJblng.prepare()
	handle =codecs.open('Cat241CJblng.txt', 'w')
	inputs = ['0','1']

	for input in inputs:
		index = Cat241CJblng.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat241CJblng.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat241CJblng.KEY_LIST, dtype=int)

		df_input[Cat241CJblng.KEYS]=input
		ret = Cat241CJblng.to_onehot(df_input,output)
		print(df_input[Cat241CJblng.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

