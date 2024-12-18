import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect
#オッズ符号化
class CatBaseBOdds(CatBase):
	BINS_LIST = []
	def __init__(self):
		self.foo = 0 
	
	#オッズ符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	   
	
	#オッズ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			temp = float(input/10.0)
			if(temp == 0.0):
				temp = 999
			ret = util.create_float_bin_category_index(CatBaseBOdds.BINS_LIST, temp)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare():
		try:
			CatBaseBOdds.BINS_LIST=[0,1,2,3,4,5,6,7,8,9,10,15,20,30,40,50,1000]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		