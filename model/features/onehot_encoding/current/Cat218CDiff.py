import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCDiff import CatBaseCDiff
import os
import inspect
#218-着差コード
class Cat218CDiff(CatBaseCDiff):
	KEY = "cat_diff2"
	KEYS = "cats_diff2"
	KEY_XX="cat_diff2_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_diff2_3"
 
	def __init__(self):
		self.foo = 0 

	#218-着差コード
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCDiff.to_onehot(input, Cat218CDiff.KEY_LIST, Cat218CDiff.KEYS, Cat218CDiff.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#218-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCDiff.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCDiff.prepare(df_code)
		max = len(CatBaseCDiff.CAT_LIST)-1
		for i in range(0,max):
			key = Cat218CDiff.KEY_XX.format(i+1)
			Cat218CDiff.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCDiff.create_zeros(Cat218CDiff.KEY_LIST)
		temp[Cat218CDiff.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE,
				dtype=str	
				)
	Cat218CDiff.prepare(df_code)
	handle =codecs.open('Cat218CDiff.txt', 'w')
	inputs = ["","000","1","112","114","12","134","14","2","212","214","234","3","312","314","334","34","4","412","414","434","5","512","514","534","6","612","614","634","7","712","714","734","8","812","814","834","9","A","D","H","K","T","Z"]

	for input in inputs:
		index = Cat218CDiff.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseCDiff.CAT_LIST))

	for input in inputs:
		zeros = np.zeros(len(Cat218CDiff.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat218CDiff.KEY_LIST, dtype=int)

		df_input[Cat218CDiff.KEYS]=input
		ret = Cat218CDiff.to_onehot(df_input,output)
		print(df_input[Cat218CDiff.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)