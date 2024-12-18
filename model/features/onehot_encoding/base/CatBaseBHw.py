import sys
sys.path.append(r"C:\Dev\py2")

import model.utility.k_jra_util as util
from .CatBase import CatBase
import os
import  inspect
#馬体重符号化
class CatBaseBHw(CatBase):
	BINS_LIST=[]
	def __init__(self):
		self.foo = 0 

	#馬体重符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#馬体重符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			#bins=[0,400,420,440,460,480,500,550,600,650,700]
			ret = util.create_num_bin_category_index(CatBaseBHw.BINS_LIST, input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare():
		try:
			CatBaseBHw.BINS_LIST=[0,400,420,440,460,480,500,550,600,650,700]
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	