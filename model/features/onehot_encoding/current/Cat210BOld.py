import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBOld import CatBaseBOld
import os
import inspect
#210-年齢符号化
class Cat210BOld(CatBaseBOld):
	KEY = "cat_old"
	KEYS = "cats_old"
	KEY_XX="cat_old_{0}"
	KEY_LIST = []

	DEFAULT_CAT = "cat_old_3"
 
	def __init__(self):
		self.foo = 0 

	#210-年齢符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBOld.to_onehot(input, Cat210BOld.KEY_LIST, Cat210BOld.KEYS, Cat210BOld.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#210-年齢符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseBOld.to_cats(int(input)) #ビニングはIntに変換
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseBOld.prepare()
		Cat210BOld.KEY_LIST=[]
		max = len(CatBaseBOld.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat210BOld.KEY_XX.format(i+1)
			Cat210BOld.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseBOld.create_zeros(Cat210BOld.KEY_LIST)
		temp[Cat210BOld.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat210BOld.prepare()
	handle =codecs.open('Cat210BOld.txt', 'w')
	temp_list = range(1,20)
	inputs=[]
	for i in temp_list:
		temp = f'{i:02}'
		inputs.append(temp)

	for input in inputs:
		index = Cat210BOld.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(Cat210BOld.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat210BOld.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat210BOld.KEY_LIST, dtype=int)

		df_input[Cat210BOld.KEYS]=input
		ret = Cat210BOld.to_onehot(df_input,output)
		print(df_input[Cat210BOld.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
