
import pandas as pd
import model.utility.k_jra_util as util
from model.features.onehot_encoding.CategoryManager4 import CategoryManager4
from model.features.target_encoding.TargetManager3 import TargetManager3
from model.features.statistics_variables.SvManager2 import SvManager2
from model.data_createor.Pat009BaseDataCreator import Pat009BaseDataCreator
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
import os
import inspect
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
# AI教師データCSVファイル出力


class pat014TrainingLgbmDataCreator(Pat009BaseDataCreator):

	def __init__(self):
		super().__init__()

	def create(self):
		ret = None
		try:
			pass
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def __create_current_data_part(self, program_id, horse_id, sr_pc, to_onehot=True):
		ret = None
		try:
			sr_current = sr_pc
			if ((sr_current is not None) and (False == sr_current.empty)):
				if (len(sr_current)):
					# 着順をカテゴライズ
					#sr_current = util.convert_rank_to_category9(sr_current)
					sr_current = util.convert_rank_to_category2(sr_current)
					
					# 特徴量データ部を抽出
					pb1 = self._create_header_block_data_from_pv(sr_current)
					if (True == to_onehot):
						pb2 = CategoryManager4.to_onehot(sr_current)
					else:
						pb2 = CategoryManager4.to_cats_direct(sr_current)
					pb3 = TargetManager3.to_feature(sr_current)
					pb4 = SvManager2.to_sv(program_id, horse_id, sr_current)
					ret = pd.concat([pb1, pb2, pb3, pb4])
					#ret = df_temp.drop(['cat_plc_10','cat_plc_11'], axis=1)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret


	def __create_history_feature_data_part(self, program_id, horse_id, col_key):
		ret = None
		try:
			sr_temp = QueryFactory().get_hv_one_by_ih_to_sr(program_id, horse_id)
			# if(0 == len(df_temp)):
			# 	dict_zero = {'his_l4_p1': 0, 'his_l4_p2': 0, 'his_l4_p3': 0, 'his_l4_p4': 0}
			# 	sr_temp = pd.Series(dict_zero)
			# else:
			# 	df_temp = df_temp.drop(columns=
			# 		['key_program_id','key_horse_id','desc_horse_no','desc_race_no','upd']
			# 	)
			# 	sr_temp=df_temp.iloc[0]
			ret = util.rename_index(sr_temp, col_key)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
	
	def __create_history_sc_feature_data_part(self, program_id, horse_id, col_key):
		ret = None
		try:
			sr_temp = QueryFactory().get_hv_one_by_ih_to_sr2(program_id, horse_id)
			# if(0 == len(df_temp)):
			# 	dict_zero = {'his_l4_p1': 0, 'his_l4_p2': 0, 'his_l4_p3': 0, 'his_l4_p4': 0}
			# 	sr_temp = pd.Series(dict_zero)
			# else:
			# 	df_temp = df_temp.drop(columns=
			# 		['key_program_id','key_horse_id','desc_horse_no','desc_race_no','upd']
			# 	)
			# 	sr_temp=df_temp.iloc[0]
			ret = util.rename_index(sr_temp, col_key)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def __create_history_feature_data_part(self, program_id, horse_id, col_key):
		ret = None
		try:
			sr_temp = QueryFactory().get_hv_one_by_ih_to_sr(program_id, horse_id)
			# if(0 == len(df_temp)):
			# 	dict_zero = {'his_l4_p1': 0, 'his_l4_p2': 0, 'his_l4_p3': 0, 'his_l4_p4': 0}
			# 	sr_temp = pd.Series(dict_zero)
			# else:
			# 	df_temp = df_temp.drop(columns=
			# 		['key_program_id','key_horse_id','desc_horse_no','desc_race_no','upd']
			# 	)
			# 	sr_temp=df_temp.iloc[0]
			ret = util.rename_index(sr_temp, col_key)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
	
	def __create_extra_l4_features_data_part(self, program_id, horse_id, col_key):
		ret = pd.Series()
		try:	
			sr_temp = QueryFactory().get_speed_exp_by_ph_to_sr(program_id, horse_id)
			if(len(sr_temp)):
				sr_temp.fillna(0.0, inplace=True)
			if( sr_temp.empty):
				sr_temp['sv_speed_exp'] =0.0
			ret = util.rename_index(sr_temp, col_key)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
