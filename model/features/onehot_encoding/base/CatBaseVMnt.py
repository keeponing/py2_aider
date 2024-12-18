import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#開催月符号化
class CatBaseVMnt(CatBase):
	CAT_LIST = []
	def __init__(self):
		self.foo = 0 

	#開催月符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#開催月符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			for i in range(len(CatBaseVMnt.CAT_LIST)):
				if(CatBaseVMnt.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare():
		try:
			CatBaseVMnt.CAT_LIST =[]
			month = range(1, 13)
			for m in month:
				temp = f'{m:02}'
				CatBaseVMnt.CAT_LIST.append(temp)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
