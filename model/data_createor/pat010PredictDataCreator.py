
import pandas as pd
from model.features.onehot_encoding.CategoryManager4  import CategoryManager4
from model.features.target_encoding.TargetManager3 import TargetManager3
from model.features.statistics_variables.SvManager2 import SvManager2
from model.data_createor.Pat009BaseDataCreator import Pat009BaseDataCreator
import os
import inspect
# AI検証データ
class pat010PredictDataCreator(Pat009BaseDataCreator):

	def __init__(self):
		super().__init__()

	def create(self, program_id, horse_id, sr_re, prev_ids, sr_pcs):
		ret = None
		try:		
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

			pb1 = self.__create_current_data_part(program_id, horse_id, sr_re)
			pb2 = self._create_history_data_part2(program_id, prev_id1, horse_id, sr_pcs[prev_id1], 'p1')
			pb3 = self._create_history_data_part2(program_id, prev_id2, horse_id, sr_pcs[prev_id2], 'p2')
			pb4 = self._create_history_data_part2(program_id, prev_id3, horse_id, sr_pcs[prev_id3], 'p3')
			pb5 = self._create_history_data_part2(program_id, prev_id4, horse_id, sr_pcs[prev_id4], 'p4')
			pb6 = self._create_history_data_part2(program_id, sc_id1, horse_id, sr_pcs[sc_id1], 'sc1')
			pb7 = self._create_history_data_part2(program_id, sc_id2, horse_id, sr_pcs[sc_id2], 'sc2')
			pb8 = self._create_history_data_part2(program_id, sc_id3, horse_id, sr_pcs[sc_id3], 'sc3')
			pb9 = self._create_history_data_part2(program_id, sc_id4, horse_id, sr_pcs[sc_id4], 'sc4')
			ret = pd.concat([pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, pb9])
	
	
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def update(self, program_id, horse_id, sr_re):
		ret = None
		try:		
			ret = self.__create_current_hot_data_part(program_id, horse_id, sr_re)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret

	def __create_current_data_part(self, program_id, horse_id, sr_pc):
		ret = None
		try:		
			pb1 = self._create_header_block_data_from_rr(sr_pc)
			sr_cats = self._create_category_seed(sr_pc)
			sr_cats = CategoryManager4.to_cats(sr_cats)
			pb2 = CategoryManager4.to_onehot(sr_cats)
			pb3 = TargetManager3.to_feature(sr_pc)
			pb4 = SvManager2.to_sv(program_id, horse_id, sr_pc)
			ret =  pd.concat([pb1, pb2, pb3, pb4])
			#ret = df_temp.drop(['cat_plc_10','cat_plc_11'],axis=0)
		except Exception as e:	
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	

	def __create_current_hot_data_part(self,  program_id, horse_id, sr_pc):
		ret = None
		try:		
			
			sr_cats = self._create_category_hot_seed(sr_pc)
			sr_cats = CategoryManager4.to_cats_hot(sr_cats)
			pb1 = CategoryManager4.to_onehot_hot(sr_cats)
			pb2 = SvManager2.to_sv_hot(program_id, horse_id, sr_pc)
			ret =  pd.concat([pb1, pb2])
		except Exception as e:	
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret	