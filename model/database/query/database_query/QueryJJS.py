import pyodbc
import model.conf.KJraConst as const


def get_score_by_id_to_df(accessor, y, jockey_id):
	template = """
		select 
			*
		from 
			{0} 
		where
			js_year = '{1}'
			and
			js_id ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_JOCKEY_SCORE,
		y,
		jockey_id
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
			js_year ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_JOCKEY_SCORE,
		y
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_score_by_iy_to_df(accessor, jockey_id, y):
	template = """
		select 
			*
		from 
			{0} 
		where
			js_id ='{1}'
			and 
			js_year='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_JOCKEY_SCORE,
		jockey_id,
		y
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_average_value(accessor, y):
	template = """
		select 
			avg({0}.js_race_count) as js_race_count_avg,
			avg({0}.js_win_score) as js_win_score_avg,
			avg({0}.js_mul_score) as js_mul_score_avg,
			avg({0}.js_win_count) as js_win_count_avg,
			avg({0}.js_mul_count) as js_mul_count_avg
		from 
			{0} 
		where
			{0}.js_id <> '00000'
			and
			{0}.js_race_count > 10
			and
			{0}.js_year='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_JOCKEY_SCORE,
		y
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret
