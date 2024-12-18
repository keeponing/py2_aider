import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBVote import CatBaseBVote
import os
import inspect
#226-人気符号化
class Cat226BVote(CatBaseBVote):
	KEY = "cat_vote"
	KEYS = "cats_vote"
	KEY_XX="cat_vote_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_vote_10"
 
	def __init__(self):
		self.foo = 0

	#226-人気符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBVote.to_onehot(input, Cat226BVote.KEY_LIST, Cat226BVote.KEYS, Cat226BVote.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#226-人気符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseBVote.to_cats(int(input))#ビニングはIntに変換
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseBVote.prepare()
		Cat226BVote.KEY_LIST=[]
		max = len(CatBaseBVote.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat226BVote.KEY_XX.format(i+1)
			Cat226BVote.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseBVote.create_zeros(Cat226BVote.KEY_LIST)
		temp[Cat226BVote.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat226BVote.prepare()
	handle =codecs.open('Cat226BVote.txt', 'w')
	inputs = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']

	for input in inputs:
		index = Cat226BVote.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseBVote.BINS_LIST))

	for input in inputs:
		zeros = np.zeros(len(Cat226BVote.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat226BVote.KEY_LIST, dtype=int)

		df_input[Cat226BVote.KEYS]=input
		ret = Cat226BVote.to_onehot(df_input,output)
		print(df_input[Cat226BVote.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)

