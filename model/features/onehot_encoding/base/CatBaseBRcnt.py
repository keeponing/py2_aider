import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect
#出走数符号化
class CatBaseBRcnt(CatBase):
	BINS_LIST=[0,1,2,3,4,6,7,10,12,14,20,25,30,35,40]
	def __init__(self):
		self.foo = 0 

	#出走数符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#20-出走数符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:		
			ret = util.create_num_bin_category_index(CatBaseBRcnt.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		try:
			CatBaseBRcnt.BINS_LIST=[0,1,2,3,4,6,7,10,12,14,20,25,30,35,40]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	