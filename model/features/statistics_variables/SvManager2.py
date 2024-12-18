
import pandas as pd
import inspect
import os
from model.features.statistics_variables.current.Sv026Vote import Sv026Vote
from model.features.statistics_variables.current.Sv025SpeedExpL4 import Sv025SpeedExpL4
from model.features.statistics_variables.current.Sv024Speed3fExp import Sv024Speed3fExp
from model.features.statistics_variables.current.Sv022JkWinScore import Sv022JkWinScore
from model.features.statistics_variables.current.Sv021TrWinScore import Sv021TrWinScore
from model.features.statistics_variables.current.Sv020SireMulScore import Sv020SireMulScore
from model.features.statistics_variables.current.Sv019SireWinScore import Sv019SireWinScore
from model.features.statistics_variables.current.Sv018DirtDev import Sv018DirtDev
from model.features.statistics_variables.current.Sv017TrufDev import Sv017TrufDev
from model.features.statistics_variables.current.Sv016RCornerDev import Sv016RCornerDev
from model.features.statistics_variables.current.Sv015LCornerDev import Sv015LCornerDev
from model.features.statistics_variables.current.Sv014StraightDev import Sv014StraightDev
from model.features.statistics_variables.current.Sv013ArgDeviation3f import Sv013ArgDeviation3f
from model.features.statistics_variables.current.Sv012ArgDeviation import Sv012ArgDeviation
from model.features.statistics_variables.current.Sv023SpeedExp import Sv023SpeedExp
from model.features.statistics_variables.current.Sv009MulScore import Sv009MulScore
from model.features.statistics_variables.current.Sv008WinScore import Sv008WinScore
from model.features.statistics_variables.current.Sv010WinScoreWA import Sv010WinScoreWA
from model.features.statistics_variables.current.Sv011MulScoreWA import Sv011MulScoreWA

from model.features.statistics_variables.current.Sv007Deviation3f import Sv007Deviation3f
from model.features.statistics_variables.current.Sv005TimeDiff import Sv005TimeDiff
from model.features.statistics_variables.current.Sv004Weight import Sv004Weight
from model.features.statistics_variables.current.Sv003Odds import Sv003Odds
from model.features.statistics_variables.current.Sv002Burden import Sv002Burden
from model.features.statistics_variables.current.Sv010WinScoreWA import Sv010WinScoreWA
from model.features.statistics_variables.current.Sv011MulScoreWA import Sv011MulScoreWA
import model.utility.k_jra_util as util
import sys
import time 
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
sys.path.append(r"C:\Dev\py2")


# 統計量マネージャ


