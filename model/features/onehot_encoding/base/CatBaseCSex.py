import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#性別符号化
class CatBaseCSex(CatBase):
	CAT_LIST=[ ]
	def __init__(self):
		self.foo = 0 

	#性別符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		

	#性別符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			for i in range(len(CatBaseCSex.CAT_LIST)):
				if(CatBaseCSex.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare(df_code):
		try:
			CatBaseCSex.CAT_LIST=[]
			CatBaseCSex.CAT_LIST=df_code.query("type=='2202'")['code'].tolist()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
