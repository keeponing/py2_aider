import pyodbc
import model.conf.KJraConst as const
import pandas as pd


def get_all_record_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		order by 
			bs_win_score desc
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_score_by_sire_id_to_df(accessor, sire_id):
	template = """
		select 
			*
		from 
			{0} 
		where
			bs_id ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		sire_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_record_by_y_to_df(accessor, y):
	template = """
		select 
			*
		from 
			{0} 
		where
			bs_year ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		y
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_score_by_siypdt_to_sr(accessor, sire_id, y,p,d,t):
	ret = pd.Series()
	template = """
		select 
			*
		from 
			{0} 
		where	
				bs_id ='{1}' 
			and
				bs_year = '{2}'
			and 
				bs_place ='{3}'
			and
				bs_distance = '{4}'
			and 
				bs_track ='{5}' 
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		sire_id,
		y,p,d,t
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	else:
		ret = pd.Series(data={
			"bs_id": sire_id,
			"bs_year": y,
			"bs_place": p,
			"bs_distance": d,
			"bs_track": t,
			"bs_name": "",
			"bs_win_score": 0.0,
			"bs_mul_score": 0.0,
			"bs_race_count": 0,
			"bs_win_count": 0,
			"bs_mul_count": 0
		})

	return ret

def is_existed(accessor, bs):
	template = """
		select 
			count(*) 
		from 
			{0}
		where	
				bs_id ='{1}' 
			and
				bs_year = '{2}'
			and 
				bs_place ='{3}'
			and
				bs_distance = '{4}'
			and 
				bs_track ='{5}' 
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		bs['bs_id'],
		bs['bs_year'],
		bs['bs_place'],
		bs['bs_distance'],
		bs['bs_track']
		)
	accessor.execute(cmd)
	ret = False
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		if(0 != ret):
			ret = True
		break
	accessor.cur_close()

def get_all_sire_id_to_df(accessor):
	template = """
		select 
			distinct(bs_id)
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret
#=== old ============================================================
def is_existed2(accessor, bs_name):
	template = """
		select 
			*
		from  
			{0}
		where
				bs_name ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		bs_name
		)
	accessor.execute(cmd)
	ret = False
	for c in accessor.cur.fetchall():
		ret = True
		break
	accessor.cur_close()
	return ret


def get_sire_name_list_to_df(accessor):
	template = """
		select 
			distinct(bs_name)
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_sire_list_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_score_by_ypdt_to_df(accessor, y, p, d, t):
	template = """
		select 
			*
		from 
			{0} 
		where
				(bs_year = '{1}' or bs_year = '{2}')
			and 
				bs_place ='{3}'
			and
				bs_distance = '{4}'
			and 
				bs_track ='{5}' 
			and 
				bs_id <>'0000000000' 
			and 
				bs_name <>'' 
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		int(y), int(y)-1, p, d, t
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_average_value(accessor, y):
	template = """
		select 
			avg({0}.bs_win_score) as bs_win_score_avg,
			avg({0}.bs_mul_score) as bs_mul_score_avg,
			avg({0}.bs_race_count) as bs_race_count_avg,
			avg({0}.bs_win_count) as bs_win_count_avg,
			avg({0}.bs_mul_count) as bs_mul_count_avg
		from 
			{0} 
		where
			{0}.bs_id <> '0000000000'
			and
			{0}.bs_race_count > 10
			and
			{0}.bs_year='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_BLOOD_SCORE,
		y
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret
