import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseVMnt2 import CatBaseVMnt2
import os
import inspect
#003-開催月符号化
class Cat003VMnt2(CatBaseVMnt2):
	KEY = "cat_mnt"
	KEYS = "cats_mnt"
	KEY_LIST = ["cat_mnt_cos","cat_mnt_sin"]
	def __init__(self):
		self.foo = 0 

	#003-開催月符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseVMnt2.to_onehot(input, Cat003VMnt2.KEY_LIST,Cat003VMnt2.KEYS)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#003-開催月符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseVMnt2.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseVMnt2.prepare()

	@staticmethod
	def create_zeros(output):
		temp = CatBaseVMnt2.create_zeros(Cat003VMnt2.KEY_LIST)
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	import datetime
	today = datetime.date.today()
	Cat003VMnt2.prepare()
	handle =codecs.open('Cat003VMnt2.txt', 'w')
	month = range(1, 13)
	inputs =[]
	for m in month:
		temp = f'{m:02}'
		inputs.append(temp+'AA')
	for input in inputs:
		index = Cat003VMnt2.to_cats(input[:2])
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat003VMnt2.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat003VMnt2.KEY_LIST, dtype=int)
		df_input[Cat003VMnt2.KEYS]=input
		ret = Cat003VMnt2.to_onehot(df_input,output)
		print(df_input[Cat003VMnt2.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
