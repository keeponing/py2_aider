
import inspect
import pandas as pd
import model.utility.k_jra_util as util
from model.features.onehot_encoding.CategoryManager4 import CategoryManager4
from model.features.target_encoding.TargetManager3 import TargetManager3
from model.features.statistics_variables.SvManager2 import SvManager2
from model.features.onehot_encoding.current.Cat001CPlc import Cat001CPlc
from model.features.onehot_encoding.current.Cat002VYear import Cat002VYear
from model.features.onehot_encoding.current.Cat003VMnt2 import Cat003VMnt2
from model.features.onehot_encoding.current.Cat004VEvtd import Cat004VEvtd
from model.features.onehot_encoding.current.Cat006VRpc import Cat006VRpc

from model.features.onehot_encoding.current.Cat104CWtr import Cat104CWtr
from model.features.onehot_encoding.current.Cat105CTrk2 import Cat105CTrk2
from model.features.onehot_encoding.current.Cat106CBct import Cat106CBct
from model.features.onehot_encoding.current.Cat107CBcd import Cat107CBcd
from model.features.onehot_encoding.current.Cat109CCat import Cat109CCat
from model.features.onehot_encoding.current.Cat110CCls2 import Cat110CCls2
from model.features.onehot_encoding.current.Cat111CCls3 import Cat111CCls3
from model.features.onehot_encoding.current.Cat112CCls4 import Cat112CCls4
from model.features.onehot_encoding.current.Cat113CCls5 import Cat113CCls5
from model.features.onehot_encoding.current.Cat114CClsY import Cat114CClsY
from model.features.onehot_encoding.current.Cat115CRule import Cat115CRule
from model.features.onehot_encoding.current.Cat116CRcnd import Cat116CRcnd
from model.features.onehot_encoding.current.Cat117BDst import Cat117BDst

from model.features.onehot_encoding.current.Cat119BHcnt import Cat119BHcnt
from model.features.onehot_encoding.current.Cat120CGrd import Cat120CGrd

from model.features.onehot_encoding.current.Cat205BHn import Cat205BHn
from model.features.onehot_encoding.current.Cat206BRnk import Cat206BRnk
from model.features.onehot_encoding.current.Cat207CFrm import Cat207CFrm
from model.features.onehot_encoding.current.Cat209CBlink import Cat209CBlink
from model.features.onehot_encoding.current.Cat210BOld import Cat210BOld
from model.features.onehot_encoding.current.Cat211CSex import Cat211CSex
from model.features.onehot_encoding.current.Cat215CJmrk import Cat215CJmrk
from model.features.onehot_encoding.current.Cat217CDiff import Cat217CDiff
from model.features.onehot_encoding.current.Cat218CDiff import Cat218CDiff
from model.features.onehot_encoding.current.Cat219CDiff import Cat219CDiff
from model.features.onehot_encoding.current.Cat222CPm import Cat222CPm
from model.features.onehot_encoding.current.Cat223BGal import Cat223BGal
from model.features.onehot_encoding.current.Cat226BVote import Cat226BVote
from model.features.onehot_encoding.current.Cat227BCnr import Cat227BCnr
from model.features.onehot_encoding.current.Cat228BCnr import Cat228BCnr
from model.features.onehot_encoding.current.Cat229BCnr import Cat229BCnr
from model.features.onehot_encoding.current.Cat230BCnr import Cat230BCnr
from model.features.onehot_encoding.current.Cat231CHsgn import Cat231CHsgn
from model.features.onehot_encoding.current.Cat232CVt import Cat232CVt
from model.features.onehot_encoding.current.Cat233CBlng import Cat233CBlng
from model.features.onehot_encoding.current.Cat262BRcnt import Cat262BRcnt
from model.features.onehot_encoding.current.Cat267VYD import Cat267VYD
from model.features.onehot_encoding.current.Cat268CErr import Cat268CErr
import os
import inspect
from model.database.drivers.driver_factory.QueryFactory import QueryFactory

