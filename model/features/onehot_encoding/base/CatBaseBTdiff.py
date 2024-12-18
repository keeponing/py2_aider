import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect
#タイム差符号化
class CatBaseBTdiff(CatBase):
	BINS_LIST = []
	def __init__(self):
		self.foo = 0 
	
	#タイム差符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	
	#タイム差符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = util.create_num_bin_category_index(CatBaseBTdiff.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare():
		try:
			# 01ms 30秒=300, 1秒=10, 0.1秒=1
			CatBaseBTdiff.BINS_LIST=[ -1000, -40, -20, 0, 20, 40, 60, 80, 100, 200, 400,600, 10000 ]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	