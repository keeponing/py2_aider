import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect
#年齢符号化
class CatBaseBOld(CatBase):
	BINS_LIST = []
	def __init__(self):
		self.foo = 0 

	#年齢符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#年齢符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:		
			ret = util.create_num_bin_category_index(CatBaseBOld.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		try:
			CatBaseBOld.BINS_LIST=[1,2,3,4,5,6,7,8,9,10,20]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	