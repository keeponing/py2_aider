import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#着差符号化
class CatBaseCDiff(CatBase):
	CAT_LIST = []
	DEFAULT_INDEX = 22
	def __init__(self):
		self.foo = 0 

	#着差符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#着差符号化
	@staticmethod
	def to_cats(input):
		ret =CatBaseCDiff.DEFAULT_INDEX
		try:
			temp0 =input
			for i in range(len(CatBaseCDiff.CAT_LIST)):
				if(CatBaseCDiff.CAT_LIST[i] == temp0):
					ret=i
					break
			#該当コードがない場合
			if((ret == CatBaseCDiff.DEFAULT_INDEX) and (3 == len(input))):
				temp0 = input[0]
				for i in range(len(CatBaseCDiff.CAT_LIST)):
					if(CatBaseCDiff.CAT_LIST[i] == temp0):
						ret=i
						break		
    				
		except Exception as e:
			#print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
			ret=0
		return ret

	@staticmethod
	def prepare(df_code):
		try:
			CatBaseCDiff.CAT_LIST=[]
			CatBaseCDiff.CAT_LIST=df_code.query("type=='2102'")['code'].tolist()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
