import sys
sys.path.append(r"C:\Dev\py2")
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCCls import CatBaseCCls
import os
import inspect
#112-競走条件コード 4歳条件符号化
class Cat112CCls4(CatBaseCCls):
	KEY = "cat_cls4"
	KEYS = "cats_cls4"
	KEY_XX="cat_cls4_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_cls4_1"
 
	def __init__(self):
		self.foo = 0 

	#112-競走条件コード 4歳条件符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCCls.to_onehot(input, Cat112CCls4.KEY_LIST, Cat112CCls4.KEYS, Cat112CCls4.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#112-カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCCls.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare(df_code):
		CatBaseCCls.prepare(df_code)
		max = len(CatBaseCCls.CAT_LIST)-1
		for i in range(0,max):
			key = Cat112CCls4.KEY_XX.format(i+1)
			Cat112CCls4.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseCCls.create_zeros(Cat112CCls4.KEY_LIST)
		temp[Cat112CCls4.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE ,
				dtype=str	
				)
	Cat112CCls4.prepare(df_code)
	handle =codecs.open('Cat112CCls4.txt', 'w')
	inputs = ["000","001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022","023","024","025","026","027","028","029","030","031","032","033","034","035","036","037","038","039","040","041","042","043","044","045","046","047","048","049","050","051","052","053","054","055","056","057","058","059","060","061","062","063","064","065","066","067","068","069","070","071","072","073","074","075","076","077","078","079","080","081","082","083","084","085","086","087","088","089","090","091","092","093","094","095","096","097","098","099","100","701","702","703","999",]
	for input in inputs:
		index = Cat112CCls4.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(Cat112CCls4.KEY_LIST)+1)

	for input in inputs:
		zeros = np.zeros(len(Cat112CCls4.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat112CCls4.KEY_LIST, dtype=int)

		df_input[Cat112CCls4.KEYS]=input
		ret = Cat112CCls4.to_onehot(df_input,output)
		print(df_input[Cat112CCls4.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
