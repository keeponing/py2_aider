import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import model.utility.k_jra_util as util

import os
import inspect
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
#24-スピード指数
class Sv023SpeedExp(SvBase):
	_key_list =[
		"sv_speed_exp",		
	]   
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def query(sr_re):
		ret =.0
		try:
			base_time,dist_exponent = Sv023SpeedExp.query_base_time(sr_re)
			time= sr_re['rr_r_time']
			burden = sr_re['rr_r_burden']
			
			racetrack_exp = Sv023SpeedExp.get_racetrack_exponent(sr_re, base_time)
			run_time =util.conv_str_time_to_float(time)
			if(run_time==.0):
				ret =.0
			else:
				ret = util.calc_speed_exponent(
							base_time*10,
							run_time*10,
							dist_exponent,
							racetrack_exp*10,
							float(burden)/10
							)
			return ret 	
				
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
				ret["sv_speed_exp"] = df_result["sv_speed_exp"]
			else:
				with  open(r"c:\temp\Sv023SpeedExp.txt", 'a') as f:
					f.write("Sv023SpeedExp None {} {}\r\n".format(program_id, horse_id))
				ret =Sv023SpeedExp.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv023SpeedExp._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():

		return SvBase.create_zeros(Sv023SpeedExp._key_list)


	@staticmethod				
	def get_racetrack_exponent(sr_re, base_time):
		ret =.0
		if(len(sr_re)):
			ret = (sr_re['rh_avg_time']-base_time)
		return ret 	

	@staticmethod
	def query_base_time(sr_re):
		ret1 =.0
		ret2 =.0

		sr_bt = QueryFactory().get_record_by_ypdt_to_sr(sr_re)
		if(len(sr_bt)):
			ret1 = float(sr_bt['bt_base_time'])
			ret2 = float(sr_bt['bt_dist_exponet'])
		return ret1, ret2 