import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import model.utility.k_jra_util as util

import os
import inspect
#24-脚質ターゲットエンコーディング
class Sv001Feets(SvBase):
	_key_list =[
			"sv_feet_pb1",
			"sv_feet_pb2",
			"sv_feet_pb3",
			"sv_feet_pb4",
		]
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def query(sr_horse):
		ret =[]
		try:
			fv=[]
			fv.append(float(sr_horse['Kyakusitu1']))
			fv.append(float(sr_horse['Kyakusitu2']))
			fv.append(float(sr_horse['Kyakusitu3']))
			fv.append(float(sr_horse['Kyakusitu4']))  
			ret = util.softmax(fv)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	# @staticmethod
	# def to_sv_from_db(accessor,program_id, horse_id):
	# 	ret =pd.Series()
	# 	try:
	# 		df_result = qjsv.get_feets_to_sr(accessor, program_id, horse_id)	

	# 		if(len(df_result)):
	# 			ret = df_result.iloc[0]
	# 		else:
	# 			with  open(r"c:\temp\Sv001Feets.txt", 'a') as f:
	# 				f.write("Sv001Feets None {} {}\r\n".format(program_id, horse_id))
	# 			ret =Sv001Feets.create_zeros_series()
			
	# 	except Exception as e:
	# 		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	# 	return ret

	@staticmethod
	def to_sv_from_sr(df_sv,program_id, horse_id):
		ret =pd.Series()
		try:
			df_result = df_sv	

			if(len(df_result)):
				ret["sv_feet_pb1"] = df_result["sv_feet_pb1"]
				ret["sv_feet_pb2"] = df_result["sv_feet_pb2"]
				ret["sv_feet_pb3"] = df_result["sv_feet_pb3"]
				ret["sv_feet_pb4"] = df_result["sv_feet_pb4"]
			else:
				with  open(r"c:\temp\Sv001Feets.txt", 'a') as f:
					f.write("Sv001Feets None {} {}\r\n".format(program_id, horse_id))
				ret =Sv001Feets.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		
	@staticmethod
	def create_zeros(output):

		df_temp =SvBase.create_zeros(Sv001Feets._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():

		return SvBase.create_zeros(Sv001Feets._key_list)