
import pandas as pd
import model.utility.k_jra_util as util
from model.features.onehot_encoding.CategoryManager4 import CategoryManager4
from model.features.target_encoding.TargetManager3 import TargetManager3
from model.features.statistics_variables.SvManager2 import SvManager2
from model.data_createor.Pat009BaseDataCreator import Pat009BaseDataCreator
import os
import inspect
# AI教師データCSVファイル出力


class pat009TrainingDataCreator(Pat009BaseDataCreator):

	def __init__(self):
		super().__init__()

	def create(self, program_id, horse_id, prev_id1, prev_id2, prev_id3, prev_id4,  sr_pcs, to_onehot=True):
		ret = None
		try:
			# if(program_id == '2021082801' and  horse_id=='2016102556' and prev_id1=='2021052905'):
				# 		i=0
			# if(horse_id != '2019104023'):
			# 	return
			sr_pc = sr_pcs[horse_id]
			pb1 = self.__create_current_data_part(program_id, horse_id, sr_pc, to_onehot)
			if (pb1 is not None):
				pb2 = self._create_history_data_part2(
					program_id, prev_id1, horse_id, sr_pcs[prev_id1], 'p1', to_onehot)
				pb3 = self._create_history_data_part2(
					program_id, prev_id2, horse_id, sr_pcs[prev_id2], 'p2', to_onehot)
				pb4 = self._create_history_data_part2(
					program_id, prev_id3, horse_id, sr_pcs[prev_id3], 'p3', to_onehot)
				pb5 = self._create_history_data_part2(
					program_id, prev_id4, horse_id, sr_pcs[prev_id4], 'p4', to_onehot)
				ret = pd.concat([pb1, pb2, pb3, pb4, pb5])
				if (ret.isnull().sum()):
					ret = None
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

