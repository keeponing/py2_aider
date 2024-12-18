import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBGal import CatBaseBGal
import os
import inspect
#223-馬体重増減符号化
class Cat223BGal(CatBaseBGal):
	KEY = "cat_gal"
	KEYS = "cats_gal"
	KEY_XX="cat_gal_{0}"
	KEY_LIST = []

	DEFAULT_CAT = "cat_gal_7"
 
	def __init__(self):
		self.foo = 0 

	#223-馬場状態符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBGal.to_onehot(input, Cat223BGal.KEY_LIST, Cat223BGal.KEYS, Cat223BGal.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#223-馬体重増減符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseBGal.to_cats(int(input)) #ビニングはIntに変換
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseBGal.prepare()
		Cat223BGal.KEY_LIST=[]
		max = len(CatBaseBGal.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat223BGal.KEY_XX.format(i+1)
			Cat223BGal.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseBGal.create_zeros(Cat223BGal.KEY_LIST)
		temp[Cat223BGal.DEFAULT_CAT] =1
		return pd.concat([output, temp])

		
if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat223BGal.prepare()
	handle =codecs.open('Cat223BGal.txt', 'w')
	inputs =  ['0', '5', '10', '15', '20', '25', '30', '40', '100']

	for input in inputs:
		index = Cat223BGal.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseBGal.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat223BGal.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat223BGal.KEY_LIST, dtype=int)

		df_input[Cat223BGal.KEYS]=input
		ret = Cat223BGal.to_onehot(df_input,output)
		print(df_input[Cat223BGal.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
