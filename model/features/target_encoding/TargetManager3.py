
import sys
sys.path.append(r"C:\Dev\py2")
import pandas as pd	
#import model.conf.KJraConfig as conf

from model.features.target_encoding.current.Tgt001BPD import Tgt001BPD
from model.features.target_encoding.current.Tgt002BD import Tgt002BD
from model.features.target_encoding.current.Tgt004BPDSY import Tgt004BPDSY
from model.features.target_encoding.current.Tgt005BPDJY import Tgt005BPDJY
from model.features.target_encoding.current.Tgt006BPDTY import Tgt006BPDTY
from model.features.target_encoding.current.Tgt008C2 import Tgt008C2
import os
import inspect
#ターゲットエンコーディングマネージャ
class TargetManager3:
		_target_encoding_list = [
			Tgt001BPD, 
			Tgt002BD, 
			Tgt004BPDSY, 	
			Tgt005BPDJY,	
			Tgt006BPDTY,
			Tgt008C2,
		]
		_target_encoding_of_history_list = [
			Tgt001BPD, 
			Tgt002BD, 
			#Tgt004BPDSY, 	
			Tgt005BPDJY,	
			Tgt006BPDTY,
			Tgt008C2,
		]	
		def __init__(self):
				self.foo = 0 
					
		@staticmethod
		def to_feature(sr_re):
			ret = None
			try:
				target_columns = TargetManager3.get_columns_list()
				ret = TargetManager3.get_element(target_columns, sr_re)		
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			return ret
			
		@staticmethod
		def to_feature_of_history(sr_re):
			ret = None
			try:
				target_columns = TargetManager3.get_columns_list_of_history()
				ret = TargetManager3.get_element(target_columns, sr_re)
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			return ret

		@staticmethod
		def create_zeros(query_columns):
			ret = None
			try:
				output = pd.Series()
				for i in range(len(query_columns)):
					tgt = query_columns[i]
					output = tgt.create_zeros2(output) 
					if(output is None):
						break
				ret = output
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			return ret

		@staticmethod
		def create_zeros_of_history():
			ret = None
			try:
				output = pd.Series()
				lst = TargetManager3._target_encoding_of_history_list
				for i in range(len(lst)):
					tgt = lst[i]
					output = tgt.create_zeros2(output) 
					if(output is None):
						break
				ret = output
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			return ret	
				
		@staticmethod
		def get_element(target_columns, sr_re):
			ret = pd.Series()
			try:
				for column in target_columns:
					ret[column] = sr_re[column]	

				if(0==len(ret)):
					ret = TargetManager3.create_zeros(target_columns)
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			return ret		

		@staticmethod
		def get_columns_list():
			ret =[]
			try:
				lst = TargetManager3._target_encoding_list
				for i in range(len(lst)):
					tgt = lst[i]
					ret.extend(tgt._columns_list)			
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			return ret	

		@staticmethod
		def get_columns_list_of_history():
			ret =[]
			try:
				lst = TargetManager3._target_encoding_of_history_list
				for i in range(len(lst)):
					tgt = lst[i]
					ret.extend(tgt._columns_list)			
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			return ret	