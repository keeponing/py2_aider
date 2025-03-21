
import pandas as pd
import model.utility.k_jra_util as util
from model.features.onehot_encoding.CategoryManager4 import CategoryManager4
from model.features.target_encoding.TargetManager3 import TargetManager3
from model.features.statistics_variables.SvManager2 import SvManager2
from model.data_createor.Pat009BaseDataCreator import Pat009BaseDataCreator
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
import os
import inspect
# AI教師データCSVファイル出力


class pat013TrainingHisDataCreator(Pat009BaseDataCreator):

	def __init__(self):
		super().__init__()

	# def prepare(self, program_id, horse_id, rr):
	# 	ret = {}
	# 	try:
	# 		prev_id1 = rr['rr_h_prev_id1']
	# 		prev_id2 = rr['rr_h_prev_id2']
	# 		prev_id3 = rr['rr_h_prev_id3']
	# 		prev_id4 = rr['rr_h_prev_id4']
		
	# 		sc_id1 = rr['rr_h_sc_prev_id1']
	# 		sc_id2 = rr['rr_h_sc_prev_id2']
	# 		sc_id3 = rr['rr_h_sc_prev_id3']
	# 		sc_id4 = rr['rr_h_sc_prev_id4']

	# 		prev_ids={
	# 			'history_l4':[prev_id1, prev_id2,prev_id3, prev_id4],
	# 			'same_course':[sc_id1, sc_id2,sc_id3, sc_id4],
	# 		}

	# 		sr_current = QueryFactory().get_record_to_sr(program_id, horse_id)
			
	# 		ret[program_id] = sr_current
	# 	except Exception as e:
	# 		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
	# 	return ret, prev_ids

	def create(self, program_id, horse_id, prev_ids,  to_onehot=True):
		ret = None
		try:

			
			pb1 = self.__create_current_data_part(program_id, horse_id, to_onehot)
			if (pb1 is not None):
				hisl4_id = prev_ids['history_l4']
				samecourse_id = prev_ids['same_course']
				prev_id1 = hisl4_id[0]
				prev_id2 = hisl4_id[1]
				prev_id3 = hisl4_id[2]
				prev_id4 = hisl4_id[3]

				sc_id1 = samecourse_id[0]
				sc_id2 = samecourse_id[1]
				sc_id3 = samecourse_id[2]
				sc_id4 = samecourse_id[3]
				pb2 = self.__create_history_feature_data_part(
					prev_id1, horse_id, 'p1')
				pb3 = self.__create_history_feature_data_part(
					prev_id2, horse_id, 'p2')
				pb4 = self.__create_history_feature_data_part(
					prev_id3, horse_id, 'p3')
				pb5 = self.__create_history_feature_data_part(
					prev_id4, horse_id, 'p4')
				
				pb6 = self.__create_history_sc_feature_data_part(
					sc_id1, horse_id, 'sc_p1')
				pb7 = self.__create_history_sc_feature_data_part(
					sc_id2, horse_id, 'sc_p2')
				pb8 = self.__create_history_sc_feature_data_part(
					sc_id3, horse_id, 'sc_p3')
				pb9 = self.__create_history_sc_feature_data_part(
					sc_id4, horse_id, 'sc_p4')
    
				pb10 = self.__create_extra_l4_features_data_part(
					prev_id1, horse_id, 'p1')
				pb11 = self.__create_extra_l4_features_data_part(
					prev_id2, horse_id, 'p2')
				pb12 = self.__create_extra_l4_features_data_part(
					prev_id3, horse_id, 'p3')
				pb13 = self.__create_extra_l4_features_data_part(
					prev_id4, horse_id, 'p4')
				
				pb14 = self.__create_extra_l4_features_data_part(
					sc_id1, horse_id, 'sc_p1')
				pb15 = self.__create_extra_l4_features_data_part(
					sc_id2, horse_id, 'sc_p2')
				pb16 = self.__create_extra_l4_features_data_part(
					sc_id3, horse_id, 'sc_p3')
				pb17 = self.__create_extra_l4_features_data_part(
					sc_id4, horse_id, 'sc_p4')					
				ret = pd.concat([pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, pb9,
		     		pb10, pb11, pb12, pb13, pb14, pb15, pb16, pb17
			 	])
				if (ret.isnull().sum()):
					ret = None
				if(ret is None):
					print(f" {program_id}  {horse_id} {len(ret)}" )
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def __create_current_data_part(self, program_id, horse_id, to_onehot=True):
		ret = None
		try:
			sr_current = QueryFactory().get_record_to_sr(program_id, horse_id)
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
			ret = util.rename_index(sr_temp, col_key)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
	
	def __create_history_sc_feature_data_part(self, program_id, horse_id,  col_key):
		ret = None
		try:

			sr_temp = QueryFactory().get_hv_one_by_ih_to_sr2(program_id, horse_id)
			ret = util.rename_index(sr_temp, col_key)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def __create_history_feature_data_part(self, program_id, horse_id, col_key):
		ret = None
		try:  
			sr_temp = QueryFactory().get_hv_one_by_ih_to_sr(program_id, horse_id)
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
			if(sr_temp.empty):
				sr_temp =  pd.Series([0.0], index=['sv_speed_exp']) 

			ret = util.rename_index(sr_temp, col_key)	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
