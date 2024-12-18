import sys
sys.path.append(r"C:\Dev\py2")

import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCBlink import CatBaseCBlink
import os
import inspect
#209-ブリンカー符号化
class Cat209CBlink(CatBaseCBlink):
	KEY = "cat_blink"
	KEYS = "cats_blink"
	KEY_XX="cat_blink_{0}"
	KEY_LIST = []


	def __init__(self):
		self.foo = 0 

	#209-ブリンカー符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCBlink.to_onehot(input, Cat209CBlink.KEY_LIST, Cat209CBlink.KEYS, Cat209CBlink.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	 
	#209-ブリンカー符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCBlink.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		Cat209CBlink.KEY_LIST=[]
		for i in range(0,1):
			key = Cat209CBlink.KEY_XX.format(i+1)
			Cat209CBlink.KEY_LIST.append(key)


	@staticmethod
	def create_zeros(output):
		temp = CatBaseCBlink.create_zeros(Cat209CBlink.KEY_LIST)
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat209CBlink.prepare()
	handle =codecs.open('Cat209CBlink.txt', 'w')
	inputs = ['0','1']

	for input in inputs:
		index = Cat209CBlink.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat209CBlink.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat209CBlink.KEY_LIST, dtype=int)

		df_input[Cat209CBlink.KEYS]=input
		ret = Cat209CBlink.to_onehot(df_input,output)
		print(df_input[Cat209CBlink.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

