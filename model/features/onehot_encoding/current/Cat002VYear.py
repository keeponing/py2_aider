import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
import datetime
from model.features.onehot_encoding.base.CatBaseVYear import CatBaseVYear
import os
import inspect
#002-開催年符号化
class Cat002VYear(CatBaseVYear):
	KEY = "cat_year"
	KEYS = "cats_year"
	KEY_XX="cat_year_{0}"
	KEY_LIST = []

	def __init__(self):
		self.foo = 0 

	@staticmethod
	def to_onehot(input, output):
		try:
			temp = CatBaseVYear.to_onehot(input, Cat002VYear.KEY_LIST, Cat002VYear.KEYS, Cat002VYear.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#002-開催年符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseVYear.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	#002-開催年リスト作成
	@staticmethod
	def prepare():
		CatBaseVYear.prepare()
		Cat002VYear.KEY_LIST=[]
		# for i, _ in enumerate(Cat002VYear.CAT_LIST):
		# 	key = Cat002VYear.KEY_XX.format(i+1)
		# 	Cat002VYear.KEY_LIST.append(key)
		max = len(CatBaseVYear.CAT_LIST)-1
		for i in range(0,max):
			key = Cat002VYear.KEY_XX.format(i+1)
			Cat002VYear.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseVYear.create_zeros(Cat002VYear.KEY_LIST)
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
	Cat002VYear.prepare()
	handle =codecs.open('Cat002VYear.txt', 'w')
	inputs = range(from_year, to_year)
	for input in inputs:
		index = Cat002VYear.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat002VYear.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat002VYear.KEY_LIST, dtype=int)
		df_input[Cat002VYear.KEYS]=input
		ret = Cat002VYear.to_onehot(df_input,output)
		print(df_input[Cat002VYear.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
