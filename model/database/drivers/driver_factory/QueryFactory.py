import inspect
import sys
sys.path.append(r"C:\Dev\py2")
import model.database.query.database_query2.Query_S_ODDS_TANPUKU as qstanpuku
import model.database.query.database_query2.Query_N_RACE as qnrace
import model.database.query.database_query2.Query_S_RACE as qsrace
import model.database.query.database_query2.Query_N_UMA as qnuma
import model.database.query.database_query2.Query_N_UMA_RACE as qnumarace
import model.database.query.database_query2.Query_S_UMA_RACE as qsumarace
import model.database.query.database_query2.Query_N_CHOKYO as qnchokyo
import model.database.query.database_query2.Query_N_KISYU as qnkisyu
import model.database.query.database_query2.Query_N_BANUSI as qnbanusi
import model.database.query.database_query.QueryJAT as qjat
import model.database.query.database_query.QueryJRR as qjrr
import model.database.query.database_query.QueryJPV2 as qjpv
import model.database.query.database_query.QueryJRE as qjre
import model.database.query.database_query.QueryJTD as qjtd
import model.database.query.database_query.QueryJBS as qjbs
import model.database.query.database_query.QueryJJS as qjjs
import model.database.query.database_query.QueryJTS as qjts
import model.database.query.database_query.QueryJBT as qjbt
import model.database.query.database_query.QueryJSV as qjsv
import model.database.query.database_query.QueryJPH as qjph
import model.database.query.database_query.QueryJHV as qjhv
import model.database.query.database_query.QueryJTE as qjte
import model.database.query.database_query.QueryJPC as qjpc
import model.database.query.database_query.QueryJRH as qjrh
import pandas as pd
import model.conf.KJraConst as const
from model.database.drivers.driver_factory.DatabaseFactory import DatabaseFactory
import time
import os
import model.conf.KJraConfig as conf
import pickle
import model.utility.k_jra_util as util
import json
#クエリファクトリ
class QueryFactory:

	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "_instance"):
			cls._instance = super(QueryFactory, cls).__new__(cls)
		return cls._instance
	  
	def __init__(self):
		pass
	

	def get_record_rank_non_zero(self, program_id, horse_id):
		ret = pd.Series()
		try:
			if(program_id != const.VOID_PID):
				y = program_id[:4]
				accessor_pv = DatabaseFactory().get(DatabaseFactory.PV_ACCESSOR2, int(y))
				ret = qjpv.get_record_rank_non_zero_to_df(accessor_pv,program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def get_horse_result_by_hid(self, program_id,horse_id):
		ret = pd.Series()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjrr.get_horse_result_by_hid(accessor_acc,program_id,horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def get_odds_and_vote_to_sr(self, year, md, place, race_no, horse_no):
		ret = pd.Series()
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			
			ret= qstanpuku.get_odds_and_vote_to_sr(accessor_sql, year, md, place, race_no, horse_no)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def get_race_at_to_df2(self, year, md, place, race_no, horse_id):
		ret = pd.DataFrame()
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret = qnumarace.get_race_at_to_df2(
				accessor_sql, year, md, place, race_no, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def get_rank_and_distance_still_ih_to_df(self, program_id, horse_id, ad_year):					
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjre.get_rank_and_distance_still_ih_to_df(
								accessor_acc, program_id, horse_id, ad_year)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret


	def get_describe(self, desc_id):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjtd.get_describe(accessor_acc, desc_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def get_score_by_sire_id_to_df(self, blood01):			
		ret = pd.DataFrame()
		try:
			accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
			ret  = qjbs.get_score_by_sire_id_to_df(accessor_scr, blood01)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret


	
	def get_score_by_id_to_df(self, y, jockey_id):			
		ret = pd.DataFrame()
		try:
			accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
			ret  = qjjs.get_score_by_id_to_df(accessor_scr, y, jockey_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		

	def get_score_by_id_to_df2(self, y, trainer_id):			
		ret = pd.DataFrame()
		try:
			accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
			ret = qjts.get_score_by_id_to_df(accessor_scr, y, trainer_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		

	def get_deviations_still_id_to_df(self, program_id, horse_id):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret  = qjre.get_deviations_still_id_to_df(
								accessor_acc, program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_record_by_ypdt_to_sr(self, sr_re):			
		ret = pd.DataFrame()
		try:
			accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
			ret  = qjbt.get_record_by_ypdt_to_sr(
				accessor_scr,
				sr_re['rh_id'][:4],
				sr_re['rh_id'][8:10],
				sr_re['rh_distance'],
				sr_re['rh_track']
			)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	
				
	def get_speed_exp_by_ph_to_sr(self, program_id, horse_id):			
		ret = pd.DataFrame()
		try:
			y = int(program_id[:4])
			if(y != 0):
				accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
				ret = qjsv.get_speed_exp_by_ph_to_sr(accessor_acc, program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		
		
	def get_max_count(self):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjph.get_max_count(accessor_acc)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		

	def get_max_place_count(self):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjph.get_max_place_count(accessor_acc)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		

	def get_feet_by_h_at_to_df(self, horse_id):			
		ret = pd.DataFrame()
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret = qnuma.get_feet_by_h_at_to_df(accessor_sql, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_sv_by_phid_to_sr(self, accessor_acc, program_id, horse_id):			
		ret = pd.Series()
		try:
			if(accessor_acc is None):
				accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)

			ret = qjsv.get_sv_by_phid_to_sr(accessor_acc, program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret			

	def get_sire_id_to_sr(self, horse_id):			
		ret = pd.Series()
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret = qnuma.get_sire_id_to_sr(accessor_sql,horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_sire_result_by_iste_still_id_to_df(self, program_id,sire_id, tecode):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjrr.get_sire_result_by_iste_still_id_to_df(accessor_acc, program_id,sire_id, tecode)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_sire_result_by_iste_all_to_df(self, program_id, sire_id, bpd_code):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjrr.get_sire_result_by_iste_all_to_df(accessor_acc, program_id, sire_id, bpd_code)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret		

	def get_jocky_id_to_df(self, horse_id, y, md):			
		ret = pd.DataFrame()
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret =  qnumarace.get_jocky_id_to_df(accessor_sql,horse_id, y, md)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	
 
	def get_jocky_result_by_iste_all_to_df(self, program_id,jocky_id, tecode):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjrr.get_jocky_result_by_iste_all_to_df(accessor_acc,program_id,jocky_id, tecode)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_jocky_result_by_iste_still_id_to_df(self, program_id,jocky_id, tecode):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjrr.get_jocky_result_by_iste_still_id_to_df(accessor_acc,program_id,jocky_id, tecode)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_trainer_at_to_df_by_horse_id(self, horse_id):			
		ret = pd.DataFrame()
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret = qnuma.get_trainer_at_to_df_by_horse_id(accessor_sql, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_trainer_result_by_iste_all_to_df(self, program_id,trainer_id, tecode):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjrr.get_trainer_result_by_iste_all_to_df(accessor_acc,program_id,trainer_id, tecode)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret						


	def get_trainer_result_by_iste_still_id_to_df(self, program_id,trainer_id, tecode):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret= qjrr.get_trainer_result_by_iste_still_id_to_df(accessor_acc, program_id,trainer_id, tecode)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def get_hv_one_by_ih_to_sr(self, program_id, horse_id):			
		ret = pd.DataFrame()
		fill_zero = True
		try:
			if(program_id != const.VOID_PID):
				y = program_id[:4]
				if(1999<int(y)):
					accessor_pv = DatabaseFactory().get(DatabaseFactory.PV_ACCESSOR2, int(y))
					ret = qjhv.get_hv_one_by_ih_to_sr(accessor_pv, program_id, horse_id, True)
				if(True==ret.empty):
					fill_zero = True
			if(fill_zero == True):
				dict_zero = {'his_l4_p1': 0, 'his_l4_p2': 0, 'his_l4_p3': 0, 'his_l4_p4': 0}
				ret = pd.Series(dict_zero)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	
	
	def get_hv_one_by_ih_to_sr2(self, program_id, horse_id):			
		ret = pd.DataFrame()
		fill_zero = False
		try:
			if(program_id != const.VOID_PID):
				y = program_id[:4]
				accessor_pv = DatabaseFactory().get(DatabaseFactory.PV_ACCESSOR2, int(y))
				ret = qjhv.get_hv_one_by_ih_to_sr2(accessor_pv, program_id, horse_id)
				if(ret is not None):
					fill_zero = True

			if(fill_zero == False):
				dict_zero = {'his_sc_l4_p1': 0, 'his_sc_l4_p2': 0, 'his_sc_l4_p3': 0, 'his_sc_l4_p4': 0}
				ret = pd.Series(dict_zero)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	
   
	def get_conditions_by_y(self, y):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjre.get_conditions_by_y(accessor_acc, y)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	
	
	def get_rantime_by_ypdtc_to_df(self, y, p, d, t, c):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjre.get_rantime_by_ypdtc_to_df(accessor_acc, y, p, d, t, c)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	
	
	def get_rantime_by_y_to_df(self, y):			
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjre.get_rantime_by_y_to_df(accessor_acc, y)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	
	
	def get_describe_by_pdc_to_sr(self, td):

		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			# ret = qsumarace.get_describe_by_pdc_to_sr(accessor_sql, td)
			# if(0==len(ret)):
			ret = qnumarace.get_describe_by_pdc_to_sr(accessor_sql, td)	
			ret.fillna(0, inplace=True)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def update_td_value(self, sr_desc, td):
		ret = {}
		try:
			accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
			sr_av = qjat.get_record_by_ypdt_to_sr(accessor_scr, 
											td['td_year'], 
											td['td_place'], 
											td['td_track_cd'],
											td['td_distance']							
											)
			if(len(sr_av)):
				td["td_count"] = sr_desc['CntVal'] if sr_desc['CntVal'] is not None else sr_av['at_count']
				td["td_mean"] = sr_desc['AvgVal'] if sr_desc['AvgVal'] is not None else sr_av['td_mean']
				td["td_std"] = sr_desc['StdVal'] if sr_desc['StdVal'] is not None else sr_av['td_std']
				td["td_mean_3f"] = sr_desc['Avg3fVal'] if sr_desc['Avg3fVal'] is not None else sr_av['td_mean_3f']
				td["td_std_3f"] = sr_desc['Std3fVal'] if sr_desc['Std3fVal'] is not None else sr_av['td_std_3f']	
			else:
				td["td_count"] = sr_desc['CntVal'] if sr_desc['CntVal'] is not None else 0
				td["td_mean"] = sr_desc['AvgVal'] if sr_desc['AvgVal'] is not None else 0
				td["td_std"] = sr_desc['StdVal'] if sr_desc['StdVal'] is not None else 50
				td["td_mean_3f"] = sr_desc['Avg3fVal'] if sr_desc['Avg3fVal'] is not None else 0
				td["td_std_3f"] = sr_desc['Std3fVal'] if sr_desc['Std3fVal'] is not None else 50
			ret = td.copy()		
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def update_his_speed_exp_to_sr(self, accessor_acc, his_p_id, horse_id, index):
		ret = pd.Series()
		try:
			if(accessor_acc is None):
				accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			sr_his = qjsv.get_speed_exp_by_ph_to_sr(accessor_acc, his_p_id, horse_id)
			ret[f'his{index}_speed_exp'] = sr_his['sv_speed_exp'] if len(sr_his) > 0 else .0

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	
	def create_his_exp_l4(self, accessor_acc, his_list, horse_id):
		ret = pd.Series()
		try:	
			if(accessor_acc is None):
				accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			for i, his_p_id in enumerate(his_list):
				yh =int(his_p_id[:4])
				if(2000 <= yh and '0000000000' != his_p_id ):
					ret = pd.concat([ret, self.update_his_speed_exp_to_sr(accessor_acc, his_p_id, horse_id, i)]) 
				else:
					ret[f'his{i}_speed_exp'] = .0
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret
	

	def get_hv_by_phid_to_sr(self, accessor_acc, program_id, horse_id):
		ret = pd.Series()
		try:
			if(accessor_acc is None):
				accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjhv.get_hv_one_by_ih_to_sr3(accessor_acc, program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret
	
	def get_te_by_phid_to_sr(self, accessor_acc, program_id, horse_id):
		ret = pd.Series()
		try:
			if(accessor_acc is None):
				accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjte.get_record_to_sr2(accessor_acc, program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret
	
	def get_bs_by_sypdt_to_sr(self, accessor_scr, sire_id, y, place, distance, tarck):
		ret = pd.Series()
		try:
			if(accessor_scr is None):
				accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
			ret = qjbs.get_score_by_siypdt_to_sr(accessor_scr, sire_id, int(y), place, distance, tarck)	
			if(ret.empty):
				ret = qjbs.get_score_by_siypdt_to_sr(accessor_scr, sire_id, int(y)-1, place, distance, tarck)
				if(ret.empty):
					ret = pd.Series(
						data=[sire_id, y, place, distance, tarck, "", 
								0.0, 0.0, 0, 0, 0, ],
						index=['bs_id', 'bs_year', 'bs_place', 'bs_distance', 'bs_track', 'bs_name',
								'bs_win_score', 'bs_mul_score', 'bs_race_count', 'bs_win_count','bs_mul_count']				
					)
					print(sire_id, y, place, distance, tarck)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret
	
	def get_latest_make_date(self):
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret = qsrace.get_latest_make_date(accessor_sql)	
			if(0==len(ret)):
				ret = qnrace.get_latest_make_date(accessor_sql)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
	
		return ret
	
	def get_race_by_makedate_to_df(self, make_date):
		accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
		ret = qsrace.get_race_by_makedate_to_df(accessor_sql, make_date)
		if(0==len(ret)):
			ret = qnrace.get_race_by_makedate_to_df(accessor_sql, make_date)	
		return ret
	
	def get_race_at_to_df4(self, year, md, place, race_no):
		accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
		ret = qsumarace.get_race_at_to_df4(accessor_sql, year, md, place, race_no)
		# if (0 == len(ret)):
		# 	ret = qnumarace.get_race_at_to_df4(accessor_sql, year, md, place, race_no)
		return ret	
	
	def get_categories(self):

		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)


			t_id_categories = qnchokyo.get_all_trainer_id_to_list(accessor_sql)
			j_id_categories = qnkisyu.get_all_jockey_id_to_list(accessor_sql)
			o_id_categories = qnbanusi.get_all_owner_id_to_list(accessor_sql)
			place_id_list = qnrace.get_place_id_to_list(accessor_sql)
			race_hash256_list = qjrh.get_hash256_to_list(accessor_acc)
			t_id_categories.append('99999')
			j_id_categories.append('99999')
			o_id_categories.append('99999')
			place_id_list.append('99')
		except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return t_id_categories, j_id_categories, o_id_categories,place_id_list, race_hash256_list
	
	def get_odds(self, year, md, place, race_no, horse_no):
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			odds = "000"
			vote = "00"

			sr_odds = qstanpuku.get_odds_and_vote_to_sr(
				accessor_sql, year, md, place, race_no, horse_no)

			if (0 != len(sr_odds)):
				odds = sr_odds['TanOdds']
				vote = sr_odds['TanNinki']

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return odds, vote

	def get_mean_and_std_condition_code_by_place(self, y, md, place):
		ret = pd.DataFrame()
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret = qsrace.get_mean_and_std_condition_code_by_place(accessor_sql, y, md, place)
			if(0==len(ret)):
				ret = qnrace.get_mean_and_std_condition_code_by_place(accessor_sql, y, md, place)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	
		
	def get_arg_times(self, y, p, d, t):
		rh_avg_time = .0
		rh_avg_3f_time = .0
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			sr_base = qnumarace.get_base_time_by_ypdc_to_sr(accessor_sql, y, p, d, t)
			if(0==sr_base['CntVal']):
				sr_base = qnumarace.get_base_time_by_ypdc_to_sr2(accessor_sql, y, p, d, t)
			if(0==sr_base['CntVal']):
				sr_base = qnumarace.get_base_time_by_ypdc_to_sr3(accessor_sql, y, p, d, t)
			if(0!=sr_base['CntVal']):
				rh_avg_time=sr_base['AvgVal']
				rh_avg_3f_time=sr_base['Avg3fVal']
				rh_avg_3f_time=rh_avg_3f_time if(30<rh_avg_3f_time ) else 38.0

			else:
				sr_base = qnumarace.get_distance_base_time_by_d_to_sr(accessor_sql, d)									
				rh_avg_time=sr_base['AvgVal']
				rh_avg_3f_time=sr_base['Avg3fVal']
				rh_avg_3f_time=rh_avg_3f_time if(30<rh_avg_3f_time ) else 38.0
		except Exception as e: 
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return rh_avg_time, rh_avg_3f_time
	
	def get_toku_num(self, y, md, place, race_no):
		ret='0000'
		try:
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			ret = qnrace.get_tokunum_by_ymdp(accessor_sql, y, md, place, race_no)
		except Exception as e: 
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	

	def get_horse_by_ir_to_df(self, program_id, race_no, ad_year):
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret =  qjre.get_horse_by_ir_to_df(accessor_acc, program_id, race_no, ad_year)
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	
	def get_result_by_y(self, y):
		ret = pd.DataFrame()
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret =  qjre.get_result_by_y(accessor_acc, y)
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	def get_result_by_ite_still_id_to_df(self, program_id, horse_id, ad_year, skip_file =False):
		ret = pd.DataFrame()
		try:
			start = time.time()
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			# path = conf.CACHE_HISTORY_PATH.format(horse_id)
			# if(os.path.exists(path) and (False == skip_file)):
			# 	with  open(conf.CACHE_HISTORY_PATH.format(horse_id), 'rb') as f:
			# 		ret = pickle.load(f)
			if(0 == len(ret)):
				ret = qjre.get_result_by_ite_still_id_to_df(accessor_acc, program_id, horse_id, ad_year)
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def get_bpd_tecode(self, program_id, race_no):
		ret =""
		try:
			start = time.time()
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)

			df_tecode = qnrace.get_tecode_bpd_to_df(accessor_sql, program_id, race_no)
			if(len(df_tecode) ):
				dt_tecode =df_tecode.iloc[0]
				ret = dt_tecode['TeBPDCode']
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	

	def get_horse_active_duty_to_df(self, y, ad_year):
		try:
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			start = time.time()
			ret =  qjre.get_all_horses_active_duty_by_y_to_df(accessor_acc, y, ad_year)
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	
	def get_record_to_sr(self, program_id, horse_id):
		ret = pd.Series()
		try:

			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)

			ret = qjpc.get_record_to_sr(accessor_acc, program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret

	def get_race_result_by_ir3(self,  program_id, race_no):
		ret = pd.DataFrame()
		try:

			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			ret = qjrr.get_race_result_by_ir3(accessor_acc, program_id, race_no )
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret
	

	def get_te_bpd_list(self):
		ret = pd.DataFrame()
		try:
			path = conf.CACHE_CONF_TE_BPD_LIST_PATH
			if(os.path.exists(path) ):
				with  open(path, 'rb') as f:
					ret = pickle.load(f)
			else:			
				accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
				ret = qnrace.get_te_bpd_list(accessor_sql)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret
	
	def get_te_bd_list(self):
		ret = pd.DataFrame()
		try:
			path = conf.CACHE_CONF_TE_BD_LIST_PATH
			if(os.path.exists(path) ):
				with  open(path, 'rb') as f:
					ret = pickle.load(f)
			else:			
				accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
				ret = qnrace.get_te_bd_list(accessor_sql)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret	
	
	def get_te_c_list(self):
		ret = pd.DataFrame()
		try:
			path = conf.CACHE_CONF_TE_C_LIST_PATH
			if(os.path.exists(path) ):
				with  open(path, 'rb') as f:
					ret = pickle.load(f)
			else:			
				accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
				ret = qnrace.get_te_c_list(accessor_sql)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
		return ret

	# def get_horse_rank_still_by_ph(self, program_id, horse_id, ad_year):
	# 		ret = pd.DataFrame()
	# 		try:
	# 			start = time.time()
	# 			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
	# 			if(0 == len(ret)):
	# 				ret = qjrr.get_horse_rank_still_by_ph(accessor_acc, program_id, horse_id, ad_year)
			
	# 		except Exception as e:
	# 			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	# 		return ret

	def get_horse_rank_still_by_ph(self, program_id, horse_id, ad_year):
		ret = pd.DataFrame()
		try:
			start = time.time()
			path = rf'\\192.168.1.3\E\cache\{horse_id[:4]}'
			if not os.path.exists(path):
				os.makedirs(path)
			file_name = os.path.join(path, f'{horse_id}.txt')
			df_temp = pd.DataFrame()
			if(os.path.exists(file_name)):
				df_temp = pd.read_csv(file_name)
				df_temp['rr_r_rank'] = df_temp['rr_r_rank'].apply(lambda x: '{0:0>2}'.format(x))
			else:
				accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
				df_temp = qjrr.get_horse_full_rank_by_ph(accessor_acc, program_id, horse_id, ad_year)
				if(len(df_temp)):
					df_temp.to_csv(file_name, index=False)

			df_temp['rr_r_id'] = df_temp['rr_r_id'].astype(str)
			ret = df_temp.loc[df_temp['rr_r_id'].str[:8] < program_id[:8]]	
			
		except Exception as e:
			print(f'{program_id, horse_id,os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret