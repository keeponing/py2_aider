import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCJmrk import CatBaseCJmrk
import os
import inspect
#215-騎手見習コード
class Cat215CJmrk(CatBaseCJmrk):
	KEY = "cat_jmk"
	KEYS = "cats_jmk"
	KEY_XX="cat_jmk_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_jmk_3"
 
	def __init__(self):
		self.foo = 0 

	#215-騎手見習コード
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCJmrk.to_onehot(input, Cat215CJmrk.KEY_LIST, Cat215CJmrk.KEYS, Cat215CJmrk.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#115-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCJmrk.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCJmrk.prepare(df_code)
		max = len(CatBaseCJmrk.CAT_LIST)-1
		for i in range(0,max):
			key = Cat215CJmrk.KEY_XX.format(i+1)
			Cat215CJmrk.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCJmrk.create_zeros(Cat215CJmrk.KEY_LIST)
		temp[Cat215CJmrk.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE,
				dtype=str	
				)
	Cat215CJmrk.prepare(df_code)
	handle =codecs.open('Cat215CJmrk.txt', 'w')
	inputs = ['0','1','2','3','4','9']

	for input in inputs:
		index = Cat215CJmrk.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat215CJmrk.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat215CJmrk.KEY_LIST, dtype=int)

		df_input[Cat215CJmrk.KEYS]=input
		ret = Cat215CJmrk.to_onehot(df_input,output)
		print(df_input[Cat215CJmrk.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

