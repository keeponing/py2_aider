import pyodbc
import model.conf.KJraConst as const
import pandas as pd

#IDと一致するレコードを取得する。
def get_record_all_to_df(accessor):
	template = """
		select
			 {0}.*
		from 
            {0}
		order by 
			{0}.at_year 
		"""
	cmd = template.format(
		const.TBL_KJDB_AVERAGE_TIME_MAIDEN_RACE,
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_record_by_ypdt_to_sr(accessor, y, p, t, d):
	ret = pd.Series()
	template = """
		select
			 {0}.*
		from 
            {0}
		where 
			{0}.at_year ='{1}'
			and
			{0}.at_place='{2}'
			and
			{0}.at_distance='{3}'
			and
			{0}.at_track_cd='{4}'
		"""
	cmd = template.format(
		const.TBL_KJDB_AVERAGE_TIME_MAIDEN_RACE,
		y, 
		p, 
		d, 
		t
		)
	df_temp  = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret  

