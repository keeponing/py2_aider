import sys
sys.path.append(r"C:\Dev\py2")
import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import inspect

#平均距離符号化
class CatBaseBAd(CatBase):
	BINS_LIST=[]
	def __init__(self):
		self.foo = 0 

	#平均距離符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#平均距離符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:			
			ret = util.create_num_bin_category_index(CatBaseBAd.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		try:
			CatBaseBAd.BINS_LIST=[0,1000,1200,1400,1600,1800,2000,2200,2400,3000,3500,5000]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
