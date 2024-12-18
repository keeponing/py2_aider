import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#異常区分コード符号化
class CatBaseCErr(CatBase):
	CAT_LIST=[]
	def __init__(self):
		self.foo = 0 
		
	#異常区分コード符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			i=0
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		 
		
	#異常区分コード符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			for i in range(len(CatBaseCErr.CAT_LIST)):
				if(CatBaseCErr.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
		
	@staticmethod
	def prepare(df_code):
		try:
			CatBaseCErr.CAT_LIST=[]
			CatBaseCErr.CAT_LIST=df_code.query("type=='2101'")['code'].tolist()		
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	