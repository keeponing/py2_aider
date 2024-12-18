import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCRule import CatBaseCRule
import os
import inspect
#115-競走記号コード
class Cat115CRule(CatBaseCRule):
	KEY = "cat_rule"
	KEYS = "cats_rule"
	KEY_XX="cat_rule_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_rule_3"
 
	def __init__(self):
		self.foo = 0 

	#115-競走記号コード
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCRule.to_onehot(input, Cat115CRule.KEY_LIST, Cat115CRule.KEYS, Cat115CRule.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#115-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCRule.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCRule.prepare(df_code)
		max = len(CatBaseCRule.CAT_LIST)-1
		for i in range(0,max):
			key = Cat115CRule.KEY_XX.format(i+1)
			Cat115CRule.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCRule.create_zeros(Cat115CRule.KEY_LIST)
		temp[Cat115CRule.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat115CRule.prepare(df_code)
	handle =codecs.open('Cat115CRule.txt', 'w')
	inputs = ["000","001","002","003","004","020","021","023","024","030","031","033","034","040","041","043","044","A00","A01","A02","A03","A04","A10","A11","A13","A14","A20","A21","A23","A24","A30","A31","A33","A34","A40","A41","B00","B01","B03","B04","C00","C01","C03","C04","D00","D01","D03","E00","E01","E03","F00","F01","F03","F04","G00","G01","G03","H00","H01","I00","I01","I03","J00","J01","K00","K01","K03","L00","L01","L03","M00","M01","M03","M04","N00","N01","N03","N04","N20","N21","N23","N24","N30","N31","N40","N41","N44",]
	for input in inputs:
		index = Cat115CRule.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(inputs))

	for input in inputs:
		zeros = np.zeros(len(Cat115CRule.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat115CRule.KEY_LIST, dtype=int)

		df_input[Cat115CRule.KEYS]=input
		ret = Cat115CRule.to_onehot(df_input,output)
		print(df_input[Cat115CRule.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
