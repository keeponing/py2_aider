#ユーティリティ
import os
import datetime
import pandas as pd
import model.database.query.database_query2.Query_S_RACE as qsrace
import model.database.query.database_query2.Query_N_RACE as qnrace
import model.database.query.database_query2.Query_N_UMA as qnuma
import model.database.query.database_query2.Query_S_UMA_RACE as qsumarace
import model.database.query.database_query2.Query_N_UMA_RACE as qnumarace
from model.database.drivers.mdb_driver.MdbAccessor import MdbAccessor
import model.conf.KJraConfig as conf
import model.database.query.database_query.QueryJPV2 as qjpv
import model.database.query.database_query.QueryJTE as qjte
import model.database.query.database_query.QueryJSV as qjsv
import model.database.query.database_query.QueryJCACHE as qjcache
import model.database.query.database_query.QueryJRE as qjre
import model.database.query.database_query.QueryJRH as qjrh
import inspect
import model.conf.TargetPlace as tplace
from model.database.drivers.driver_factory.DatabaseFactory import DatabaseFactory
def get_qrace_by_mode(mode):
	ret = qsrace
	if(mode == "N_MODE"):
		ret = qnrace
	return ret

def get_qumarace_by_mode(mode):
	ret = qsumarace
	if(mode == "N_MODE"):
		ret = qnumarace
	return ret

# 予測フォルダ作成
def create_folder(path):
	try:
		if False == os.path.exists(path):
			os.mkdir(path) 
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

def get_target_all_today_race( ):
	ret = pd.DataFrame()
	try:
		ret = get_target_race( hour_offset_from=-1, hour_offset_to=18, day_offset=1, mode='N')
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret	  
#指定帯域のレース情報を取得
def get_target_race( hour_offset_from=-1, hour_offset_to=1, day_offset=1, mode='N'):
	ret = pd.DataFrame()
	try:
		accessor_sql = DatabaseFactory().get(DatabaseFactory.SQL_ACCESSOR)
		today1 = datetime.datetime.now() 
		today2 =  today1 + datetime.timedelta(hours=hour_offset_from)
		today3 = today1 + datetime.timedelta(hours=hour_offset_to)
		tomorrow = today1 + datetime.timedelta(days=day_offset)
		year = today1.year
		month1 = today1.month
		month2 = tomorrow.month
		day1 = today1.day 
		day2 = tomorrow.day 
		
		h1 = today2.hour
		m1 = today2.minute
		h2 = today3.hour
		m2 = today3.minute
		hm1= "{:02}{:02}".format(h1, m1)
		hm2= "{:02}{:02}".format(h2, m2)
		
		
		md1 = "{:02}{:02}".format(month1, day1)
		md2 = "{:02}{:02}".format(month2, day2)
		
		qrace = None
		if('N'== mode):
			qrace = qnrace
		elif('S'==mode):
			qrace = qsrace
		if(int(h1) < 16):
			ret = qrace.get_current_race_until_today_to_df(accessor_sql, year, md1, hm1, hm2)
		if(0 == len(ret)):
			ret = qrace.get_current_race_until_tomorrow_to_df(accessor_sql,year, md2)
		if(0 == len(ret)):
			ret = qrace.get_latest_top_n_to_df(accessor_sql, 36)
		#ret =qrace.get_race_by_makedate_to_df(accessor_sql, '20230105')
		#ret =qrace.get_race_to_df(accessor_sql)
		#ret =qrace.get_race_by_year_to_df(accessor_sql, 2019)
		#ret =qrace.get_current_race_until_tomorrow_to_df(accessor_sql, 2021, 1218)
		#ret = qrace.sample(frac=1)
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret


#指定帯域のレース情報を取得
def get_target_race2(hour_offset_from=-1, hour_offset_to=1, day_offset=1):
	ret = pd.DataFrame()
	try:
		accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
		today1 = datetime.datetime.now() 
		today2 =  today1 + datetime.timedelta(hours=hour_offset_from)
		today3 = today1 + datetime.timedelta(hours=hour_offset_to)
		tomorrow = today1 + datetime.timedelta(days=day_offset)
		year = today1.year
		month1 = today1.month
		month2 = tomorrow.month
		day1 = today1.day 
		day2 = tomorrow.day 
		
		h1 = today2.hour
		m1 = today2.minute
		h2 = today3.hour
		m2 = today3.minute
		hm1= "{:02}{:02}".format(h1, m1)
		hm2= "{:02}{:02}".format(h2, m2)
		
		
		md1 = "{:02}{:02}".format(month1, day1)
		md2 = "{:02}{:02}".format(month2, day2)
		
		if(int(h1) < 16):
			ret = qjrh.get_current_race_until_today_to_df(accessor_acc, year, md1, hm1, hm2)
		if(0 == len(ret)):
			ret = qjrh.get_current_race_until_tomorrow_to_df(accessor_acc,year, md2)
		if(0 == len(ret)):
			ret = qjrh.get_latest_top_n_to_df(accessor_acc, 36)
		#ret = qjrh.get_race_header_by_id(accessor_acc, '2024032406')
		#ret =qrace.get_race_by_makedate_to_df(accessor_sql, '20230105')
		#ret =qrace.get_race_to_df(accessor_sql)
		#ret =qrace.get_race_by_year_to_df(accessor_sql, 2019)
		#ret =qrace.get_current_race_until_tomorrow_to_df(accessor_sql, 2021, 1218)
		#ret = qrace.sample(frac=1)
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

