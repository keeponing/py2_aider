import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd

from model.features.onehot_encoding.base.CatBaseBRnk import CatBaseBRnk
import os
import inspect
#230-第四コーナー符号化
class Cat230BCnr(CatBaseBRnk):
	KEY = "cat_cnr4"
	KEYS = "cats_cnr4"
	KEY_XX="cat_cnr4_{0}"
	KEY_LIST = []

	DEFAULT_CAT = "cat_cnr4_17"
	def __init__(self):
		self.foo = 0 

	#230-第四コーナー符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBRnk.to_onehot(input, Cat230BCnr.KEY_LIST, Cat230BCnr.KEYS, Cat230BCnr.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
 
	#230-第四コーナー符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseBRnk.to_cats(int(input)) #ビニングはIntに変換
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseBRnk.prepare()
		Cat230BCnr.KEY_LIST=[]
		max = len(CatBaseBRnk.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat230BCnr.KEY_XX.format(i+1)
			Cat230BCnr.KEY_LIST.append(key)


	@staticmethod
	def create_zeros(output):
		temp = CatBaseBRnk.create_zeros(Cat230BCnr.KEY_LIST)
		temp[Cat230BCnr.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat230BCnr.prepare()
	handle =codecs.open('Cat230BCnr.txt', 'w')
	temp_list = range(1,31)
	inputs=[]
	for i in temp_list:
		temp = f'{i:02}'
		inputs.append(temp)

	for input in inputs:
		index = Cat230BCnr.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseBRnk.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat230BCnr.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat230BCnr.KEY_LIST, dtype=int)

		df_input[Cat230BCnr.KEYS]=input
		ret = Cat230BCnr.to_onehot(df_input,output)
		print(df_input[Cat230BCnr.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