class Pat009BaseDataCreator:

	def __init__(self):
		i = 0

	def _create_header_block_data_from_pv(self, input):
		ret = pd.Series()
		try:
			ret['key_program_id'] = ''
			ret['key_horse_id'] = ''
			ret['obj_rank'] = 0
			ret['desc_horse_no'] = 0
			if (input is not None):
				ret['key_program_id'] = input['key_program_id']
				ret['key_horse_id'] = input['key_horse_id']
				ret['obj_rank'] = input['obj_rank']
				ret['desc_horse_no'] =  f"{int(input['desc_horse_no']):02}"
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')

		return ret

	def _create_header_block_data_from_rr(self, input):
		ret = pd.Series()
		try:
			ret['key_program_id'] = ''
			ret['key_horse_id'] = ''
			ret['obj_rank'] = 0
			ret['desc_horse_no'] = 0

			if (input is not None):
				ret['key_program_id'] = input['ph_id']
				ret['key_horse_id'] = input['rr_r_horse_id']
				ret['obj_rank'] = input['rr_r_rank']
				ret['desc_horse_no'] = input['rr_r_horse_no']

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')

		return ret

	def _create_category_seed(self, sr_rr):
		ret = pd.Series()
		try:
			ret[Cat001CPlc.KEYS] = sr_rr['ph_place']  # 005
			ret[Cat002VYear.KEYS] = sr_rr['ph_year']  # 002
			ret[Cat003VMnt2.KEYS] = sr_rr['ph_monthday'][:2]  # 003
			ret[Cat004VEvtd.KEYS] = sr_rr['ph_count']  # 004
			ret[Cat006VRpc.KEYS] = sr_rr['ph_place_count']  # 006
			ret[Cat104CWtr.KEYS] = sr_rr['rh_weather']  # 104
			ret[Cat105CTrk2.KEYS] = sr_rr['rh_track']  # 105
			ret[Cat106CBct.KEYS] = sr_rr['rh_turf_condition']  # 106
			ret[Cat107CBcd.KEYS] = sr_rr['rh_dirt_condition']  # 107
			ret[Cat109CCat.KEYS] = sr_rr['rh_category']  # 109
			ret[Cat110CCls2.KEYS] = sr_rr['rh_class2']  # 110
			ret[Cat111CCls3.KEYS] = sr_rr['rh_class3']  # 111
			ret[Cat112CCls4.KEYS] = sr_rr['rh_class4']  # 112
			ret[Cat113CCls5.KEYS] = sr_rr['rh_class5over']  # 113
			ret[Cat114CClsY.KEYS] = sr_rr['rh_classYoung']  # 114
			ret[Cat115CRule.KEYS] = sr_rr['rh_rule']  # 115

			ret[Cat116CRcnd.KEYS] = sr_rr['rh_weight']  # 116
			ret[Cat117BDst.KEYS] = sr_rr['rh_distance']  # 117
			ret[Cat119BHcnt.KEYS] = sr_rr['rh_horse_count']  # 119
			ret[Cat120CGrd.KEYS] = sr_rr['rh_grade']  # 120
			ret[Cat205BHn.KEYS] = sr_rr['rr_r_horse_no']
			ret[Cat206BRnk.KEYS] = sr_rr['rr_r_rank']
			ret[Cat222CPm.KEYS] = sr_rr['rr_r_gal_sign']  # 222
			ret[Cat223BGal.KEYS] = sr_rr['rr_r_gal_val']  # 223
			ret[Cat226BVote.KEYS] = sr_rr['rr_r_vote']  # 226
			ret[Cat207CFrm.KEYS] = sr_rr['rr_r_waku']  # 207
			ret[Cat209CBlink.KEYS] = sr_rr['rr_r_blinker']  # 209
			ret[Cat210BOld.KEYS] = sr_rr['rr_r_age']  # 210
			ret[Cat211CSex.KEYS] = sr_rr['rr_r_gender']  # 211
			ret[Cat215CJmrk.KEYS] = sr_rr['rr_r_j_mark']  # 215
			# ret['cats_time'] = sr_rr['rr_r_time'] #216  目的変数除外
			ret[Cat217CDiff.KEYS] = sr_rr['rr_r_diff1']  # 217
			ret[Cat218CDiff.KEYS] = sr_rr['rr_r_diff2']  # 218
			ret[Cat219CDiff.KEYS] = sr_rr['rr_r_diff3']  # 219
			ret[Cat227BCnr.KEYS] = sr_rr['rr_r_corner1']  # 227
			ret[Cat228BCnr.KEYS] = sr_rr['rr_r_corner2']  # 228
			ret[Cat229BCnr.KEYS] = sr_rr['rr_r_corner3']  # 229
			ret[Cat230BCnr.KEYS] = sr_rr['rr_r_corner4']  # 230
			ret[Cat231CHsgn.KEYS] = sr_rr['rr_r_horse_sign']  # 231
			ret[Cat232CVt.KEYS] = sr_rr['rr_r_varieties']  # 232
			ret[Cat233CBlng.KEYS] = sr_rr['rr_r_belongs']  # 241　rr_m_jra_bilongs
			ret[Cat262BRcnt.KEYS] = sr_rr['rr_a_race_count']  # 262
			ret[Cat268CErr.KEYS] = sr_rr['rr_r_err']  # 268
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def _create_category_hot_seed(self, sr_rr):
		ret = pd.Series()
		try:

			ret[Cat104CWtr.KEYS] = sr_rr['rh_weather']  # 104
			ret[Cat106CBct.KEYS] = sr_rr['rh_turf_condition']  # 106
			ret[Cat107CBcd.KEYS] = sr_rr['rh_dirt_condition']  # 107
			ret[Cat222CPm.KEYS] = sr_rr['rr_r_gal_sign']  # 222
			ret[Cat223BGal.KEYS] = sr_rr['rr_r_gal_val']  # 223
			ret[Cat226BVote.KEYS] = sr_rr['rr_r_vote']  # 226

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
	def _create_history_data_part2(self, program_id, prev_id, horse_id, sr_pc, col_key,to_onehot=True):
		try:
			ret = None

			if ((sr_pc is not None) and (False == sr_pc.empty)):
				# df_history
				sr_pc[Cat206BRnk.KEYS] = int(sr_pc['obj_rank'])
				sr_pc[Cat267VYD.KEYS] = self._calc_year_diff(program_id, sr_pc)
				if (True == to_onehot):
					pb1 = CategoryManager4.to_onehot_of_history(sr_pc)
				else:
					pb1 = CategoryManager4.to_cats_direct_of_history(sr_pc)
				pb2 = TargetManager3.to_feature_of_history(sr_pc)
				pb3 = SvManager2.to_sv_of_history(prev_id, horse_id, sr_pc)
				ret = pd.concat([pb1, pb2, pb3])

				ret = util.rename_index(ret, col_key)
			else:
				sr_tr = self._create_void_history_training_data()

				ret = util.rename_index(sr_tr, col_key)
				#sr_train = pd.concat([sr_train, sr_tr])
				# sr_train.to_csv(r"c:\temp\sr_train.csv")
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def _create_void_history_training_data(self):
		ret = pd.Series()
		try:
			pb1 = CategoryManager4.create_zeros_of_history()
			pb2 = TargetManager3.create_zeros_of_history()
			pb3 = SvManager2.create_zeros_of_history()
			ret = pd.concat([pb1, pb2, pb3])
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')

		# util.save_dict_keys("create_void_training_data.txt",ret)
		return ret

	def _get_pv_data_at(self, program_id, horse_id):
		ret = pd.DataFrame()
		try:
			ret = QueryFactory().get_record_rank_non_zero(program_id, horse_id)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def _query_stock_by_ih(self, stock, program_id, horse_id):
		ret = None
		try:
			query = '''
				key_program_id == '{0}' and key_horse_id == '{1}' 
				'''.format(
					program_id,
					horse_id
				)
			ret = stock.query(query, engine='python')
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	def _calc_year_diff(self, progam_id, input):
		ret = 0
		try:
			from_year = int(progam_id[:4])
			to_year = int(input['key_program_id'][:4])
			ret = max(from_year - to_year, 0)
			ret = min(ret, 3)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
