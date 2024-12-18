import sys
sys.path.append(r"C:\Dev\py2")

from .CatBase import CatBase
import os
import inspect
#23-クラス符号化
class CatBaseCls(CatBase):
	CAT_LIST = range(1, 14)
	def __init__(self):
		self.foo = 0 

	#23-クラス符号化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#23-クラス符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:		  
			#	1	→	0
			#	2	→	1
			#	3	→	2
			#	4	→	3
			#	5	→	4
			#	6	→	5
			#	7	→	6
			#	8	→	7
			#	9	→	8
			#	10	→	9
			#	11	→	10
			#	12	→	11
			#	13	→	12
			# if(0 < input):
			# 	ret =input-1
			for i in range(len(CatBaseCls.CAT_LIST)):
				if(CatBaseCls.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

