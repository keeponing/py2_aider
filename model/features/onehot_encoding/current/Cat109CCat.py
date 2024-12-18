import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCCat import CatBaseCCat
import os
import inspect
#109-カテゴリ符号化
class Cat109CCat(CatBaseCCat):
	KEY = "cat_cat"
	KEYS = "cats_cat"
	KEY_XX="cat_cat_{0}"
	KEY_LIST = []

	DEFAULT_CAT = "cat_cat_3"
 
	def __init__(self):
		self.foo = 0 

	#109-カテゴリ符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCCat.to_onehot(input, Cat109CCat.KEY_LIST, Cat109CCat.KEYS, Cat109CCat.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#109-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCCat.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCCat.prepare(df_code)
		max = len(Cat109CCat.CAT_LIST)-1
		for i in range(0,max):
			key = Cat109CCat.KEY_XX.format(i+1)
			Cat109CCat.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCCat.create_zeros(Cat109CCat.KEY_LIST)
		temp[Cat109CCat.DEFAULT_CAT]=1
		return pd.concat([output, temp])

if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat109CCat.prepare(df_code)
	handle =codecs.open('Cat109CCat.txt', 'w')
	inputs = ['00','11','12','13','14','18','19','21','22','23','24',]
	for input in inputs:
		index = Cat109CCat.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat109CCat.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat109CCat.KEY_LIST, dtype=int)

		df_input[Cat109CCat.KEYS]=input
		ret = Cat109CCat.to_onehot(df_input,output)
		print(df_input[Cat109CCat.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