class SvManager2:
	_describe_cache = {}
	_target_encoding_list = [
			# Sv001Feets,
		 			Sv002Burden,
		 			Sv003Odds,
		 			Sv004Weight,
		 			# Sv008WinScore,
		 			# Sv009MulScore,
		 			Sv010WinScoreWA,
		 			Sv011MulScoreWA,
		 			Sv012ArgDeviation,
		 			Sv013ArgDeviation3f,
		 			# Sv014StraightDev,
		 			# Sv015LCornerDev,
		 			# Sv016RCornerDev,
		 			# Sv017TrufDev,
		 			# Sv018DirtDev,
		 			Sv019SireWinScore,
		 			Sv020SireMulScore,
		 			# Sv021TrWinScore,
		 			# Sv022JkWinScore,
		 			Sv025SpeedExpL4,
					Sv026Vote,
		]
	_target_encoding_of_history_list = [
			# Sv001Feets,
		 			Sv002Burden,
		 			Sv003Odds,
		 			Sv004Weight,
		 			Sv005TimeDiff,
		 			# Sv006Deviation,
		 			Sv007Deviation3f,
		 			# Sv008WinScore,
		 			# Sv009MulScore,
		 			Sv010WinScoreWA,
		 			Sv011MulScoreWA,
						# Sv012ArgDeviation,
						# Sv013ArgDeviation3f,
		 			# Sv014StraightDev,
		 			# Sv015LCornerDev,
		 			# Sv016RCornerDev,
		 			# Sv017TrufDev,
		 			# Sv018DirtDev,
		 			Sv019SireWinScore,
		 			Sv020SireMulScore,
		 			# Sv021TrWinScore,
		 			# Sv022JkWinScore,
		 			Sv023SpeedExp,
		 			Sv025SpeedExpL4,
					Sv026Vote
		]
	_target_encoding_hot_list = [
		 			Sv003Odds,
		 			Sv004Weight,
					Sv026Vote,
		]
	def __init__(self):
		self.foo = 0

	@staticmethod
	def query3(program_id, horse_id, horse_no, sr_race, sr_re, df_re, ad_year):
		ret = {}
		try:
			year = program_id[:4]
			md = program_id[4:8]
			place = program_id[8:]
			race_no = sr_race['RaceNum']
			cls_code = sr_re['rh_te_c2_code']
			sr_describe = SvManager2.get_describe(sr_race)

			#df_re = SvManager2.get_re2(program_id, horse_id, df_cache_re)
			ret1 = SvManager2.get_uma_feet(sr_re)
			ret2 = SvManager2.get_uma_race(
				year, md, place, race_no, horse_id, sr_describe)
			ret3 = SvManager2.get_odds(
				year, md, place, race_no, horse_no, sr_re)
			ret4 = SvManager2.get_uma_race3(cls_code, df_re)
			ret5 = SvManager2.get_sire_score(sr_re)
			ret6 = SvManager2.get_tr_score(sr_re)
			ret7 = SvManager2.get_jk_score(sr_re)
			ret8 = SvManager2.get_deviation(df_re)
			ret9 = SvManager2.get_speed_exponent(sr_re)

			ret['sv_program_id'] = program_id
			ret['sv_horse_id'] = horse_id
			ret['sv_feet_pb1'] = ret1['sv_feet_pb1']
			ret['sv_feet_pb2'] = ret1['sv_feet_pb2']
			ret['sv_feet_pb3'] = ret1['sv_feet_pb3']
			ret['sv_feet_pb4'] = ret1['sv_feet_pb4']
			ret['sv_burdern'] = ret2['sv_burdern']
			ret['sv_odds'] = ret3['sv_odds']
			ret['sv_weight'] = ret2['sv_weight']
			ret['sv_timediff'] = ret2['sv_timediff']
			ret['sv_deviation'] = ret2['sv_deviation']
			ret['sv_deviation3f'] = ret2['sv_deviation3f']
			ret['sv_vote'] = ret2['sv_vote']
			ret['sv_win_ratio'] = ret4['sv_win_ratio']
			ret['sv_mul_ratio'] = ret4['sv_mul_ratio']
			ret['sv_win_score_wa'] = ret4['sv_win_score_wa']
			ret['sv_mul_score_wa'] = ret4['sv_mul_score_wa']
			ret['sv_sire_win_score'] = ret5['sv_sire_win_score']
			ret['sv_sire_mul_score'] = ret5['sv_sire_mul_score']
			ret['sv_tr_score'] = ret6['sv_tr_score']
			ret['sv_jk_score'] = ret7['sv_jk_score']
			ret['sv_arg_dev'] = ret8['sv_arg_dev']
			ret['sv_arg_3fd'] = ret8['sv_arg_3fd']
			ret['sv_straight_dev'] = ret8['sv_straight_dev']
			ret['sv_l_corner_dev'] = ret8['sv_l_corner_dev']
			ret['sv_r_corner_dev'] = ret8['sv_r_corner_dev']
			ret['sv_turf_dev'] = ret8['sv_turf_dev']
			ret['sv_dirt_dev'] = ret8['sv_dirt_dev']
			ret['sv_speed_exp'] = ret9['sv_speed_exp']
			ret['sv_speed_3f_exp'] = ret9['sv_speed_3f_exp']
			ret['sv_speed_exp_l4'] = ret9['sv_speed_exp_l4']
			
			ret['upd'] = 2

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv(program_id, horse_id, sr_pc):
		ret = pd.Series()
		try:

			if (len(sr_pc)):
				#df1 = Sv001Feets.to_sv_from_sr(sr_pc, program_id, horse_id)
				df2 = Sv002Burden.to_sv_from_sr(sr_pc, program_id, horse_id)
				df3 = Sv003Odds.to_sv_from_sr(sr_pc, program_id, horse_id)
				df4 = Sv004Weight.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df5 = Sv008WinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df6 = Sv009MulScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				df5 = Sv010WinScoreWA.to_sv_from_sr(sr_pc, program_id, horse_id)
				df6 = Sv011MulScoreWA.to_sv_from_sr(sr_pc, program_id, horse_id)
				df8 = Sv012ArgDeviation.to_sv_from_sr(sr_pc, program_id, horse_id)
				df9 = Sv013ArgDeviation3f.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df10 = Sv014StraightDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df11 = Sv015LCornerDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df12 = Sv016RCornerDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df13 = Sv017TrufDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df14 = Sv018DirtDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				df15 = Sv019SireWinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				df16 = Sv020SireMulScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				df17 = Sv021TrWinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				df18 = Sv022JkWinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				#df19 = Sv023SpeedExp.to_sv_from_sr(sr_pc, program_id, horse_id)
				df20 = Sv025SpeedExpL4.to_sv_from_sr(sr_pc, program_id, horse_id)
				df21 = Sv026Vote.to_sv_from_sr(sr_pc, program_id, horse_id)
				ret = pd.concat([
									df2,  df3,  df4,  df5,  df6,   df8,  df9,
									# df10 ,df11, df12, df13, df14,
									df15, df16, df17, df18,  # ,df19,
									df20, df21
								])
			else:
				ret = SvManager2.create_zeros()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv_hot(program_id, horse_id, sr_pc):
		ret = pd.Series()
		try:

			if (len(sr_pc)):
				df1 = Sv003Odds.to_sv_from_sr(sr_pc, program_id, horse_id)
				df2 = Sv004Weight.to_sv_from_sr(sr_pc, program_id, horse_id)
				df3 = Sv026Vote.to_sv_from_sr(sr_pc, program_id, horse_id)
				ret = pd.concat([
									df1,  df2,  df3
								])
			else:
				ret = SvManager2.create_zeros_hot()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_sv_of_history(program_id, horse_id, sr_pc):
		ret = None
		try:
			if (len(sr_pc)):
				#df1  = Sv001Feets.to_sv_from_sr(sr_pc, program_id, horse_id)
				df2 = Sv002Burden.to_sv_from_sr(sr_pc, program_id, horse_id)
				df3 = Sv003Odds.to_sv_from_sr(sr_pc,  program_id, horse_id)
				df4 = Sv004Weight.to_sv_from_sr(sr_pc, program_id, horse_id)
				df5 = Sv005TimeDiff.to_sv_from_sr(sr_pc, program_id, horse_id)
				#df6  = Sv006Deviation.to_sv_from_sr(sr_pc, program_id, horse_id)
				df7 = Sv007Deviation3f.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df8 = Sv008WinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df9 = Sv009MulScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				df8 = Sv010WinScoreWA.to_sv_from_sr(sr_pc, program_id, horse_id)
				df9 = Sv011MulScoreWA.to_sv_from_sr(sr_pc, program_id, horse_id)
				
				# df11 = Sv012ArgDeviation.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df12 = Sv013ArgDeviation3f.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df13 = Sv014StraightDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df14 = Sv015LCornerDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df15 = Sv016RCornerDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df16 = Sv017TrufDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df17 = Sv018DirtDev.to_sv_from_sr(sr_pc, program_id, horse_id)
				df18 = Sv019SireWinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				df19 = Sv020SireMulScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df20 = Sv021TrWinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				# df21 = Sv022JkWinScore.to_sv_from_sr(sr_pc, program_id, horse_id)
				df22 = Sv023SpeedExp.to_sv_from_sr(sr_pc, program_id, horse_id)
				df23 = Sv025SpeedExpL4.to_sv_from_sr(sr_pc, program_id, horse_id)
				df24 = Sv026Vote.to_sv_from_sr(sr_pc, program_id, horse_id)
				ret = pd.concat([
								# df1,
								df2,  df3,  df4,  df5,  # df6,
								df7,  df8,  df9,
								# df11, df12,
								# df13, df14, df15, df16, df17,
								df18, df19,
								#df20, df21,
								df22, df23,df24
								])
			else:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name}')
				ret = SvManager2.create_zeros_of_history()
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros():
		ret = None
		try:
			output = pd.Series()
			lst = SvManager2._target_encoding_list
			for i in range(len(lst)):
				tgt = lst[i]
				output = tgt.create_zeros(output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros_hot():
		ret = None
		try:
			output = pd.Series()
			lst = SvManager2._target_encoding_hot_list
			for i in range(len(lst)):
				tgt = lst[i]
				output = tgt.create_zeros(output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
	@staticmethod
	def create_zeros_of_history():
		ret = None
		try:
			output = pd.Series()
			lst = SvManager2._target_encoding_of_history_list
			for i in range(len(lst)):
				tgt = lst[i]
				output = tgt.create_zeros(output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_uma_feet(sr_re):
		ret = {}
		start = time.time()
		try:
			ret['sv_feet_pb1'] = .0
			ret['sv_feet_pb2'] = .0
			ret['sv_feet_pb3'] = .0
			ret['sv_feet_pb4'] = .0		
			if (False == sr_re.empty):
				ret['sv_feet_pb1'] = sr_re['rr_m_feet1']
				ret['sv_feet_pb2'] = sr_re['rr_m_feet2']
				ret['sv_feet_pb3'] = sr_re['rr_m_feet3']
				ret['sv_feet_pb4'] = sr_re['rr_m_feet4']
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_uma_race(year, md, place, race_no, horse_id, sr_describe):
		ret = {}
		start = time.time()
		try:
			ret['sv_burdern'] = .0
			ret['sv_weight'] = .0
			ret['sv_timediff'] = .0
			ret['sv_deviation'] = .0
			ret['sv_deviation3f'] = .0
			ret['sv_vote'] = .0

			df_horse = QueryFactory().get_race_at_to_df2(year, md, place, race_no, horse_id)
			if (len(df_horse)):
				sr_horse = df_horse.iloc[0]
				ret['sv_burdern'] = Sv002Burden.query(sr_horse)
				ret['sv_weight'] = Sv004Weight.query(sr_horse)
				ret['sv_timediff'] = Sv005TimeDiff.query(sr_horse)
				ret['sv_deviation'] = 0#Sv006Deviation.query(sr_horse, sr_describe)
				ret['sv_deviation3f'] = Sv007Deviation3f.query(sr_horse, sr_describe)
				ret['sv_vote'] = Sv026Vote.query(sr_horse)
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	
	@staticmethod
	def get_uma_race3(cls_code, df_horses):
		ret = {}
		start = time.time()
		try:
			ret['sv_win_ratio'] = .0
			ret['sv_mul_ratio'] = .0
			ret['sv_win_score_wa'] = .0
			ret['sv_mul_score_wa'] = .0

			if (race_count:=len(df_horses)):
				ret['sv_win_ratio'] = Sv008WinScore.query(df_horses)
				ret['sv_mul_ratio'] = Sv009MulScore.query(df_horses)
				
				ret['sv_win_score_wa'] = Sv010WinScoreWA.query(cls_code, race_count, ret['sv_win_ratio'])
				ret['sv_mul_score_wa'] = Sv011MulScoreWA.query(cls_code, race_count, ret['sv_mul_ratio'])
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
	@staticmethod
	def get_odds(year, md, place, race_no, horse_no, sr_re):
		ret = {}
		start = time.time()
		try:
			ret['sv_odds'] = .0
			sr_odds = QueryFactory().get_odds_and_vote_to_sr(year, md, place, race_no, horse_no)

			temp = {}
			if (0 != len(sr_odds)):
				temp['TanOdds'] = sr_odds['TanOdds']
			if (0 == len(temp)):
				temp['TanOdds'] = sr_re['rr_r_odds']
			ret['sv_odds'] = Sv003Odds.query(temp)
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_describe(sr_race):
		start = time.time()
		ret = pd.Series()
		desc_id = ""
		try:
			place = sr_race['JyoCD']
			distance = sr_race['Kyori']
			cls2 = sr_race['JyokenCD1']
			cls3 = sr_race['JyokenCD2']
			cls4 = sr_race['JyokenCD3']
			cls5over = sr_race['JyokenCD4']
			clsYoung = sr_race['JyokenCD5']
			category = sr_race['SyubetuCD']
			track = sr_race['TrackCD']
			weather = sr_race['TenkoCD']
			turf_condition = sr_race['SibaBabaCD']
			dirt_condition = sr_race['DirtBabaCD']
			desc_id = "{0}_{1}_{2}_{3}_{4}_{5}_{6}_{7}_{8}_{9}_{10}_{11}".format(
				place,
				distance,
				cls2,
				cls3,
				cls4,
				cls5over,
				clsYoung,
				category,
				track,
				weather,
				turf_condition,
				dirt_condition
			)
			if (desc_id in SvManager2._describe_cache):
				ret = SvManager2._describe_cache[desc_id]
			else:
				df_temp = QueryFactory().get_describe(desc_id)
				if (0 != len(df_temp)):
					ret = df_temp.iloc[0]
					SvManager2._describe_cache[desc_id] = ret
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_sire_score(sr_re):
		start = time.time()
		ret = {}
		ret['sv_sire_win_score'] = .0
		ret['sv_sire_mul_score'] = .0
		try:
			blood01 = sr_re['rr_m_blood01']
			y =  sr_re['ph_year']
			p =  sr_re['ph_place']
			d =  sr_re['rh_distance']
			t =  sr_re['rh_track']
			sr_score = QueryFactory().get_bs_by_sypdt_to_sr(None, blood01, y, p, d, t)

			if ((0 != len(sr_score)) and (blood01 != '00000000')):
				ret['sv_sire_win_score'] = sr_score['bs_win_score']
				ret['sv_sire_mul_score'] = sr_score['bs_mul_score']
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_jk_score(sr_re):
		start = time.time()
		ret = {}
		ret['sv_jk_score'] = .0
		try:
			y = sr_re['rr_r_id'][:4]
			jockey_id = sr_re['rr_r_j_id']

			df_j_scores = QueryFactory().get_score_by_id_to_df(y, jockey_id)
			if ((0 != len(df_j_scores)) and (jockey_id != '00000')):
				dt_j_score = df_j_scores.iloc[0]
				ret['sv_jk_score'] = dt_j_score['js_win_score']
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_tr_score(sr_re):
		ret = {}
		start = time.time()
		ret['sv_tr_score'] = .0
		try:
			y = sr_re['rr_r_id'][:4]
			trainer_id = sr_re['rr_r_t_id']
			df_t_scores = QueryFactory().get_score_by_id_to_df2(y, trainer_id)
			if ((0 != len(df_t_scores)) and (trainer_id != '00000')):
				dt_t_score = df_t_scores.iloc[0]
				ret['sv_tr_score'] = dt_t_score['ts_win_score']
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_re(program_id, horse_id):
		start = time.time()
		ret = pd.DataFrame()
		try:
			ret = QueryFactory().get_deviations_still_id_to_df(program_id, horse_id)
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_deviation(df_re):
		ret = {}
		start = time.time()
		try:
			ret['sv_arg_dev'] = Sv012ArgDeviation.query(df_re)
			ret['sv_arg_3fd'] = Sv013ArgDeviation3f.query(df_re)
			ret['sv_straight_dev'] = Sv014StraightDev.query(df_re)
			ret['sv_l_corner_dev'] = Sv015LCornerDev.query(df_re)
			ret['sv_r_corner_dev'] = Sv016RCornerDev.query(df_re)
			ret['sv_turf_dev'] = Sv017TrufDev.query(df_re)
			ret['sv_dirt_dev'] = Sv018DirtDev.query(df_re)
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def get_speed_exponent(sr_re):
		ret = {}
		start = time.time()
		try:
			ret['sv_speed_exp'] = Sv023SpeedExp.query(sr_re)
			ret['sv_speed_3f_exp'] = Sv024Speed3fExp.query(sr_re)
			ret['sv_speed_exp_l4'] = Sv025SpeedExpL4.query(sr_re)
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
