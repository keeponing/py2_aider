import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#負担重量条件符号化
class CatBaseCRcnd(CatBase):
	CAT_LIST=[]
	def __init__(self):
		self.foo = 0 
	#負担重量条件符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#負担重量条件符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			for i in range(len(CatBaseCRcnd.CAT_LIST)):
				if(CatBaseCRcnd.CAT_LIST[i] == input):
					ret=i
					break
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	@staticmethod
	def prepare(df_code):
		try:
			CatBaseCRcnd.CAT_LIST=[]
			CatBaseCRcnd.CAT_LIST=df_code.query("type=='2008'")['code'].tolist()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	