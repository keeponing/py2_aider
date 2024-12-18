import inspect
import os
import model.conf.KJraConst as const
import model.utility.k_jra_util as util
from model.features.statistics_variables.base.SvBase import SvBase
import pandas as pd
import sys
sys.path.append(r"C:\Dev\py2")

# 


class Sv026Vote(SvBase):
	_key_list = [
		"sv_vote",
	]
	MIN_VOTE = 1
	MAX_VOTE = 18

	def __init__(self):
		self.foo = 0

	@staticmethod
	def prepare():
		i = 0

	@staticmethod
	def query(sr_horse):
		ret = .0
		try:
			burden = sr_horse['Ninki']
			if (burden.isnumeric()):
				ret = Sv026Vote.convert_sv(burden)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def query2(sr_horse):
		ret = .0
		try:
			burden = sr_horse['rr_r_vote']
			if (burden.isnumeric()):
				ret = Sv026Vote.convert_sv(burden)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
		
	@staticmethod
	def convert_sv(vote):
		ret = 0
		try:
			if (vote.isnumeric()):
				vote2 = int(vote)
				if(vote2==0):
					vote2=Sv026Vote.MAX_VOTE
				ret = 1.0 - util.percent(vote2,  Sv026Vote.MIN_VOTE, Sv026Vote.MAX_VOTE)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv_from_sr(sr_sv, program_id, horse_id):
		ret = pd.Series()
		try:
			if (len(sr_sv)):
				ret["sv_vote"] = sr_sv["sv_vote"]
			else:
				with open(r"c:\temp\Sv002Burden.txt", 'a') as f:
					f.write("Sv026Vote None {} {}\r\n".format(program_id, horse_id))
				ret = Sv026Vote.create_zeros_series()

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros(output):
		df_temp = SvBase.create_zeros(Sv026Vote._key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return SvBase.create_zeros(Sv026Vote._key_list)
