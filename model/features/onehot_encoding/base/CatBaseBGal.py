import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect
#馬体重増減符号化
class CatBaseBGal(CatBase):
	BINS_LIST =[]
	def __init__(self):
		self.foo = 0 

	#馬体重増減符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	  

	#馬体重増減符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:		
			ret = util.create_num_bin_category_index(CatBaseBGal.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
		return ret
		
	@staticmethod
	def prepare():
		try:
			#CatBaseBGal.BINS_LIST=[-100, -40, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 40, 100]
			CatBaseBGal.BINS_LIST=[0, 5, 10, 15, 20, 25, 30, 40, 100]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	