import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#カテゴリ符号化
class CatBaseCCat(CatBase):
	def __init__(self):
		self.foo = 0 

	#30-カテゴリ符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#カテゴリ符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			for i in range(len(CatBaseCCat.CAT_LIST)):
				if(CatBaseCCat.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod		
	def prepare(df_code):
		try:
			CatBaseCCat.CAT_LIST=[]
			CatBaseCCat.CAT_LIST=df_code.query("type=='2005'")['code'].tolist()		
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
