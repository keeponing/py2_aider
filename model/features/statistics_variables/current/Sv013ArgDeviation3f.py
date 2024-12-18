import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import os
import inspect

#24-上がり平均偏差値
class Sv013ArgDeviation3f(SvBase):
	_key_list =[
		"sv_arg_3fd",
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
				ret = df_results['rr_a_deviation3f'].mean()
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
				key = Sv013ArgDeviation3f._key_list[0]
				ret[key] = df_result[key]
			else:
				with  open(r"c:\temp\Sv013ArgDeviation3f.txt", 'a') as f:
					f.write("Sv013ArgDeviation3f None {} {}\r\n".format(program_id, horse_id))
				ret =Sv013ArgDeviation3f.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv013ArgDeviation3f._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv013ArgDeviation3f._key_list)