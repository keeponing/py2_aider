import sys
sys.path.append(r"C:\Dev\py2")

import pandas as pd
from model.features.statistics_variables.base.SvBase import SvBase
import model.conf.KJraConfig as conf
import model.conf.KJraConst as const
import os
import inspect
#24-勝率加重平均
class Sv010WinScoreWA(SvBase):
	_key_list =[
		"sv_win_score_wa",		
	]   
	_cache_avg={}

	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def query(cls_code, race_count,  score):
		ret =.0
		try:
	
			Sv010WinScoreWA.load_avg()
			ratio1= race_count/const.WA_MAX_COUNT
			ratio2= 1.0-ratio1
			if(0!=cls_code):
				ret = ratio2*Sv010WinScoreWA._cache_avg[int(cls_code)] + ratio1 * score
			else:
				ret=.0
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret


	@staticmethod
	def to_sv_from_sr(df_te, program_id, horse_id):
		ret =pd.Series()
		try:
			df_result = df_te	
	
			if(len(df_result)):
				#ret = df_result.iloc[0]
				ret["sv_win_score_wa"] = df_result["sv_win_score_wa"]
			else:
				with  open(r"c:\temp\Sv008WinScore.txt", 'a') as f:
					f.write("Sv008WinScore None {} {}\r\n".format(program_id, horse_id))
				ret =Sv010WinScoreWA.create_zeros_series()
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		
		
	@staticmethod
	def create_zeros(output):
		df_temp =SvBase.create_zeros(Sv010WinScoreWA._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv010WinScoreWA._key_list)
	
	@staticmethod
	def load_avg():
		if(0==len(Sv010WinScoreWA._cache_avg)):
			if(os.path.exists(conf.WA_WIN_ACG_FILE)):
				with open(conf.WA_WIN_ACG_FILE, 'r') as f:
					# 各行を読み込んで辞書に追加
					for line in f:
						key, value = line.strip().split(': ')
						Sv010WinScoreWA._cache_avg[int(key)] = float(value)