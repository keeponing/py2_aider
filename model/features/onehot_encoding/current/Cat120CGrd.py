import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCGrd import CatBaseCGrd
import os
import inspect
#120-グレード符号化
class Cat120CGrd(CatBaseCGrd):
	KEY = "cat_grd"
	KEYS = "cats_grd"
	KEY_XX="cat_grd_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_grd_9"
	def __init__(self):
		self.foo = 0 

	#120-グレード符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCGrd.to_onehot(input, Cat120CGrd.KEY_LIST, Cat120CGrd.KEYS, Cat120CGrd.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#120-グレード符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCGrd.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	
	@staticmethod
	def prepare(df_code):
		CatBaseCGrd.prepare(df_code)
		Cat120CGrd.KEY_LIST=[]
		max = len(CatBaseCGrd.CAT_LIST)-1
		for i in range(0,max):
			key = Cat120CGrd.KEY_XX.format(i+1)
			Cat120CGrd.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCGrd.create_zeros(Cat120CGrd.KEY_LIST)
		temp[Cat120CGrd.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE,
				dtype=str	
				)
	Cat120CGrd.prepare(df_code)
	handle =codecs.open('Cat120CGrd.txt', 'w')
	inputs = ["A","B","C","D","E","F","G","H","L",""]

	for input in inputs:
		index = Cat120CGrd.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat120CGrd.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat120CGrd.KEY_LIST, dtype=int)

		df_input[Cat120CGrd.KEYS]=input
		ret = Cat120CGrd.to_onehot(df_input,output)
		print(df_input[Cat120CGrd.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
