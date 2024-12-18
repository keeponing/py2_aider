import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
import datetime
from model.features.onehot_encoding.base.CatBaseVYD import CatBaseVYD
import os
import inspect
#267-経過年符号化
class Cat267VYD(CatBaseVYD):
	KEY = "cat_yd"
	KEYS = "cats_yd"
	KEY_XX="cat_yd_{0}"
	KEY_LIST = []

	def __init__(self):
		self.foo = 0 

	@staticmethod
	def to_onehot(input, output):
		try:
			temp = CatBaseVYD.to_onehot(input, Cat267VYD.KEY_LIST, Cat267VYD.KEYS, Cat267VYD.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#267-経過年符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseVYD.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	#002-開催年リスト作成
	@staticmethod
	def prepare():
		CatBaseVYD.prepare()
		Cat267VYD.KEY_LIST=[]
		max = len(CatBaseVYD.CAT_LIST)-1
		for i in range(0,max):
			key = Cat267VYD.KEY_XX.format(i+1)
			Cat267VYD.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseVYD.create_zeros(Cat267VYD.KEY_LIST)
		#DEFAULT=0
		return pd.concat([output, temp])

if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	today = datetime.date.today()
	year = today.year
	from_year =2000
	to_year =year+1
	Cat267VYD.prepare()
	handle =codecs.open('Cat267VYD.txt', 'w')
	inputs = range(from_year, to_year)
	for input in inputs:
		index = Cat267VYD.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat267VYD.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat267VYD.KEY_LIST, dtype=int)
		df_input[Cat267VYD.KEYS]=input
		ret = Cat267VYD.to_onehot(df_input,output)
		print(df_input[Cat267VYD.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
