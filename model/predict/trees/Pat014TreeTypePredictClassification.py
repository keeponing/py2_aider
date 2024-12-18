import sys
sys.path.append(r"C:\Dev\py2")

import numpy as np
import pandas as pd
import os
import inspect
import pickle
import model.conf.KJraConfig as conf
import socket
import model.utility.k_jra_util as util
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
import model.database.query.database_query.QueryJRR as qjrr
import model.database.query.database_query.QueryJRH as qjrh
from model.database.drivers.driver_factory.DatabaseFactory import DatabaseFactory
from model.data_createor.lgbm.Pat014LgbmDataCreator2 import  Pat014LgbmDataCreator2
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
from sklearn.model_selection import train_test_split
from tqdm import trange
import lightgbm as lgb
from catboost import CatBoostClassifier


ALG_MODE_CAT = "cat"
ALG_MODE_LGBM = "lgb"
def create_train_data(place_code, track_code, distance_code):
	ret = 0
	try:
		def_dct = util.get_default_value()
		accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
		accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
		df_races = qjrh.get_race_at_by_ptd_to_df(accessor_acc, place_code, track_code, distance_code)
		#df_races = df_races[(df_races['ph_year'] > '2004') & (df_races['ph_year'] < '2024')]
		df_races = df_races[(df_races['ph_year'] > '2004') ]
		rec_list=[]
		for i in trange(len(df_races), desc=f'{place_code} {track_code} {distance_code}'):
			sr_race = df_races.iloc[i]
			program_id = sr_race['ph_id']
			y= sr_race['ph_year']
			md= sr_race['ph_monthday']
			race_no = sr_race['rh_race']
			distance = sr_race['rh_distance']
			tarck = sr_race['rh_track']

			df_horses =  QueryFactory().get_race_result_by_ir3(program_id, race_no )
			query = f"rr_r_rank<='08' and rr_r_rank!='00'"
			df_horses = df_horses.query(query, engine='python')
			for _, sr_horse in df_horses.iterrows():
				try:		
					element = create_element(accessor_acc, accessor_scr, program_id, y, place_code, distance, tarck, sr_race, sr_horse, def_dct)
					rec_list.append(element)
					# if(100 < len(rec_list)): #TODO
					# 	break	
				except Exception as e:
					print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
			# if(100 < len(rec_list)): #TODO
			# 	break
		df_train =  pd.DataFrame.from_records(rec_list)	
		df_train.fillna(0)
		file_name = conf.TREES_TRAIN_PTD_PATH_AT2.format(place_code, track_code ,distance_code)
		df_train.to_csv(file_name, index=False)
		ret = len(df_train)
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
	return ret

def create_train_data_sp(sp_code):
	ret = 0
	try:
		def_dct = util.get_default_value()
		accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
		accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
		df_races = qjrh.get_records_by_sp_code_to_df(accessor_acc, sp_code)
		df_races = df_races[(df_races['ph_year'] > '2004') & (df_races['ph_year'] < '2024')]
		rec_list=[]
		for i in trange(len(df_races), desc=f'{sp_code}'):
			sr_race = df_races.iloc[i]
			program_id = sr_race['ph_id']
			y= sr_race['ph_year']
			place_code = sr_race['ph_place']
			md= sr_race['ph_monthday']
			race_no = sr_race['rh_race']
			distance = sr_race['rh_distance']
			tarck = sr_race['rh_track']

			df_horses =  QueryFactory().get_race_result_by_ir3(program_id, race_no )
			for j, sr_horse in df_horses.iterrows():
				try:		
					element = create_element(accessor_acc, accessor_scr, program_id, y, place_code, distance, tarck, sr_race, sr_horse, def_dct)
					rec_list.append(element)
					# if(100 < len(rec_list)): #TODO
					# 	break	
				except Exception as e:
					print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
			# if(100 < len(rec_list)): #TODO
			# 	break
		df_train =  pd.DataFrame.from_records(rec_list)	
		df_train.fillna(0)
		file_name = conf.TREES_TRAIN_SP_PATH_AT2.format(sp_code)
		df_train.to_csv(file_name, index=False)
		ret = len(df_train)
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
	return ret

