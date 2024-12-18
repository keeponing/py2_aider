import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import os
import inspect

#24-直線偏差値
class Sv014StraightDev(SvBase):
	_key_list =[
		"sv_straight_dev",
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
				query ='''
					rh_corner == '10' or rh_corner == '29' 
				'''
				ret =.0	
				df_temp=df_results.query(query, engine='python')
				if(0!=len(df_temp)):
					ret = df_temp['rr_a_deviation'].mean()
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
				key = Sv014StraightDev._key_list[0]
				ret[key] = df_result[key]
			else:
				with  open(r"c:\temp\Sv014StraightDev.txt", 'a') as f:
					f.write("Sv014StraightDev None {} {}\r\n".format(program_id, horse_id))
				ret =Sv014StraightDev.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv014StraightDev._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv014StraightDev._key_list)