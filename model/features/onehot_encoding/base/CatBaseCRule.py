import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#競走記号コード符号化
class CatBaseCRule(CatBase):
	CAT_LIST = []
	def __init__(self):
		self.foo = 0 

	#競走記号コード符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#競走記号コード符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			temp0 =input
			for i in range(len(CatBaseCRule.CAT_LIST)):
				if(CatBaseCRule.CAT_LIST[i] == temp0):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		try:
			CatBaseCRule.CAT_LIST=[]
			CatBaseCRule.CAT_LIST=df_code.query("type=='2006'")['code'].tolist()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	