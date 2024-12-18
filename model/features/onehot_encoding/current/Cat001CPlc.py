import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseCPlc import CatBaseCPlc
import os
import inspect
#24-開催場符号化
class Cat001CPlc(CatBaseCPlc):
	KEY = "cat_plc"
	KEYS = "cats_plc"
	KEY_XX="cat_plc_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_plc_1"

	def __init__(self):
		self.foo = 0 

	#001-開催場符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseCPlc.to_onehot(input, Cat001CPlc.KEY_LIST, Cat001CPlc.KEYS, Cat001CPlc.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#001-開催場符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = CatBaseCPlc.to_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		CatBaseCPlc.prepare(df_code)
		max = len(CatBaseCPlc.CAT_LIST)-1
		for i in range(0,max):
			key = Cat001CPlc.KEY_XX.format(i+1)
			Cat001CPlc.KEY_LIST.append(key)
		
	@staticmethod
	def create_zeros(output):
		temp = CatBaseCPlc.create_zeros(Cat001CPlc.KEY_LIST)
		temp[Cat001CPlc.DEFAULT_CAT]=1
		return pd.concat([output, temp])



if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import codecs
	
	df_code = pd.read_csv(conf.JRA_VAN_CODE_TABLE,
				dtype=str	
				)
	Cat001CPlc.prepare(df_code)
	handle =codecs.open('Cat001CPlc.txt', 'w')
	inputs = ['00','01','02','03','04','05','06','07','08','09','10','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','A0','A2','A4','A6','A8','B0','B2','B4','B6','B8','C0','C2','C4','C5','C6','C7','C8','D0','D2','D4','D6','D8','E0','E2','E4','E6','E8','F0','F1','F2','F4','F6','F8','G0','G2','G4','G6','G8','H0','H2','H4','H6','H8','I0','I2','I4','I6','I8','J0','J2','J4','J6','J8','K0','K2','K4','K6','K8','L0','L2','L4','L6','L8','M0','M2','M4','M6','M8',]
	for input in inputs:
		index = Cat001CPlc.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(Cat001CPlc.KEY_LIST)+1)

	for input in inputs:
		zeros = np.zeros(len(Cat001CPlc.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat001CPlc.KEY_LIST, dtype=int)
		df_input[Cat001CPlc.KEYS]=input
		ret = Cat001CPlc.to_onehot(df_input,output)
		print(df_input[Cat001CPlc.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
