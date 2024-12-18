import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import model.utility.k_jra_util as util
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
import os
import inspect
#24-偏差値
class Sv006Deviation(SvBase):
	_key_list =[
		"sv_deviation",		
	]   
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def query(sr_horse, y, td_desc):
		ret =.0
		try:
			tm = sr_horse['Time']
			if(tm.isnumeric()):
				ret = util.calc_str_time_deviation(tm, td_desc.td_mean, td_desc.td_std)
			ret =  util.calc_str_time_deviation(str(td_desc.td_mean), td_desc.td_mean, td_desc.td_std)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

		finally:
			if(ret == .0):
				ret =  util.calc_str_time_deviation(str(td_desc.td_mean), td_desc.td_mean, td_desc.td_std)
			
		return ret


	@staticmethod
	def to_sv_from_sr(df_te,program_id, horse_id):
		ret =pd.Series()
		try:
			df_result = df_te	
	
			if(len(df_result)):
				#ret = df_result.iloc[0]
				ret["sv_deviation"] = df_result["sv_deviation"]
			else:
				with  open(r"c:\temp\Sv006Deviation.txt", 'a') as f:
					f.write("Sv006Deviation None {} {}\r\n".format(program_id, horse_id))
				ret =Sv006Deviation.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv006Deviation._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():

		return SvBase.create_zeros(Sv006Deviation._key_list)