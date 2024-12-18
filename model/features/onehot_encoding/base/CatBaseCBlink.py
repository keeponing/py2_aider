import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#ブリンカー符号化
class CatBaseCBlink(CatBase):

	def __init__(self):
		self.foo = 0 

	#ブリンカー符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	#ブリンカー符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = int(input)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	 
		return ret