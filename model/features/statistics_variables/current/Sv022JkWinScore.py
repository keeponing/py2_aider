import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import model.utility.k_jra_util as util
import os
import inspect
#24-ジョッキー勝率
class Sv022JkWinScore(SvBase):
	_key_list =[
		"sv_jk_score",
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
			#TODO
			i=0
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	@staticmethod
	def to_sv_from_sr(df_sv,program_id, horse_id):
		ret =pd.Series()
		try:
			df_result = df_sv	
	
			if(len(df_result)):
				#ret = df_result.iloc[0]
				key = Sv022JkWinScore._key_list[0]
				ret[key] = df_result[key]
			else:
				with  open(r"c:\temp\Sv022JkWinScore.txt", 'a') as f:
					f.write("Sv022JkWinScore None {} {}\r\n".format(program_id, horse_id))
				ret =Sv022JkWinScore.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv022JkWinScore._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv022JkWinScore._key_list)