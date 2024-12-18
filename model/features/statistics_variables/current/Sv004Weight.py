import inspect
import os
import model.utility.k_jra_util as util
from model.features.statistics_variables.base.SvBase import SvBase
import pandas as pd
import sys
sys.path.append(r"C:\Dev\py2")

# 24-馬体重特徴量


class Sv004Weight(SvBase):
	_key_list = [
		"sv_weight",
	]
	MIN_WEIGHT = 320
	MAX_WEIGHT = 650

	def __init__(self):
		self.foo = 0

	@staticmethod
	def prepare():
		i = 0

	@staticmethod
	def query(sr_horse):
		ret = .0
		try:
			weight = sr_horse['BaTaijyu']
			if (weight.isnumeric()):
				ret = util.percent(int(weight), Sv004Weight.MIN_WEIGHT,
								   Sv004Weight.MAX_WEIGHT)
			# sr_weight = qjrr.get_weight_to_sr(accessor,program_id,horse_id)

			# if(sr_weight is None):
			# 	ret = util.percent(float(weight),  Sv004Weight.MIN_WEIGHT, Sv004Weight.MAX_WEIGHT)
			# else:
			# 	if(True == sr_weight['rr_r_weight'].isnumeric()):
			# 		ret = util.percent(float(sr_weight['rr_r_weight']),Sv004Weight.MIN_WEIGHT, Sv004Weight.MAX_WEIGHT)
			# 	else:
			# 		sr_weight = qjrr.get_prev_weight_to_sr(accessor,program_id,horse_id)
			# 		if(True == sr_weight['rr_r_weight'].isnumeric()):
			# 			ret = util.percent(float(sr_weight['rr_r_weight']),Sv004Weight.MIN_WEIGHT, Sv004Weight.MAX_WEIGHT)

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
				ret["sv_weight"] = df_result["sv_weight"]
			else:
				with open(r"c:\temp\Sv004Weight.txt", 'a') as f:
					f.write("Sv004Weight None {} {}\r\n".format(program_id, horse_id))
				ret = Sv004Weight.create_zeros_series()

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros(output):
		df_temp = SvBase.create_zeros(Sv004Weight._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv004Weight._key_list)
