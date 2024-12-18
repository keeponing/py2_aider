import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import os
import inspect
#24-複勝率
class Sv009MulScore(SvBase):
	_key_list =[
		"sv_mul_ratio",
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
			race_count = len(df_results)
			mul_count = len(df_results[df_results['rr_r_rank'].isin(['01', '02', '03'])])
			ret = mul_count/race_count if race_count != 0 else 0
			
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
				ret["sv_mul_ratio"] = df_result["sv_mul_ratio"]
			else:
				with  open(r"c:\temp\Sv009MulScore.txt", 'a') as f:
					f.write("Sv009MulScore None {} {}\r\n".format(program_id, horse_id))
				ret =Sv009MulScore.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv009MulScore._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv009MulScore._key_list)