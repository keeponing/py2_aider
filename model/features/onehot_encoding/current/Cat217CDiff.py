import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCDiff import CatBaseCDiff
import os
import inspect
#217-着差コード
class Cat217CDiff(CatBaseCDiff):
	KEY = "cat_diff1"
	KEYS = "cats_diff1"
	KEY_XX="cat_diff1_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_diff1_3"
 
	def __init__(self):
		self.foo = 0 

	#217-着差コード
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCDiff.to_onehot(input, Cat217CDiff.KEY_LIST, Cat217CDiff.KEYS, Cat217CDiff.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#217-カテゴリ符号化
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
			key = Cat217CDiff.KEY_XX.format(i+1)
			Cat217CDiff.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCDiff.create_zeros(Cat217CDiff.KEY_LIST)
		temp[Cat217CDiff.DEFAULT_CAT]=1
		return pd.concat([output, temp])

if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat217CDiff.prepare(df_code)
	handle =codecs.open('Cat217CDiff.txt', 'w')
	inputs = ["","000","1","112","114","12","134","14","2","212","214","234","3","312","314","334","34","4","412","414","434","5","512","514","534","6","612","614","634","7","712","714","734","8","812","814","834","9","A","D","H","K","T","Z"]

	for input in inputs:
		index = Cat217CDiff.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseCDiff.CAT_LIST))

	for input in inputs:
		zeros = np.zeros(len(Cat217CDiff.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat217CDiff.KEY_LIST, dtype=int)

		df_input[Cat217CDiff.KEYS]=input
		ret = Cat217CDiff.to_onehot(df_input,output)
		print(df_input[Cat217CDiff.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

