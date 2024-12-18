import inspect
import os
import model.conf.KJraConst as const
import model.utility.k_jra_util as util
from model.features.statistics_variables.base.SvBase import SvBase
import pandas as pd
import sys
sys.path.append(r"C:\Dev\py2")

# 負担重量特徴量


class Sv002Burden(SvBase):
	_key_list = [
		"sv_burdern",
	]
	MIN_BURDEN = 47.0
	MAX_BURDEN = 80.0

	def __init__(self):
		self.foo = 0

	@staticmethod
	def prepare():
		i = 0

	@staticmethod
	def query(sr_horse):
		ret = .0
		try:
			burden = sr_horse['Futan']
			if (burden.isnumeric()):
				ret = Sv002Burden.convert_sv(burden)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def convert_sv(burden):
		ret = .0
		try:
			ret = util.percent(float(burden)/10.0,  const.MIN_BURDEN, const.MAX_BURDEN)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv_from_sr(sr_sv, program_id, horse_id):
		ret = pd.Series()
		try:
			if (len(sr_sv)):
				ret["sv_burdern"] = sr_sv["sv_burdern"]
			else:
				with open(r"c:\temp\Sv002Burden.txt", 'a') as f:
					f.write("Sv002Burden None {} {}\r\n".format(program_id, horse_id))
				ret = Sv002Burden.create_zeros_series()

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros(output):
		df_temp = SvBase.create_zeros(Sv002Burden._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv002Burden._key_list)
