import sys
import datetime

sys.path.append(r"C:\Dev\py2")
import os
import inspect
from .CatBase import CatBase
#54-経過年符号化
class CatBaseVYD(CatBase):
	CAT_LIST = []

	def __init__(self):
		self.foo = 0 

	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#54-経過年符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseVYD.CAT_LIST.index(int(input))
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare():
		try:
			CatBaseVYD.CAT_LIST = list(range(4))
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		