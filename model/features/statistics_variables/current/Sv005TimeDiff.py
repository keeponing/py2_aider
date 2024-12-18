import inspect
import os
from math import tanh
from model.features.statistics_variables.base.SvBase import SvBase
import pandas as pd
import sys
sys.path.append(r"C:\Dev\py2")

# タイム差特徴量


class Sv005TimeDiff(SvBase):
	_key_list = [
		"sv_timediff",
	]
	MIN_TIMEDIFF = -5
	MAX_TIMEDIFF = 35

	def __init__(self):
		self.foo = 0

	@staticmethod
	def prepare():
		i = 0

	@staticmethod
	def query(sr_horse):
		ret = 1.0
		try:
			timediff = sr_horse['TimeDiff']
			timediff = timediff.replace('+', '')
			if (Sv005TimeDiff.is_num(timediff)):
				ret = Sv005TimeDiff.convert_sv(float(timediff)/10.0)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def query2(sr_horse):
		ret = 1.0
		try:
			timediff = sr_horse['rr_r_time_diff']
			timediff = timediff.replace('+', '')

			if (Sv005TimeDiff.is_num(timediff)):
				
				ret = Sv005TimeDiff.convert_sv(float(timediff)/10.0)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def convert_sv(val):
		ret = 1.0
		try:
			temp = val
			# -5<=x<=35
			if (temp < Sv005TimeDiff.MIN_TIMEDIFF):
				temp = Sv005TimeDiff.MIN_TIMEDIFF
			if (Sv005TimeDiff.MAX_TIMEDIFF < temp):
				temp = Sv005TimeDiff.MAX_TIMEDIFF
			# =(1+TANH(x/MAX_TIMEDIFF))/2
			ret = (1+tanh(temp))/2
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv_from_sr(df_te, program_id, horse_id):
		ret = pd.Series()
		try:
			df_result = df_te

			if (len(df_result)):
				#ret = df_result.iloc[0]
				ret["sv_timediff"] = df_result["sv_timediff"]
			else:
				with open(r"c:\temp\Sv005TimeDiff.txt", 'a') as f:
					f.write("Sv005TimeDiff None {} {}\r\n".format(program_id, horse_id))
				ret = Sv005TimeDiff.create_zeros_series()

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros(output):
		df_temp = SvBase.create_zeros(Sv005TimeDiff._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv005TimeDiff._key_list)

	@staticmethod
	def is_num(a):
		try:
			float(a)
		except:
			return False
		return True
