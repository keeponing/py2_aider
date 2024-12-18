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
			{0}.bt_year 
		"""
	cmd = template.format(
		const.TBL_KJDB_BASE_TIME,
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_record_by_ypdt_to_sr(accessor, y, p, d, t):
	ret = pd.Series()
	template = """
		select
			 {0}.*
		from 
            {0}
		where 
			{0}.bt_year ='{1}'
			and
			{0}.bt_place='{2}'
			and
			{0}.bt_distance='{3}'
			and
			{0}.bt_track_cd='{4}'
		"""
	cmd = template.format(
		const.TBL_KJDB_BASE_TIME,
		y, 
		p, 
		d, 
		t
		)
	df_temp  = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret  


def get_upd(accessor, y,  p, d, t):
	ret = 0
	template = """
		select 
			{0}.upd
		from 
			{0} 
		where 
			{0}.bt_year ='{1}'
			and
			{0}.bt_place='{2}'
			and
			{0}.bt_distance='{3}'
			and
			{0}.bt_track_cd='{4}'
		"""
	cmd = template.format(
		const.TBL_KJDB_BASE_TIME,
		y, 
		p, 
		d, 
		t
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(0 != len(df_temp)):
		sr_temp = df_temp.iloc[0]
		ret = sr_temp['upd']
	return ret


def get_record_by_pdt_to_df(accessor,  p, d, t):
	template = """
		select
			 {0}.*
		from 
            {0}
		where 
			{0}.bt_place='{1}'
			and
			{0}.bt_distance='{2}'
			and
			{0}.bt_track_cd='{3}'
		"""
	cmd = template.format(
		const.TBL_KJDB_BASE_TIME,
		p, 
		d, 
		t
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret  
