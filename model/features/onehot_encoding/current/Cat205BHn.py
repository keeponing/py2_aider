import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBHn import CatBaseBHn
import os
import inspect
#205-馬番符号化
class Cat205BHn(CatBaseBHn):
	KEY = "cat_hn"
	KEYS = "cats_hn"
	KEY_XX="cat_hn_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_hn_4"
 
	def __init__(self):
		self.foo = 0 

	#205-馬番符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBHn.to_onehot(input, Cat205BHn.KEY_LIST, Cat205BHn.KEYS, Cat205BHn.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
   
	#205-馬番符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseBHn.to_cats(int(input)) #ビニングはIntに変換
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseBHn.prepare()
		Cat205BHn.KEY_LIST=[]
		max = len(CatBaseBHn.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat205BHn.KEY_XX.format(i+1)
			Cat205BHn.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseBHn.create_zeros(Cat205BHn.KEY_LIST)
		temp[Cat205BHn.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat205BHn.prepare()
	handle =codecs.open('Cat205BHn.txt', 'w')
	temp_list = range(0,31)
	inputs=[]
	for i in temp_list:
		temp = f'{i:02}'
		inputs.append(temp)

	for input in inputs:
		index = Cat205BHn.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseBHn.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat205BHn.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat205BHn.KEY_LIST, dtype=int)

		df_input[Cat205BHn.KEYS]=input
		ret = Cat205BHn.to_onehot(df_input,output)
		print(df_input[Cat205BHn.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

