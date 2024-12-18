import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import model.utility.k_jra_util as util
import os
import inspect
#24-上がり3F偏差値
class Sv007Deviation3f(SvBase):
	_key_list =[
		"sv_deviation3f",
	]    
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def query(sr_horse, td_desc):
		ret =.0
		try:
			tm = sr_horse['HaronTimeL3']
			ret = util.calc_str_3f_time_deviation(tm, td_desc.td_mean_3f, td_desc.td_std_3f)
		
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
				ret["sv_deviation3f"] = df_result["sv_deviation3f"]
			else:
				with  open(r"c:\temp\Sv007Deviation3f.txt", 'a') as f:
					f.write("Sv007Deviation3f None {} {}\r\n".format(program_id, horse_id))
				ret =Sv007Deviation3f.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):

		df_temp =SvBase.create_zeros(Sv007Deviation3f._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv007Deviation3f._key_list)