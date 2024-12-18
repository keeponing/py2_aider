import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBRnk import CatBaseBRnk
import os
import inspect
#206-着順符号化
class Cat206BRnk(CatBaseBRnk):
	KEY = "cat_rnk"
	KEYS = "cats_rnk"
	KEY_XX="cat_rnk_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_rnk_17"
	def __init__(self):
		self.foo = 0 

	#206-着順符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBRnk.to_onehot(input, Cat206BRnk.KEY_LIST, Cat206BRnk.KEYS, Cat206BRnk.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
 
	#206-着順符号化
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
		Cat206BRnk.KEY_LIST=[]
		max = len(CatBaseBRnk.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat206BRnk.KEY_XX.format(i+1)
			Cat206BRnk.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseBRnk.create_zeros(Cat206BRnk.KEY_LIST)
		temp[Cat206BRnk.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat206BRnk.prepare()
	handle =codecs.open('Cat206BRnk.txt', 'w')
	temp_list = range(0,31)
	inputs=[]
	for i in temp_list:
		temp = f'{i:02}'
		inputs.append(temp)

	for input in inputs:
		index = Cat206BRnk.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseBRnk.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat206BRnk.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat206BRnk.KEY_LIST, dtype=int)

		df_input[Cat206BRnk.KEYS]=input
		ret = Cat206BRnk.to_onehot(df_input,output)
		print(df_input[Cat206BRnk.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
