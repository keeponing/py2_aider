import sys
sys.path.append(r"C:\Dev\py2")

import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCPm import CatBaseCPm
import os
import inspect
#222-+-符号化
class Cat222CPm(CatBaseCPm):
	KEY = "cat_pm"	
	KEYS = "cats_pm"
	KEY_XX="cat_pm_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_pm_1"
 
	def __init__(self):
		self.foo = 0 

	#222-+-符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp = CatBaseCPm.to_onehot(input, Cat222CPm.KEY_LIST, Cat222CPm.KEYS, Cat222CPm.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#222-+-符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCPm.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseCPm.prepare()
		Cat222CPm.KEY_LIST=[]
		max = len(CatBaseCPm.CAT_LIST)-1
		for i in range(0,max):
			key = Cat222CPm.KEY_XX.format(i+1)
			Cat222CPm.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		#default 
		temp = CatBaseCPm.create_zeros(Cat222CPm.KEY_LIST)
		temp[Cat222CPm.DEFAULT_CAT] =1 
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat222CPm.prepare()
	handle =codecs.open('Cat222CPm.txt', 'w')
	inputs = ['','+','-']

	for input in inputs:
		index = Cat222CPm.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat222CPm.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat222CPm.KEY_LIST, dtype=int)

		df_input[Cat222CPm.KEYS]=input
		ret = Cat222CPm.to_onehot(df_input,output)
		print(df_input[Cat222CPm.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

