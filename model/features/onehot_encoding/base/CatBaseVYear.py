import sys
import datetime
import os
import inspect
sys.path.append(r"C:\Dev\py2")
import os
import inspect
from .CatBase import CatBase
#53-開催年符号化
class CatBaseVYear(CatBase):
	CAT_LIST = []

	def __init__(self):
		self.foo = 0 

	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#51-種牡馬符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			if(True == input.isdecimal()):
				ret = CatBaseVYear.CAT_LIST.index(int(input))
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret 

	@staticmethod
	def prepare():
		try:
			today = datetime.date.today()
			year = today.year+1
			from_year =2000
			to_year =year
			CatBaseVYear.CAT_LIST = list(range(from_year, to_year))
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	