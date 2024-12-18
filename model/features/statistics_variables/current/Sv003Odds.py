import inspect
import os
from model.features.statistics_variables.base.SvBase import SvBase
import pandas as pd
from math import tanh
import sys
import numpy as np
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
sys.path.append(r"C:\Dev\py2")

# オッズ特徴量


class Sv003Odds(SvBase):
	_key_list = [
		"sv_odds",
	]

	def __init__(self):
		self.foo = 0

	@staticmethod
	def query(sr_odds):
		ret = Sv003Odds.odds_tune2(float(999.0))
		try:
			odds = sr_odds['TanOdds']
			if (odds.isnumeric()):
				ret = Sv003Odds.odds_tune2(float(odds)/10.0)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def convert_sv(odds):
		ret = Sv003Odds.odds_tune2(float(999.0))
		try:
			if (odds.isnumeric()):
				ret = Sv003Odds.odds_tune2(float(odds)/10.0)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def query2(program_id, horse_id):

		ret = Sv003Odds.odds_tune2(float(999.0))
		try:

			df_rr = QueryFactory().get_horse_result_by_hid(program_id, horse_id)
			if (df_rr is not None):
				y = program_id[:4]
				md = program_id[4:8]
				race_no = df_rr['rr_r_race']
				place = program_id[8:]
				horse_no = df_rr['rr_r_horse_no']
				sr_odds = QueryFactory().get_odds_and_vote_to_sr(y, md, place, race_no, horse_no)

				if (0 != len(sr_odds)):
					odds = sr_odds['TanOdds']
					if (odds.isdecimal()):
						ret = Sv003Odds.odds_tune2(float(sr_odds['TanOdds'])/10.0)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv_from_sr(sr_sv, program_id, horse_id):
		ret = pd.Series()
		try:

			sr_result = sr_sv
			is_upd = False
			if (len(sr_result)):
				odds = sr_result['sv_odds']
				if (odds != .0):
					ret = pd.Series(data=[odds], index=["sv_odds"], dtype=float)
					is_upd = True
			if (is_upd == False):
				odds = Sv003Odds.query2( program_id, horse_id)
				if (0 != odds):
					ret = pd.Series(data=[odds], index=["sv_odds"], dtype=float)
					#ret = ret.reset_index(drop=True)
				else:
					with open(r"c:\temp\Sv003Odds.txt", 'a') as f:
						f.write("Sv003Odds None {} {}\r\n".format(program_id, horse_id))
					ret = Sv003Odds.create_zeros_series()

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros(output):
		df_temp = SvBase.create_zeros(Sv003Odds._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv003Odds._key_list)

	# @staticmethod
	# def odds_tune(x):
	# 	try:
	# 		if (x == .0):
	# 			return 0
	# 		else:
	# 			return 1-tanh(x/30)
	# 	except Exception as e:
	# 		return 0


	@staticmethod
	def odds_tune2(x):
		try:
			if (x == .0):
				return 0
			else:
				return 1-np.log(x)/7.0 # 7.0 is log(1000)近く
		except Exception as e:
			return 0