def create_predict_data(sr_rh):
	ret = pd.DataFrame()
	try:
		def_dct = util.get_default_value()
		accessor_acc = DatabaseFactory().get(DatabaseFactory.ACC_ACCESSOR)
		accessor_scr = DatabaseFactory().get(DatabaseFactory.SCR_ACCESSOR)
		program_id = sr_rh['rh_id']
		race_no = sr_rh['rh_race']
		rec_list=[]

		df_races = qjrh.get_program_and_race_at_by_ir_to_df(accessor_acc, program_id, race_no)
		for i in range(len(df_races)):
			sr_race = df_races.iloc[i]
			program_id = sr_race['ph_id']
			y= sr_race['ph_year']
			md= sr_race['ph_monthday']
			place_code = sr_race['ph_place']

			race_no = sr_race['rh_race']
			distance = sr_race['rh_distance']
			tarck = sr_race['rh_track']

			df_horses = qjrr.get_race_result_by_ir(accessor_acc, program_id, race_no )
			if(0 == len(df_horses)):
				continue
			for _, sr_horse in df_horses.iterrows():				
				element = create_element(accessor_acc, accessor_scr, program_id, y, place_code, distance, tarck, sr_race, sr_horse, def_dct)
				rec_list.append(element)
				
			
		ret = pd.DataFrame.from_records(rec_list)
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')			
	return ret

def do_training(place_code, track_code, distance_code, alg):
	try:
		file_name =  conf.TREES_TRAIN_PTD_PATH_AT2.format(place_code, track_code ,distance_code)

		model = do_training_model(file_name, alg)
		
		model_file = ""
		if(alg == ALG_MODE_LGBM):
			model_file = conf.LGBM_MODEL_PTD_PATH_AT2.format(place_code, track_code, distance_code)
		elif(alg ==ALG_MODE_CAT):
			model_file = conf.CAT_MODEL_PTD_PATH_AT2.format(place_code, track_code, distance_code)

		pickle.dump(model, open(model_file, 'wb'))
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {place_code},  {e}')	
		
def do_training_sp(sp_code, alg):
	try:
		file_name =  conf.TREES_TRAIN_SP_PATH_AT2.format(sp_code)

		model = do_training_model(file_name, alg)
		model_file = ""
		if(alg == ALG_MODE_LGBM):
			model_file = conf.LGBM_MODEL_SP_PATH_AT.format(sp_code)
		elif(alg ==ALG_MODE_CAT):
			model_file = conf.CAT_MODEL_SP_PATH_AT.format(sp_code)

		pickle.dump(model, open(model_file, 'wb'))
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def do_training_model(data_path, alg):
	ret = None
	try:
		df_train = pd.read_csv(data_path, dtype=str)
		df_train = df_train['00' < df_train['rr_r_rank'] ]

		df_train['rr_r_rank'] = df_train['rr_r_rank'].apply(lambda x: 1 if int(x) <= 3 else 0)
		creator = Pat014LgbmDataCreator2()
		df_train = creator.create2(df_train,  True)

		
		target_column = 'rr_r_rank'
		feature_columns = df_train.columns.to_list()[1:]
		#df_train.to_clipboard()
		# 訓練データとテストデータに分割
		X_train, X_test, y_train, y_test = train_test_split(
			df_train[feature_columns],
			df_train[target_column],
			test_size=0.2, random_state=42, stratify=df_train[target_column] )

		# LightGBMモデルを初期化
		model = None
		if(alg == ALG_MODE_LGBM):
			cat_list = creator.get_category_list2()
			model = lgb.LGBMClassifier(force_col_wise=True)
			# モデルをトレーニング
			model.fit(X_train, y_train, 
				categorical_feature = cat_list
				)
		elif(alg ==ALG_MODE_CAT):
			model = CatBoostClassifier(
				iterations=100, 
				depth=5, 
				learning_rate=0.1, 
				loss_function='Logloss',
				verbose= False)

			model.fit(X_train, y_train)

		# テストデータで予測
		y_pred = model.predict(X_test)

		# 分類レポートを表示
		accuracy = accuracy_score(y_test, y_pred)
		print(f"正解率: {accuracy:.2f}")	
		ret = model

	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	return ret

