import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import model.utility.k_jra_util as util
import os
import inspect
#24-調教師勝率
class Sv021TrWinScore(SvBase):
	_key_list =[
		"sv_tr_score",
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
	def to_sv_from_sr(df_te,program_id, horse_id):
		ret =pd.Series()
		try:
			df_result = df_te	
	
			if(len(df_result)):
				#ret = df_result.iloc[0]
				key = Sv021TrWinScore._key_list[0]
				ret[key] = df_result[key]
			else:
				with  open(r"c:\temp\Sv021TrWinScore.txt", 'a') as f:
					f.write("Sv021TrWinScore None {} {}\r\n".format(program_id, horse_id))
				ret =Sv021TrWinScore.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv021TrWinScore._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv021TrWinScore._key_list)