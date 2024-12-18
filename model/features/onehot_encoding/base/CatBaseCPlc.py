import sys
sys.path.append(r"C:\Dev\py2")
import model.conf.KJraConfig as conf
from .CatBase import CatBase
import os
import inspect
#開催場符号化
class CatBaseCPlc(CatBase):
	CAT_LIST = []
	def __init__(self):
		self.foo = 0 

	#開催場符号化
	@staticmethod
	def to_onehot(sr_value, keylist, keys_code, key_format):
		try:	
			return CatBase.to_onehot(sr_value, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#開催場符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			temp1 = conf.code_group_2001[input]
			for i in range(len(CatBaseCPlc.CAT_LIST)):
				if(CatBaseCPlc.CAT_LIST[i] == temp1):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def prepare(df_code):
		try:
			CatBaseCPlc.CAT_LIST=[]
			#CatBaseCPlc.CAT_LIST=df_code.query("type=='2001'")['code'].tolist()
			CatBaseCPlc.CAT_LIST=conf.code_group_2001_value
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
