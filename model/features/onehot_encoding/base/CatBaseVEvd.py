import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect

#25-開催日符号化
class CatBaseVEvd(CatBase):
	CAT_LIST=[]
	def __init__(self):
		self.foo = 0 
	#25-開催日符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#25-開催日符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			for i in range(len(CatBaseVEvd.CAT_LIST)):
				if(CatBaseVEvd.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(max):
		try:
			lst=list(range(1,max))
			inputs=[]
			for i in lst:
				temp = f'{i:02}'
				inputs.append(temp)

			CatBaseVEvd.CAT_LIST=inputs
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

