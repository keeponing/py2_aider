
import inspect
import pandas as pd

import os
import inspect
from model.features.format.concrete.SimpleFormatter import SimpleFormatter
from model.features.format.concrete.LabelConvFormatter import LabelConvFormatter
from model.features.format.FeatureFormatter import FeatureFormatter
from model.database.drivers.driver_factory.QueryFactory import QueryFactory

class Pat014LgbmDataCreator:

	def __init__(self):
		pass
	
	def get_category_list():
		return 	[
				'rr_r_j_id', 
				'rr_r_t_id',
				#'rr_r_o_id'
				]	
	
	def create(self, df_cache, is_train = True):
		ret = None
		try:
			formatter = self.prepare(is_train)
			
			series_list= []
			for i in range(len(df_cache)):
				sr_re = df_cache.iloc[i]
				try:
					if(is_train == True):
						formatter['rr_r_rank'].val = int(sr_re['rr_r_rank'])

					formatter['rh_cnd_hash256'].val = sr_re['rh_cnd_hash256']
					formatter['rr_r_vote'].val = float(sr_re['rr_r_vote'])
					formatter['rr_r_odds'].val = float(sr_re['rr_r_odds'])
					formatter['rr_r_j_id'].val = sr_re['rr_r_j_id']
					formatter['rr_r_t_id'].val = sr_re['rr_r_t_id']
					formatter['rr_r_o_id'].val = sr_re['rr_r_o_id']

					formatter['his0_speed_exp'].val = float(sr_re['his0_speed_exp'])
					formatter['his1_speed_exp'].val = float(sr_re['his1_speed_exp'])
					formatter['his2_speed_exp'].val = float(sr_re['his2_speed_exp'])
					formatter['his3_speed_exp'].val = float(sr_re['his3_speed_exp'])
					formatter['bs_win_score'].val = float(sr_re['bs_win_score'])
					formatter['bs_mul_score'].val = float(sr_re['bs_mul_score'])
					formatter['his_sc_l4_p1'].val = float(sr_re['his_sc_l4_p1'])
					formatter['his_sc_l4_p2'].val = float(sr_re['his_sc_l4_p2'])
					formatter['his_sc_l4_p3'].val = float(sr_re['his_sc_l4_p3'])
					formatter['his_sc_l4_p4'].val = float(sr_re['his_sc_l4_p4'])
					formatter['his_l4_p1'].val = float(sr_re['his_l4_p1'])
					formatter['his_l4_p2'].val = float(sr_re['his_l4_p2'])
					formatter['his_l4_p3'].val = float(sr_re['his_l4_p3'])
					formatter['his_l4_p4'].val = float(sr_re['his_l4_p4'])
					series_list.append(formatter.doit())
					formatter.clear_val()
				except Exception as e:
					print(sr_re['rr_r_id'], sr_re['rr_r_horse_id'])
					print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
				formatter.clear_val()
			ret = pd.DataFrame.from_records(series_list)


		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
		
	def prepare(self, is_train):
		t_id_categories, j_id_categories, o_id_categories, place_id_list, race_hash256_list = QueryFactory().get_categories()
		formatter = FeatureFormatter()
		if(is_train == True):
				formatter['rr_r_rank'] = SimpleFormatter('rr_r_rank')
		formatter['rh_cnd_hash256']= LabelConvFormatter('rh_cnd_hash256', race_hash256_list)
		formatter['rr_r_vote'] = SimpleFormatter('rr_r_vote')
		formatter['rr_r_odds'] = SimpleFormatter('rr_r_odds')
		formatter['rr_r_t_id'] = LabelConvFormatter('rr_r_t_id', t_id_categories)
		formatter['rr_r_j_id'] = LabelConvFormatter('rr_r_j_id', j_id_categories)
		formatter['rr_r_o_id'] = LabelConvFormatter('rr_r_o_id', o_id_categories)
		formatter['his0_speed_exp'] = SimpleFormatter('his0_speed_exp')
		formatter['his1_speed_exp'] = SimpleFormatter('his1_speed_exp')
		formatter['his2_speed_exp'] = SimpleFormatter('his2_speed_exp')
		formatter['his3_speed_exp'] = SimpleFormatter('his3_speed_exp')
		formatter['bs_win_score'] = SimpleFormatter('bs_win_score') 
		formatter['bs_mul_score'] = SimpleFormatter('bs_mul_score')
		formatter['his_sc_l4_p1'] = SimpleFormatter('his_sc_l4_p1')
		formatter['his_sc_l4_p2'] = SimpleFormatter('his_sc_l4_p2')
		formatter['his_sc_l4_p3'] = SimpleFormatter('his_sc_l4_p3')
		formatter['his_sc_l4_p4'] = SimpleFormatter('his_sc_l4_p4')
		formatter['his_l4_p1'] = SimpleFormatter('his_l4_p1')
		formatter['his_l4_p2'] = SimpleFormatter('his_l4_p2')
		formatter['his_l4_p3'] = SimpleFormatter('his_l4_p3')
		formatter['his_l4_p4'] = SimpleFormatter('his_l4_p4')
		ret = formatter
		return ret
