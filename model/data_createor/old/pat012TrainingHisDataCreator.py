
import pandas as pd
import model.utility.k_jra_util as util
from model.features.onehot_encoding.CategoryManager4 import CategoryManager4
from model.features.target_encoding.TargetManager3 import TargetManager3
from model.features.statistics_variables.SvManager2 import SvManager2
from model.data_createor.Pat009BaseDataCreator import Pat009BaseDataCreator
import os
import inspect
# AI教師データCSVファイル出力


class pat012TrainingHisDataCreator(Pat009BaseDataCreator):

	def __init__(self):
		super().__init__()

	def create(self, program_id, horse_id, prev_ids, sr_pcs, to_onehot=True):
		ret = None
		try:
			sr_pc = sr_pcs[program_id]
			pb1 = self.__create_current_data_part(program_id, horse_id, sr_pc, to_onehot)
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
				pb2 = self._create_history_data_part2(
					program_id, prev_id1, horse_id, sr_pc, 'p1')
				pb3 = self._create_history_data_part2(
					program_id, prev_id2, horse_id, sr_pc, 'p2')
				pb4 = self._create_history_data_part2(
					program_id, prev_id3, horse_id, sr_pc, 'p3')
				pb5 = self._create_history_data_part2(
					program_id, prev_id4, horse_id, sr_pc, 'p4')
				
				pb6 = self._create_history_data_part2(
					program_id, sc_id1, horse_id, sr_pc, 'sc_p1')
				pb7 = self._create_history_data_part2(
					program_id, sc_id2, horse_id, sr_pc, 'sc_p2')
				pb8 = self._create_history_data_part2(
					program_id, sc_id3, horse_id, sr_pc, 'sc_p3')
				pb9 = self._create_history_data_part2(
					program_id, sc_id1, horse_id, sr_pc, 'sc_p4')
    
				ret = pd.concat([pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, pb9])
				if (ret.isnull().sum()):
					ret = None
				if(ret is None):
					a=0
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


