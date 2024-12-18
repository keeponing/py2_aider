import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBHcnt import CatBaseBHcnt
import os
import inspect
#119-出走頭数符号化
class Cat119BHcnt(CatBaseBHcnt):
	KEY = "cat_hcnt"
	KEYS = "cats_hcnt"
	KEY_XX="cat_hcnt_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_hcnt_10"
	def __init__(self):
		self.foo = 0 

	#119-出走頭数符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBHcnt.to_onehot(input, Cat119BHcnt.KEY_LIST, Cat119BHcnt.KEYS, Cat119BHcnt.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#119-出走頭数符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseBHcnt.to_cats(int(input))#ビニングはIntに変換
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseBHcnt.prepare()
		Cat119BHcnt.KEY_LIST=[]
		max = len(CatBaseBHcnt.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat119BHcnt.KEY_XX.format(i+1)
			Cat119BHcnt.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseBHcnt.create_zeros(Cat119BHcnt.KEY_LIST)
		temp[Cat119BHcnt.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat119BHcnt.prepare()
	handle =codecs.open('Cat119BHcnt.txt', 'w')
	inputs = ["00","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","26","29",]

	for input in inputs:
		index = Cat119BHcnt.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseBHcnt.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat119BHcnt.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat119BHcnt.KEY_LIST, dtype=int)

		df_input[Cat119BHcnt.KEYS]=input
		ret = Cat119BHcnt.to_onehot(df_input,output)
		print(df_input[Cat119BHcnt.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
