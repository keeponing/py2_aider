import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect

#出走距離符号化
class CatBaseBDst(CatBase):
	BINS_LIST=[]
	def __init__(self):
		self.foo = 0 

	#出走距離符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#出走距離符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = util.create_num_bin_category_index(CatBaseBDst.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		try:
			CatBaseBDst.BINS_LIST=[
				0,
				1000,
				1150,
				1200,
				1300,
				1400,
				1500,
				1600,
				1700,
				1800,
				1900,
				2000,
				2100,
				2200,
				2300,
				2400,
				2500,
				2600,
				2700,
				2800,
				2900,
				3000,
				3100,
				3200,
				3300,
				3400,
				3500,
				3600,
				9999
				]

			# CatBaseBDst.BINS_LIST=[
			# 0,
			# 760,
			# 800,
			# 820,
			# 850,
			# 900,
			# 950,
			# 1000,
			# 1010,
			# 1100,
			# 1130,
			# 1150,
			# 1175,
			# 1180,
			# 1190,
			# 1200,
			# 1225,
			# 1230,
			# 1250,
			# 1300,
			# 1330,
			# 1350,
			# 1390,
			# 1400,
			# 1410,
			# 1430,
			# 1445,
			# 1490,
			# 1500,
			# 1550,
			# 1590,
			# 1600,
			# 1620,
			# 1640,
			# 1650,
			# 1660,
			# 1670,
			# 1690,
			# 1700,
			# 1750,
			# 1760,
			# 1777,
			# 1790,
			# 1800,
			# 1856,
			# 1870,
			# 1900,
			# 1950,
			# 1980,
			# 1990,
			# 2000,
			# 2018,
			# 2020,
			# 2025,
			# 2040,
			# 2050,
			# 2080,
			# 2100,
			# 2150,
			# 2200,
			# 2226,
			# 2250,
			# 2300,
			# 2350,
			# 2380,
			# 2390,
			# 2400,
			# 2410,
			# 2418,
			# 2425,
			# 2435,
			# 2450,
			# 2485,
			# 2490,
			# 2500,
			# 2600,
			# 2700,
			# 2750,
			# 2770,
			# 2800,
			# 2850,
			# 2860,
			# 2880,
			# 2890,
			# 2900,
			# 2910,
			# 2920,
			# 2930,
			# 2950,
			# 2970,
			# 3000,
			# 3100,
			# 3110,
			# 3140,
			# 3170,
			# 3180,
			# 3190,
			# 3200,
			# 3210,
			# 3250,
			# 3280,
			# 3284,
			# 3285,
			# 3290,
			# 3300,
			# 3330,
			# 3350,
			# 3370,
			# 3380,
			# 3390,
			# 3400,
			# 3430,
			# 3500,
			# 3570,
			# 3600,
			# 3700,
			# 3717,
			# 3760,
			# 3790,
			# 3800,
			# 3900,
			# 3930,
			# 4000,
			# 4100,
			# 4200,
			# 4250,
			# 4260,
			# 4300,
			# 4400,
			# 4530,
			# 4700,
			# 9999
			# ]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	