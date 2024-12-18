import statistics
import inspect
import os
import model.database.query.database_query.QueryJSV as qjsv
import model.utility.k_jra_util as util
from model.features.statistics_variables.base.SvBase import SvBase
import pandas as pd
import sys
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
sys.path.append(r"C:\Dev\py2")

# 24-スピード指数(最新4走平均)


class Sv025SpeedExpL4(SvBase):
	_key_list = [
		"sv_speed_exp_l4",
	]

	def __init__(self):
		self.foo = 0

	@staticmethod
	def prepare():
		i = 0

	@staticmethod
	def query(sr_re):
		ret = .0
		try:
			lst = []
			lst.append(sr_re['rr_h_prev_id1'])
			lst.append(sr_re['rr_h_prev_id2'])
			lst.append(sr_re['rr_h_prev_id3'])
			lst.append(sr_re['rr_h_prev_id4'])
			horse_id = sr_re['rr_r_horse_id']
			extract_exp = []
			for i in range(len(lst)):
				program_id = lst[i]
				
				func = QueryFactory().get_speed_exp_by_ph_to_sr
				sr_his = func(program_id, horse_id)
				if (0 < len(sr_his)):
					extract_exp.append(sr_his['sv_speed_exp'])
			if (len(extract_exp)):
				ret = statistics.mean(extract_exp)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv_from_sr(sr_sv, program_id, horse_id):
		ret = pd.Series()
		try:

			if (len(sr_sv)):
				ret["sv_speed_exp_l4"] = sr_sv["sv_speed_exp_l4"]
			else:
				with open(r"c:\temp\Sv025SpeedExpL4.txt", 'a') as f:
					f.write("Sv025SpeedExpL4 None {} {}\r\n".format(program_id, horse_id))
				ret = Sv025SpeedExpL4.create_zeros_series()

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros(output):
		df_temp = SvBase.create_zeros(Sv025SpeedExpL4._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv025SpeedExpL4._key_list)
