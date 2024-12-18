import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import os
import inspect

#24-種牡馬勝率
class Sv019SireWinScore(SvBase):
	_key_list =[
		"sv_sire_win_score",
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
				key = Sv019SireWinScore._key_list[0]
				ret[key] = df_result[key]
			else:
				with  open(r"c:\temp\Sv019SireWinScore.txt", 'a') as f:
					f.write("Sv019SireWinScore None {} {}\r\n".format(program_id, horse_id))
				ret =Sv019SireWinScore.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv019SireWinScore._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv019SireWinScore._key_list)