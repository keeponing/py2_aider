import model.conf.KJraConst as const
import pandas as pd

# #特徴量データ

#IDと一致するレコードを取得する。
def get_record_all_to_df(accessor):
	template = """
		select
			* 
		from 
			{0} 
		order by 
			{0}.key_program_id
		"""
	cmd = template.format(
		const.TBL_KJDB_PREDICT_CACHE_VALIABLE
		)
	ret = accessor.read_sql_with_outlier(cmd)
	return ret  


def get_pv_to_sr(accessor, program_id, horse_id, is_direct=False):
	y = program_id[:4]
	if(False == is_direct):
		mdb = const.TBL_KJDB_PREDICT_CACHE_VALIABLE_AT.format(y)
	else:
		mdb = const.TBL_KJDB_PREDICT_CACHE_VALIABLE
	template = """
		select 
			*
		from 
			{0} 
		where
			key_program_id='{1}'
			and
			key_horse_id ='{2}'

		"""
	cmd = template.format(
		mdb,
		program_id,
		horse_id
		)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = pd.Series()
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret

#データ取得
def get_record_rank_non_zero_to_df(accessor, program_id, horse_id):
	template = """
		select
			* 
		from 
			{0} 
		where 
				key_program_id='{1}' 
			and 
				key_horse_id='{2}'
			and
				obj_rank <>0
		"""
	cmd = template.format(const.TBL_KJDB_PREDICT_CACHE_VALIABLE, program_id, horse_id)
	ret = accessor.read_sql_with_outlier(cmd)
	return ret  


#データが存在するか
def is_existed(accessor, id, horse_id):
	template = """
		select
			count(*) 
		from 
			{0} 
		where 
				key_program_id='{1}' 
			and 
				key_horse_id='{2}' 
		"""
	cmd = template.format(const.TBL_KJDB_PREDICT_CACHE_VALIABLE, id, horse_id)
	accessor.execute(cmd)
	ret =False
	total_count = 0
	for c in accessor.cur.fetchall():
		total_count = int(c[0])
		if(total_count != 0):
			ret = True
		break
	accessor.cur_close()
	return ret

#データが存在するか
def is_upd_zero(accessor, id, horse_id):
	template = """
		select
			count(*) 
		from 
			{0} 
		where 
				key_program_id='{1}' 
			and 
				key_horse_id='{2}'
			and
				upd =0 
		"""
	cmd = template.format(const.TBL_KJDB_PREDICT_CACHE_VALIABLE, id, horse_id)
	accessor.execute(cmd)
	ret =False
	total_count = 0
	for c in accessor.cur.fetchall():
		total_count = int(c[0])
		if(total_count != 0):
			ret = True
		break
	accessor.cur_close()
	return ret

#IDと一致するレコードを取得する。
def get_pv_by_h_to_df(accessor, horse_id):
	template = """
		select
			* 
		from 
			{0} 
		where 
			{0}.key_horse_id='{1}'
		order by 
			{0}.key_program_id
		"""
	cmd = template.format(
		const.TBL_KJDB_PREDICT_CACHE_VALIABLE,
		horse_id)
	ret = accessor.read_sql_with_outlier(cmd)
	return ret  


