import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#枠符号化
class CatBaseCFrm(CatBase):
	CAT_LIST=[]
	def __init__(self):
		self.foo = 0 

	#枠符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
   
	#枠符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			temp = int(input)
			for i in range(len(CatBaseCFrm.CAT_LIST)):
				if(CatBaseCFrm.CAT_LIST[i] == temp):
					ret=temp-1
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		try:
			CatBaseCFrm.CAT_LIST=list(range(1,9))
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	