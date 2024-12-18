import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect

#負担重量符号化
class CatBaseBJb(CatBase):
	BINS_LIST=[]
	def __init__(self):
		self.foo = 0 

	#負担重量符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#負担重量符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:		
			ret = util.create_num_bin_category_index(CatBaseBJb.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare():
		try:
			CatBaseBJb.BINS_LIST=[0,48,49,50,51,52,53,54,55,56,57,58,59,70]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	