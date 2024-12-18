import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBase import CatBase
import os
import inspect
#105-トラック・コース周り符号化
class Cat105CTrk2(CatBase):
	KEY = "cat_trk2"
	KEYS = "cats_trk2"
	KEY_XX="cat_trk2_{0}"
	KEY_LIST = []

	def __init__(self):
		self.foo = 0 

	#105-トラック・コース周り符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  Cat105CTrk2.convert_onehot(input)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#105-コース周り符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = Cat105CTrk2.convert_cats(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 


	@staticmethod
	def prepare():
    
		Cat105CTrk2.KEY_LIST = [Cat105CTrk2.KEY_XX.format(i) for i in range(6)]
		

	@staticmethod
	def create_zeros(output):
		temp = CatBase.create_zeros(Cat105CTrk2.KEY_LIST)
		#DEFAULT=0
		return pd.concat([output, temp])

	@staticmethod
	def convert_cats(input):
		ret =0 
		if('00'==input):ret =0#未設定
		elif('10'==input):ret=1#芝・直
		elif('11'==input):ret=2#芝・左
		elif('12'==input):ret=2#芝・左
		elif('13'==input):ret=2#芝・左
		elif('14'==input):ret=2#芝・左
		elif('15'==input):ret=2#芝・左
		elif('16'==input):ret=2#芝・左
		elif('17'==input):ret=3#芝・右
		elif('18'==input):ret=3#芝・右
		elif('19'==input):ret=3#芝・右
		elif('20'==input):ret=3#芝・右
		elif('21'==input):ret=3#芝・右
		elif('22'==input):ret=3#芝・右
		elif('23'==input):ret=4#ダート・左
		elif('24'==input):ret=5#ダート・右
		elif('25'==input):ret=4#ダート・左
		elif('26'==input):ret=5#ダート・右
		elif('27'==input):ret=4#ダート・左
		elif('28'==input):ret=5#ダート・右
		elif('29'==input):ret=4#ダート・直
		elif('51'==input):ret=6#障害
		elif('52'==input):ret=6#障害
		elif('53'==input):ret=6#障害
		elif('54'==input):ret=6#障害
		elif('55'==input):ret=6#障害
		elif('56'==input):ret=6#障害
		elif('57'==input):ret=6#障害
		elif('58'==input):ret=6#障害
		elif('59'==input):ret=6#障害
		return ret
	@staticmethod
	def convert_onehot(input):
		value = input[Cat105CTrk2.KEYS]
		temp =[0,0,0,0,0,0] #未設定
		if(1==value):   temp=[1,0,0,0,0,0]#芝・直
		elif(2==value): temp=[0,1,0,0,0,0]#芝・左
		elif(3==value): temp=[0,0,1,0,0,0]#芝・右
		elif(4==value): temp=[0,0,0,1,0,0]#ダート・左
		elif(5==value): temp=[0,0,0,0,1,0]#ダート・右
		elif(6==value): temp=[0,0,0,0,0,1]#障害
		ret = pd.Series(data= temp, index=Cat105CTrk2.KEY_LIST, dtype=int)
		return ret		
if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat105CTrk2.prepare()
	handle =codecs.open('Cat105CTrk2.txt', 'w')
	inputs = ["00","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","51","52","53","54","55","56","57","58","59",]
	for input in inputs:
		index = Cat105CTrk2.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(7)

	for input in inputs:
		zeros = np.zeros(len(Cat105CTrk2.KEY_LIST))
		output = pd.Series(dtype=float, index= [Cat105CTrk2.KEYS])
	
		output[Cat105CTrk2.KEYS]=input
		ret = Cat105CTrk2.to_onehot(output,output)
		print(output[Cat105CTrk2.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
