import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import os
import inspect
#24-平均偏差値
class Sv012ArgDeviation(SvBase):
	_key_list =[
		"sv_arg_dev",
	]   
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def query(df_results):
		ret =.0
		try:
			if(0 != len(df_results)):
				ret = df_results['rr_a_deviation'].mean()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def to_sv_from_sr(df_te,program_id, horse_id):
		ret =pd.Series()
		try:
			df_result = df_te	
	
			if(len(df_result)):
				#ret = df_result.iloc[0]
				ret["sv_arg_dev"] = df_result["sv_arg_dev"]
			else:
				with  open(r"c:\temp\Sv012ArgDeviation.txt", 'a') as f:
					f.write("Sv012ArgDeviation None {} {}\r\n".format(program_id, horse_id))
				ret =Sv012ArgDeviation.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv012ArgDeviation._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv012ArgDeviation._key_list)