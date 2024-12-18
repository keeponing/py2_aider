import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect
#前走との距離符号化
class CatBaseBDd(CatBase):
	BINS_LIST=[]
	def __init__(self):
		self.foo = 0 

	#前走との距離符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#前走との距離符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			ret = util.create_num_bin_category_index(CatBaseBDd.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare():
		try:
			CatBaseBDd.BINS_LIST=[-3000,-800,-600,-400,-200,0,200,400,600,800,3000]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	