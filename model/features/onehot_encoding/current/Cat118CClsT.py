import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCCls import CatBaseCCls
import os
import inspect
#118-競走条件コード  2歳条件符号化～ 最若年条件　中最大条件
class Cat118CClsT(CatBaseCCls):
	KEYS_2 = "cats_cls2"
	KEYS_3 = "cats_cls3"
	KEYS_4 = "cats_cls4"
	KEYS_5 = "cats_cls5"
	KEYS_Y = "cats_clsy"
	KEYS = "cats_clst"
	KEY_XX="cat_clst_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_clst_1"
 
	def __init__(self):
		self.foo = 0 

	#118-競走条件コード最大値
	@staticmethod
	def to_onehot(input, output):
		try:
			arr_cls=[
				input[Cat118CClsT.KEYS_2],
				input[Cat118CClsT.KEYS_3],
				input[Cat118CClsT.KEYS_4],
				input[Cat118CClsT.KEYS_5],
				input[Cat118CClsT.KEYS_Y],
			]
			input2 ={}
			input2[Cat118CClsT.KEYS] = np.max(arr_cls)
			temp =  CatBaseCCls.to_onehot(input2, Cat118CClsT.KEY_LIST, Cat118CClsT.KEYS, Cat118CClsT.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#118-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			# Nothing to do...
			ret =0
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCCls.prepare(df_code)
		max = len(CatBaseCCls.CAT_LIST)-1
		for i in range(0,max):
			key = Cat118CClsT.KEY_XX.format(i+1)
			Cat118CClsT.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCCls.create_zeros(Cat118CClsT.KEY_LIST)
		temp[Cat118CClsT.DEFAULT_CAT]=1
		return pd.concat([output, temp])



if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE,
				dtype=str	
				)
	Cat118CClsT.prepare(df_code)
	handle =codecs.open('Cat118CClsT.txt', 'w')
	inputs = ["000","001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022","023","024","025","026","027","028","029","030","031","032","033","034","035","036","037","038","039","040","041","042","043","044","045","046","047","048","049","050","051","052","053","054","055","056","057","058","059","060","061","062","063","064","065","066","067","068","069","070","071","072","073","074","075","076","077","078","079","080","081","082","083","084","085","086","087","088","089","090","091","092","093","094","095","096","097","098","099","100","701","702","703","999",]
	for input in inputs:
		index = Cat118CClsT.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(Cat118CClsT.KEY_LIST)+1)

	for input in inputs:
		zeros = np.zeros(len(Cat118CClsT.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat118CClsT.KEY_LIST, dtype=int)

		df_input[Cat118CClsT.KEYS]=input
		ret = Cat118CClsT.to_onehot(df_input,output)
		print(df_input[Cat118CClsT.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
