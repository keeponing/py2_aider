
import pandas as pd
from model.features.onehot_encoding.CategoryManager4  import CategoryManager4
from model.data_createor.Pat009BaseDataCreator import Pat009BaseDataCreator
from model.features.statistics_variables.SvManager2 import SvManager2
import model.conf.KJraConfig as conf
import os
import inspect
import time
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
from model.database.drivers.driver_factory.DatabaseFactory import DatabaseFactory
import model.database.query.database_query2.Query_N_RACE as qnrace
import model.utility.k_jra_util as util
import time
# 教師データDB登録データ（過去4走りれきなし）
class Pat009PvdbDataCreator(Pat009BaseDataCreator):

	def __init__(self):
		super().__init__()

	def create_pv(self, program_id, horse_id, sr_re):
		ret = None
		try:	
			sr_sv = QueryFactory().get_sv_by_phid_to_sr(None, program_id, horse_id)

			sr_mix =pd.concat([sr_re, sr_sv])
			sr_current = pd.Series()

			sr_current = self._create_header_block_data_from_rr(sr_mix)
			sr_seed = self._create_category_seed(sr_mix)
			sr_category = CategoryManager4.to_cats(sr_seed)
	
			ret = pd.concat([sr_current, sr_category])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
								
	
	def create_sv(self, sr_race, sr_re, df_re, ad_year):
		ret = None
		try:	
			program_id = sr_re['ph_id']
		
			horse_id = sr_re['rr_r_horse_id']
			horse_no = sr_re['rr_r_horse_no']
				
			ret = SvManager2.query3(program_id, horse_id, horse_no, sr_race, sr_re, df_re, ad_year)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def create_te(self, sr_re, df_re, te_code_bpd):
		ret = None
		try:	
			start = time.time()
			#accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
			df_tecode_bpd_list = QueryFactory().get_te_bpd_list()
			df_tecode_bd_list =  QueryFactory().get_te_bd_list()
			df_tecode_c_list =  QueryFactory().get_te_c_list()	
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
			program_id = sr_re['ph_id']
			race_no = sr_re['rh_race']
			horse_id = sr_re['rr_r_horse_id']	
			
			df_results = self._get_rank_still_id_by_hid_to_df(df_re, program_id)
			te ={}
			te['te_id'] = program_id
			te['te_race'] = race_no
			te['te_horse_id'] = horse_id
			te['te_bpds'] = 0
			te['upd'] = 1
			df1 = self._get_bpd_to_df(df_results, df_tecode_bpd_list)
			df2 = self._get_bd_to_df(df_results,  df_tecode_bd_list)
			df3 = self._get_c_to_df(df_results,  df_tecode_c_list)
			df4 = self._get_bpdsy_to_df(sr_re, te_code_bpd)
			df5 = self._get_bpdjy_to_df(sr_re, te_code_bpd)
			df6 = self._get_bpdty_to_df(sr_re, te_code_bpd)
			df7 = self._get_c2_to_df(df_results)
			te.update(df1)
			te.update(df2)
			te.update(df3)
			te.update(df4)
			te.update(df5)
			te.update(df6)
			te.update(df7)
			ret = te	
			
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def _get_rank_still_id_by_hid_to_df(self, df_cache_re, program_id):
		ret = pd.DataFrame()
		try:
			start = time.time()

			if(len(df_cache_re)):
				query=f" ph_year+ph_monthday < '{program_id[:8]}' and rr_r_rank != '00' "
				ret= df_cache_re.query(query, engine='python')
				ret['rank'] = ret['rr_r_rank'].astype('int')
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	
	def _get_bpd_to_df(self, df_results, df_tecode_list):
		ret ={}
		try:
			start = time.time()
			te ={}
			if(len(df_results)):
				for k in range(len(df_tecode_list)):
					dt_te_code = df_tecode_list.iloc[k]
					te_code = dt_te_code['TeBPDCode']
					query ='''
						rh_te_bpd_code == '{0}' 
					'''.format(te_code)
					
					df_results2 = df_results.query(query, engine='python')
					te[f'te_{te_code}'] = util.calc_rank_average(df_results2)

			ret = te
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def _get_bd_to_df(self, df_results, df_tecode_list):
		try:
			start = time.time()
			te ={}
			for k in range(len(df_tecode_list)):
				dt_te_code =df_tecode_list.iloc[k]
				te_code = dt_te_code['TeBDCode']
				query ='''
					rh_te_bd_code == '{0}' 
				'''.format(te_code)
				df_results2 = pd.DataFrame()
				if(len(df_results)):
					df_results2 = df_results.query(query, engine='python')
				te['te_'+te_code] = util.calc_rank_average(df_results2)

			ret = te
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret


	def _get_c_to_df(self, df_results, df_tecode_list):
		ret = pd.DataFrame()
		try:
			start = time.time()
			te ={}	
			for k in range(len(df_tecode_list)):
				dt_te_code =df_tecode_list.iloc[k]
				te_code = dt_te_code['TeCCode']
				query ='''
					rh_te_c_code == '{0}' 
				'''.format(te_code)
				df_results2 = pd.DataFrame()
				if(len(df_results)):
					df_results2 = df_results.query(query, engine='python')	
				te['te_'+te_code] = util.calc_rank_average(df_results2)
				
			#print("c:",program_id, race_no, horse_id)
			ret = te
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def _get_bpdsy_to_df(self, sr_re, tecode):
		ret = pd.DataFrame()
		try:
			start = time.time()
			program_id = sr_re['ph_id']
			horse_id = sr_re['rr_r_horse_id']	

			sire_id =  QueryFactory().get_sire_id_to_sr(horse_id)
			te ={}
			df_ranks = pd.DataFrame()
			if(len(df_results1 :=  QueryFactory().get_sire_result_by_iste_all_to_df(program_id,sire_id, tecode))):
				df_ranks = pd.concat([df_ranks, df_results1], axis=0 )

			if(len(df_results2 := QueryFactory().get_sire_result_by_iste_still_id_to_df(program_id,sire_id, tecode))):
				df_ranks = pd.concat([df_ranks, df_results2], axis=0 )

			te['te_bpdsy'] = util.calc_rank_average(df_ranks)		
			
			#print("bpdsy:",program_id, race_no, horse_id)
			ret = te
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret


	def _get_bpdjy_to_df(self, sr_re, tecode):
		ret = pd.DataFrame()
		try:
			start = time.time()
			program_id = sr_re['ph_id']
			year = sr_re['ph_year']
			md = sr_re['ph_monthday']
			horse_id = sr_re['rr_r_horse_id']	
			jocky_id = QueryFactory().get_jocky_id_to_df(horse_id, year, md)
			te ={}
			df_ranks = pd.DataFrame()
			if(len(df_results1 :=  QueryFactory().get_jocky_result_by_iste_all_to_df(program_id, jocky_id, tecode))):
				df_ranks = pd.concat([df_ranks, df_results1], axis=0 )

			if(len(df_results2 := QueryFactory().get_jocky_result_by_iste_still_id_to_df(program_id, jocky_id,tecode))):
				df_ranks = pd.concat([df_ranks, df_results2], axis=0 )
			te['te_bpdjy'] = util.calc_rank_average(df_ranks)		
			ret = te
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret


	def _get_bpdty_to_df(self, sr_re, tecode):
		ret = pd.DataFrame()
		try:
			start = time.time()
			program_id = sr_re['ph_id']
			horse_id = sr_re['rr_r_horse_id']
			trainer_id = QueryFactory().get_trainer_at_to_df_by_horse_id(horse_id)
			te ={}
		
			df_ranks = pd.DataFrame()
			if(len(df_results1 := QueryFactory().get_trainer_result_by_iste_all_to_df(program_id,trainer_id,tecode))):
				df_ranks = pd.concat([df_ranks, df_results1], axis=0 )

			if(len(df_results2 := QueryFactory().get_trainer_result_by_iste_still_id_to_df(program_id,trainer_id, tecode))):
				df_ranks = pd.concat([df_ranks, df_results2], axis=0 )
			te['te_bpdty'] = util.calc_rank_average(df_ranks)					
			ret = te
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def _get_c2_to_df(self, df_results):
		ret = pd.DataFrame()
		try:
			start = time.time()
			cls_codes_list = conf.code_group_2007_value
			te ={}	
			for cls in cls_codes_list:
				query ='''
					rh_te_c2_code == '{0}' 
				'''.format(int(cls))
				df_results2 = pd.DataFrame()
				if(len(df_results)):
					df_results2 = df_results.query(query, engine='python')
				te['te_C2_{0}'.format(cls)]  = util.calc_rank_average(df_results2)			
				
				ret = te
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	