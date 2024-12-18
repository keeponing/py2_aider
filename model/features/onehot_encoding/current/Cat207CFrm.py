import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCFrm import CatBaseCFrm
import os
import inspect
#207-枠符号化
class Cat207CFrm(CatBaseCFrm):
	KEY = "cat_frm"
	KEYS = "cats_frm"
	KEY_XX="cat_frm_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_frm_4"
 
	def __init__(self):
		self.foo = 0 

	#207-枠符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCFrm.to_onehot(input, Cat207CFrm.KEY_LIST, Cat207CFrm.KEYS, Cat207CFrm.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
   
	#207-枠符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCFrm.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseCFrm.prepare()
		Cat207CFrm.KEY_LIST=[]
		max = len(CatBaseCFrm.CAT_LIST)-1 
		for i in range(0,max):
			key = Cat207CFrm.KEY_XX.format(i+1)
			Cat207CFrm.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCFrm.create_zeros(Cat207CFrm.KEY_LIST)
		temp[Cat207CFrm.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat207CFrm.prepare()
	handle =codecs.open('Cat207CFrm.txt', 'w')
	inputs = range(1,9)

	for input in inputs:
		index = Cat207CFrm.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat207CFrm.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat207CFrm.KEY_LIST, dtype=int)

		df_input[Cat207CFrm.KEYS]=input
		ret = Cat207CFrm.to_onehot(df_input,output)
		print(df_input[Cat207CFrm.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

