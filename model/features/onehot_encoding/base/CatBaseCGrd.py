import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect

#グレード符号化
class CatBaseCGrd(CatBase):
	CAT_LIST = range(0,6)
	def __init__(self):
		self.foo = 0 

	#グレード符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#グレード符号化
	@staticmethod
	def to_cats(input):
		ret =9 #　なし
		try:
			for i in range(len(CatBaseCGrd.CAT_LIST)):
				if(CatBaseCGrd.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod		
	def prepare(df_code):
		try:
			CatBaseCGrd.CAT_LIST=[]
			df_temp=df_code.query("type=='2003'")['code']	
			CatBaseCGrd.CAT_LIST= df_temp.fillna("").tolist()	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	