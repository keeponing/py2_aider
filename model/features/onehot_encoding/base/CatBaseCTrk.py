import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#トラックコード符号化
class CatBaseCTrk(CatBase):
	CAT_LIST = []
	def __init__(self):
		self.foo = 0 

	#トラックコード符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#トラックコード符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			temp0 =input
			for i in range(len(CatBaseCTrk.CAT_LIST)):
				if(CatBaseCTrk.CAT_LIST[i] == temp0):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		try:
			CatBaseCTrk.CAT_LIST=[]
			CatBaseCTrk.CAT_LIST=df_code.query("type=='2009'")['code'].tolist()		
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
