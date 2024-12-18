import inspect
import os

import model.utility.k_jra_util as util
from model.features.statistics_variables.base.SvBase import SvBase
import pandas as pd
import sys
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
sys.path.append(r"C:\Dev\py2")

# 24-スピード指数


class Sv024Speed3fExp(SvBase):
	_key_list = [
		"sv_speed_3f_exp",
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
			base_time, dist_exponent = Sv024Speed3fExp.query_base_time(sr_re)
			time = sr_re['rr_r_f3_time']
			burden = sr_re['rr_r_burden']
			if (time == '000'):
				ret = .0
			else:
				time = time if (time > '300') else '380'
				racetrack_exp = Sv024Speed3fExp.get_racetrack_exponent(sr_re, base_time)
				run_time = util.conv_str_3f_time_to_float(time)

				ret = util.calc_speed_3f_exponent(
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
	def to_sv_from_sr(sr_sv, program_id, horse_id):
		ret = pd.Series()
		try:

			if (len(sr_sv)):
				ret["sv_speed_3f_exp"] = sr_sv["sv_speed_3f_exp"]
			else:
				with open(r"c:\temp\Sv024Speed3fExp.txt", 'a') as f:
					f.write("Sv024Speed3fExp None {} {}\r\n".format(program_id, horse_id))
				ret = Sv024Speed3fExp.create_zeros_series()

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros(output):
		df_temp = SvBase.create_zeros(Sv024Speed3fExp._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv024Speed3fExp._key_list)

	@staticmethod
	def get_racetrack_exponent(sr_re, base_time):
		ret = .0
		if (len(sr_re)):
			ret = (sr_re['rh_avg_3f_time']-base_time)
		return ret

	@staticmethod
	def query_base_time(sr_re):
		ret1 = .0
		ret2 = .0
		sr_bt = QueryFactory().get_record_by_ypdt_to_sr(sr_re)
		if (len(sr_bt)):
			ret1 = float(sr_bt['bt_3f_time'])
			ret2 = float(sr_bt['bt_dist_exponet'])
		return ret1, ret2
