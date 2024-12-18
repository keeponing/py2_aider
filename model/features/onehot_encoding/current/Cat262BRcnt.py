import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBRcnt import CatBaseBRcnt
import os
import inspect
#262-出走数符号化
class Cat262BRcnt(CatBaseBRcnt):
	KEY = "cat_rcnt"
	KEYS = "cats_rcnt"
	KEY_XX="cat_rcnt_{0}"
	KEY_LIST = []

	DEFAULT_CAT = "cat_rcnt_3"
 
	def __init__(self):
		self.foo = 0 

	#262-出走数符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBRcnt.to_onehot(input, Cat262BRcnt.KEY_LIST, Cat262BRcnt.KEYS, Cat262BRcnt.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#262-出走数符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseBRcnt.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare():
		CatBaseBRcnt.prepare()
		Cat262BRcnt.KEY_LIST=[]
		max = len(CatBaseBRcnt.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat262BRcnt.KEY_XX.format(i+1)
			Cat262BRcnt.KEY_LIST.append(key)


	@staticmethod
	def create_zeros(output):
		temp = CatBaseBRcnt.create_zeros(Cat262BRcnt.KEY_LIST)
		# DEFAULT =0
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs

	Cat262BRcnt.prepare()
	handle =codecs.open('Cat262BRcnt.txt', 'w')
	inputs =[0,1,2,3,4,6,7,10,12,14,20,25,30,35,40]

	for input in inputs:
		index = Cat262BRcnt.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(Cat262BRcnt.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat262BRcnt.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat262BRcnt.KEY_LIST, dtype=int)

		df_input[Cat262BRcnt.KEYS]=input
		ret = Cat262BRcnt.to_onehot(df_input,output)
		print(df_input[Cat262BRcnt.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)


