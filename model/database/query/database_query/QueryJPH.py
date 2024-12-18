import datetime
import pandas as pd
import model.conf.KJraConst as const
import pyodbc


#番組ヘッダのクエリ
#指定年のプログラムヘッダを返す。
def get_program_header_by_year_to_df(accessor, year):
	template = """
		select	
			* 
		from 
			{0} 
		where 
			ph_year='{1}'
		order by ph_id
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		 year)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#指定IDのプログラムヘッダを返す。
def get_program_at_by_id_to_sr(accessor, program_id):
	template = """
		select 
			* 
		from 
			{0} 
		where 
			ph_id='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		 program_id)
	ret = pd.Series()
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret

def get_latest_program_header(accessor):
	template = "select top 3 * from {0} order by ph_id desc"
	cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_year_to_df(accessor):
	template = """
		select distinct(ph_year) from {0} 
		"""
	cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER)
	accessor.execute(cmd)
	temp = accessor.read_sql_to_df(cmd)
	series = temp.iloc[:,0]
	ret = series.tolist()
	return ret

def get_max_count(accessor):
	template = """
		select max(int({0}.ph_count)) from {0} 
		"""
	cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		break
	accessor.cur_close()
	return ret


def get_max_place_count(accessor):
	template = """
		select max(int({0}.ph_place_count)) from {0} 
		"""
	cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		break
	accessor.cur_close()
	return ret


#指定年のプログラムヘッダを返す。
def get_latest_program(accessor):
	template = """
		select 
			top 3 * 
		from 
			{0} 
		order by 
			{0}.ph_year desc, {0}.ph_monthday
		"""
	cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER)
	ret = accessor.read_sql_to_df(cmd)
	return ret


#指定年のJRAプログラムヘッダを返す。
def get_latest_jra_program(accessor):
	template = """
		select 
			top 3 * 
		from 
			{0} 
		where
			ph_place = '01'
			OR
			ph_place = '02'
			OR
			ph_place = '03'
			OR
			ph_place = '04'
			OR
			ph_place = '05'
			OR
			ph_place = '06'
			OR
			ph_place = '07'
			OR
			ph_place = '08'		
			OR
			ph_place = '09'		
			OR
			ph_place = '10'			
		order by 
			{0}.ph_year desc, {0}.ph_monthday desc
		"""
	cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#指定年のプログラムヘッダを返す。
def get_latest_program_id(accessor):
	template = """
		select 
			top 3 {0}.ph_id 
		from {0} 
		order by ph_id desc
		"""
	cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER)
	ret = accessor.read_sql_to_df(cmd)
	return ret


#指定年のプログラムヘッダを返す。
def get_today_program(accessor):
	today = datetime.date.today()

	template = """
		select 
			* 
		from 
			{0} 
		where 
			int(ph_id/100) in (
				select top 1 int(ph_id/100) 
				from {0} 
				where
					ph_year = {1}
					and
					ph_month ={2}
					and
					ph_day={3}
				order by ph_id desc
				)
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		today.year,
		today.month,
		today.day
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

	
#指定年のプログラムヘッダを返す。
def get_last_week_program_to_df(accessor):
	ret =pd.DataFrame()
	today = datetime.date.today()

	template = """
		select 
			top 10 * 
		from 
			{0} 
		order by ph_id desc	
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER
		)
	df_ph_list = accessor.read_sql_to_df(cmd)
	td = datetime.timedelta(weeks=1)
	
	for i, df_ph in df_ph_list.iterrows():
		t = datetime.date(df_ph['ph_year'], df_ph['ph_month'], df_ph['ph_day']) 
		diff = today - t
		if(diff < td):
			ret = ret.append(df_ph)
		
	return ret