def predict_precision(df_input, place_code, sp_code, track_code, distance_code, alg):

	ret=[]
	try:
		feature_columns = util.get_feature_columns()
		program_id = df_input['rh_id'].iloc[0]
		race_no = df_input['rh_race'].iloc[0]
		df_condition = df_input[feature_columns]
		df_condition = util.to_le(df_condition, feature_columns)
	
		creator = Pat014LgbmDataCreator2()
		df_train = creator.create2(df_input, False)
		#util.dump_feature(df_train, f'prd_{program_id}_{race_no}_{track_code}_{distance_code}')
		if(alg == ALG_MODE_LGBM):
			filename = conf.LGBM_MODEL_SP_PATH_AT.format(sp_code)
			if(False == os.path.exists(filename)):	
				filename  = conf.LGBM_MODEL_PTD_PATH_AT2.format(place_code,  track_code, distance_code)
		elif(alg ==ALG_MODE_CAT):
			filename = conf.CAT_MODEL_SP_PATH_AT.format(sp_code)
			if(False == os.path.exists(filename)):	
				filename  = conf.CAT_MODEL_PTD_PATH_AT2.format(place_code,  track_code, distance_code)			
		#print('PTD Start ', program_id, race_no, filename)
		
		if(True == os.path.exists(filename)):	
			X_train = df_train
			model = pickle.load(open(filename, 'rb'))
			
			y_pred = model.predict_proba(X_train)
			score_list = [row[1] for row in y_pred]
			df_input['score'] = score_list
			ret.append("index,horse_no,rfu1,rfu2,predict1,program_id,horse_id,predict2")			
			for index, sr_horse in df_input.iterrows():
	
				#util.dump_feature(sr_horse, f"{sr_horse[f'rr_r_id']}_{sr_horse['rh_race']}_{sr_horse[f'rr_r_horse_id']}")
				pred_index = int(np.argmax(y_pred[index]))
				ret.append(r"{0},{1},{2},{3},{4:.4f},{5},{6},{7:.4f}".format(
					index,
					sr_horse[f'rr_r_horse_no'],
					pred_index,
					pred_index,
					sr_horse['score'],
					sr_horse[f'rr_r_id'],
					sr_horse[f'rr_r_horse_id'],
					sr_horse['score']
				))
		else:
			print(f'File Not found.{filename}')
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {place_code}, {sp_code},  {e}')	
	return ret

def create_element(accessor_acc, accessor_scr, program_id, y, place_code, distance, tarck, sr_race, sr_horse, def_dct):
	ret = pd.Series()
	try:
		horse_id = sr_horse['rr_r_horse_id']
		sire_id = sr_horse['rr_m_blood01']
		his_list = [
			sr_horse['rr_h_prev_id1'],
			sr_horse['rr_h_prev_id2'],
			sr_horse['rr_h_prev_id3'],
			sr_horse['rr_h_prev_id4']]
	
		sr_his = QueryFactory().create_his_exp_l4(accessor_acc, his_list, horse_id)
		sr_bs = QueryFactory().get_bs_by_sypdt_to_sr(accessor_scr, sire_id, y, place_code, distance, tarck)
		sr_hv = QueryFactory().get_hv_by_phid_to_sr(accessor_acc, program_id, horse_id)
		sr_sv = QueryFactory().get_sv_by_phid_to_sr(accessor_acc, program_id, horse_id)
		sr_te = QueryFactory().get_te_by_phid_to_sr(accessor_acc, program_id, horse_id)
		if(sr_his.empty or sr_bs.empty or sr_hv.empty or sr_sv.empty  or sr_te.empty ):
			print(f'Skip {horse_id} ')
		else:	
			sr_horse['rr_r_vote'] = sr_horse['rr_r_vote'].replace('**', def_dct['rr_r_vote'])
			sr_horse['rr_r_vote'] = sr_horse['rr_r_vote'].replace('--',  def_dct['rr_r_vote'])
			sr_horse['rr_r_odds'] = sr_horse['rr_r_odds'].replace('****',  def_dct['rr_r_odds'])
			sr_horse['rr_r_odds'] = sr_horse['rr_r_odds'].replace('----',  def_dct['rr_r_odds'])
			if 'upd' in sr_sv.index:del sr_sv['upd']
			if 'upd' in sr_te.index:del sr_te['upd']			
			ret = pd.concat([
				sr_race,
				sr_horse, 
				sr_sv,
				sr_hv,
				sr_te,
				sr_bs,
				sr_his
				], axis=0)

	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {place_code},  {e}')	
	return ret		