# def stock_pv(years):
# 	ret={}
# 	try:
# 		for y in range(len(years)):
# 			year = years[y]
# 			accessor = MdbAccessor()
# 			mdb = conf.KJDB_PREDICT_MDB_FILE.format(year)
# 			accessor.open(mdb)	
# 			ret[str(year)] = qjpv.get_record_all_to_df(accessor)
# 			accessor.close()
# 	except Exception as e: 
# 		print('k_predict_util.stock_pv:{}'.format(e) )		
# 	return ret

def stock_pv2(years):
	ret={}
	try:
		for y in range(len(years)):
			year = years[y]
			accessor = MdbAccessor()
			mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(year)
			accessor.open(mdb)	
			ret[year] = qjpv.get_record_all_to_df(accessor)
			accessor.close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

def stock_pv3(years):
	ret_pv={}
	ret_sv={}
	ret_te={}
	try:
		for y in range(len(years)):
			year = years[y]
			accessor = MdbAccessor()
			mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(year)
			accessor.open(mdb)	
			ret_pv[year] = qjpv.get_record_all_to_df(accessor)
			ret_sv[year] = qjsv.get_record_all_to_df(accessor)
			ret_te[year] = qjte.get_record_all_to_df(accessor)
			accessor.close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret_pv, ret_sv, ret_te

def stock_te(years):
	ret={}
	try:
		for y in range(len(years)):
			year = years[y]
			accessor = MdbAccessor()
			mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(year)
			accessor.open(mdb)	
			ret[year] = qjte.get_record_all_to_df(accessor)
			accessor.close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret


def stock_sv(years):
	ret={}
	try:
		for y in range(len(years)):
			year = years[y]
			accessor = MdbAccessor()
			mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(year)
			accessor.open(mdb)	
			df = qjsv.get_record_all_to_df(accessor)
			ret[year] =df
			accessor.close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

def stock_te2():
	ret={}
	try:
		years = range(2000, 2021)
		for y in range(len(years)):
			year = years[y]
			accessor = MdbAccessor()
			mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(year)
			accessor.open(mdb)	
			df = qjte.get_record_all_to_df(accessor)
			ret[year] =df
			accessor.close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret


def stock_sv2():
	ret={}
	try:
		years = range(2000, 2021)
		for y in range(len(years)):
			year = years[y]
			accessor = MdbAccessor()
			mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(year)
			accessor.open(mdb)	
			ret[year] = qjsv.get_record_all_to_df(accessor)
			accessor.close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret


def stock_cache(years):
	ret={}
	try:
		for y in range(len(years)):
			year = years[y]
			accessor = MdbAccessor()
			mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(year)
			accessor.open(mdb)	
			ret[year] = qjcache.get_record_all_to_df(accessor)
			accessor.close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

def get_acc(accessor_acc, program_id, horse_id, ad_year):
	ret = pd.DataFrame()
	try:
			ret = qjre.get_prev_race_results_by_ihi_to_df(accessor_acc, program_id, horse_id, ad_year)
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
	return ret	



def get_nnc_p_file_at(place_code, class_code):
	ret = ''
	try:
		predict_file = os.path.join(
					conf.NNC_MODELS_PLACE_AND_CLASS_FOLDER,
					rf'kjvan_model_cls_p_{place_code}_{class_code}.nnp'
		)
		if(False == os.path.isfile(predict_file)):
			ret = os.path.join(
				conf.NNC_MODELS_FOLDER,
		      	"kjvan_model_cls_p.nnp"
			)
		else:
			ret = predict_file
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	return ret


def get_nnc_r_file_at(place_code, class_code):
	ret = ''
	try:
		predict_file = os.path.join(
					conf.NNC_MODELS_PLACE_AND_CLASS_FOLDER,
					rf'kjvan_model_cls_r_{place_code}_{class_code}.nnp'
		)
		if(False == os.path.isfile(predict_file)):
			ret = os.path.join(
				conf.NNC_MODELS_FOLDER,
		      	"kjvan_model_cls_r.nnp"
			)
		else:
			ret = predict_file
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	return ret

def extract_jra_only(df_src, key):
	ret = pd.DataFrame()
	try:
	
		#print(len(df_results))
		ret = df_src[df_src[key].isin(tplace.g_place_code)]
		#print(len(df_results))
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	return ret

def get_from_active_duty_year(accessor_sql):
	ret = 0
	try:
		horse_id = qnuma.get_oldest_horse_id_active_duty(accessor_sql)
		ret = int(horse_id[:4])+2
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	return ret
	
def update_active_duty_year(accessor_sql):
	ret = ""
	try:
		y = get_from_active_duty_year(accessor_sql)
		path = os.path.join(conf.ATTR_PARAM_FOLDER, conf.ACTIVE_DUTY_FILE)
		with open(path, mode='w') as f:
			f.write(str(y))
		ret = str(y)
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	return ret

def get_active_duty_year():
	ret = 2000
	try:
		path = os.path.join(conf.ATTR_PARAM_FOLDER, conf.ACTIVE_DUTY_FILE)
		with open(path, mode='r') as f:
			ret = int(f.read())
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	return ret