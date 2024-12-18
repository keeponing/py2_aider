import inspect
import sys
sys.path.append(r"C:\Dev\py2")
import model.database.query.database_query2.Query_N_RACE as qnrace
import model.database.query.database_query2.Query_S_RACE as qsrace
import model.database.query.database_query.UpsertJRH as ujrh
import model.database.query.database_query.UpsertJPV2 as ujpv
import model.database.query.database_query.UpsertJSV as ujsv
import model.database.query.database_query.UpsertJTE as ujte
import pandas as pd
import model.conf.KJraConst as const
from model.database.drivers.driver_factory.DatabaseFactory import DatabaseFactory
import time
import os
import model.utility.k_jra_util as util
from model.data_createor.Pat009PvdbDataCreator import Pat009PvdbDataCreator
import datetime
#クエリファクトリ
class UpsertFactory:

	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "_instance"):
			cls._instance = super(UpsertFactory, cls).__new__(cls)
		return cls._instance
	  
	def __init__(self):
		pass
	
	def upsert_bpd_tecode(self, program_id, race_no):
		ret =""
		try:
			start = time.time()
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)

			df_tecode = qnrace.get_tecode_bpd_to_df(accessor_sql, program_id, race_no)
			if(len(df_tecode) ):
				dt_tecode =df_tecode.iloc[0]
				tecode = dt_tecode['TeBPDCode']
				
				ujrh.upsert_bpd_tecode(accessor_acc, program_id, race_no, tecode)
				ret = tecode
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	

	def upsert_bd_tecode(self, program_id,  race_no):
		ret =""
		try:
			start = time.time()
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)

			te ={}
			te['te_id'] = program_id
			te['te_race'] = race_no
			df_tecode = qnrace.get_tecode_bd_to_df(accessor_sql, program_id, race_no)
			if(len(df_tecode) ):
				dt_tecode =df_tecode.iloc[0]
				tecode = dt_tecode['TeBDCode']
			
				ujrh.upsert_bd_tecode(accessor_acc, program_id, race_no, tecode)
				ret =tecode
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	
	def upsert_c_tecode(self, program_id,race_no):
		ret = ""
		try:
			start = time.time()
		
			accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
			accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)

			df_tecode = qnrace.get_tecode_c_to_df(accessor_sql, program_id, race_no)
			te ={}
			te['te_id'] = program_id
			te['te_race'] = race_no
			if(len(df_tecode) ):
				dt_tecode =df_tecode.iloc[0]
				tecode = dt_tecode['TeCCode']
				tecode2 = util.convert_2007_index_summary(tecode)
				ujrh.upsert_c_tecode2(accessor_acc, program_id, race_no, tecode, tecode2)
				ret = tecode
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	
	def upsert_pv(self, sr_re):
		try:
			start = time.time()
			program_id = sr_re['ph_id']
			horse_id = sr_re['rr_r_horse_id']
			y = sr_re['ph_year']
			creator = Pat009PvdbDataCreator()
			dct = creator.create_pv(program_id, horse_id, sr_re)

			dct['upd'] = 1
			accessor_pv = DatabaseFactory().get(DatabaseFactory.PV_ACCESSOR2, int(y))
			ujpv.upsert(accessor_pv, dct)  
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		
	def upsert_sv(self, sr_re, sr_race, df_re, ad_year):  
		try: 
			start = time.time()
			y = sr_re['ph_year']
			accessor_pv = DatabaseFactory().get(DatabaseFactory.PV_ACCESSOR2, int(y))
			creator = Pat009PvdbDataCreator()
			dct = creator.create_sv(sr_race, sr_re, df_re,  ad_year)
			dct['upd'] = 1
			if(0 != len(dct)):
				ujsv.upsert(accessor_pv, dct)	
			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	def upsert_te(self,sr_re,te_code_bpd,df_re):
					
		try:	
			start = time.time()
			
			y = sr_re['ph_year']
			accessor_pv = DatabaseFactory().get(DatabaseFactory.PV_ACCESSOR2, int(y))
			creator = Pat009PvdbDataCreator()			
			dct = creator.create_te(sr_re, df_re, te_code_bpd)
			ujte.upsert(accessor_pv, dct)

			#util.dump_span_time(inspect.currentframe().f_code.co_name, time.time() - start)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

