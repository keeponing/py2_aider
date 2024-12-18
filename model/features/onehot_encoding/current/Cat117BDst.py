import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.onehot_encoding.base.CatBaseBDst import CatBaseBDst
import os
import inspect
#117-出走距離符号化
class Cat117BDst(CatBaseBDst):
	KEY = "cat_dst"
	KEYS = "cats_dst"
	KEY_XX="cat_dst_{0}"
	KEY_LIST = []
	DEFAULT_CAT = "cat_dst_6"
 
	def __init__(self):
		self.foo = 0 

	#117-出走距離符号化
	@staticmethod
	def to_onehot(input, output):
		try:
			temp =  CatBaseBDst.to_onehot(input, Cat117BDst.KEY_LIST, Cat117BDst.KEYS, Cat117BDst.KEY_XX)
			return pd.concat([output, temp])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#117-出走距離符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseBDst.to_cats(int(input)) #ビニングはIntに変換
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		CatBaseBDst.prepare()
		Cat117BDst.KEY_LIST=[]
		max = len(CatBaseBDst.BINS_LIST)-2 # ビニングの場合は-2
		for i in range(0,max):
			key = Cat117BDst.KEY_XX.format(i+1)
			Cat117BDst.KEY_LIST.append(key)

	@staticmethod
	def create_zeros(output):
		temp = CatBaseBDst.create_zeros(Cat117BDst.KEY_LIST)
		temp[Cat117BDst.DEFAULT_CAT]=1
		return pd.concat([output, temp])


if __name__ == '__main__':
	import model.conf.KJraConfig as conf
	import model.conf.KJraConst as const
	import codecs
	
	Cat117BDst.prepare()
	handle =codecs.open('Cat117BDst.txt', 'w')
	inputs = ["0","760","800","820","850","900","950","1000","1010","1100","1130","1150","1175","1180","1190","1200","1225","1230","1250","1300","1330","1350","1390","1400","1410","1430","1445","1490","1500","1550","1590","1600","1620","1640","1650","1660","1670","1690","1700","1750","1760","1777","1790","1800","1856","1870","1900","1950","1980","1990","2000","2018","2020","2025","2040","2050","2080","2100","2150","2200","2226","2250","2300","2350","2380","2390","2400","2410","2418","2425","2435","2450","2485","2490","2500","2600","2700","2750","2770","2800","2850","2860","2880","2890","2900","2910","2920","2930","2950","2970","3000","3100","3110","3140","3170","3180","3190","3200","3210","3250","3280","3284","3285","3290","3300","3330","3350","3370","3380","3390","3400","3430","3500","3570","3600","3700","3717","3760","3790","3800","3900","3930","4000","4100","4200","4250","4260","4300","4400","4530","4700","9999"]

	for input in inputs:
		index = Cat117BDst.to_cats(input)
		print(input,'\tindex=', index, file=handle)

	inputs = range(0,len(CatBaseBDst.BINS_LIST)-1)

	for input in inputs:
		zeros = np.zeros(len(Cat117BDst.KEY_LIST))
		output = pd.Series(dtype=float)
		df_input = pd.Series(data= zeros, index=Cat117BDst.KEY_LIST, dtype=int)

		df_input[Cat117BDst.KEYS]=input
		ret = Cat117BDst.to_onehot(df_input,output)
		print(df_input[Cat117BDst.KEYS],' to_onehot=>', file=handle)
		print(ret, file=handle)
