import sys
sys.path.append(r"C:\Dev\py2")
import model.conf.KJraConfig as conf
from .CatBase import CatBase
import os
import inspect
#クラス符号化
class CatBaseCCls(CatBase):
	CAT_LIST = []
	def __init__(self):
		self.foo = 0 

	#クラス符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#クラス符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:		  
			temp1 = conf.code_group_2007[input]
			for i in range(len(CatBaseCCls.CAT_LIST)):
				if(CatBaseCCls.CAT_LIST[i] == temp1):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod		
	def prepare(df_code):
		try:
			CatBaseCCls.CAT_LIST=[]
			#CatBaseCCls.CAT_LIST=df_code.query("type=='2007'")['code'].tolist()	
			CatBaseCCls.CAT_LIST=conf.code_group_2007_value
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

