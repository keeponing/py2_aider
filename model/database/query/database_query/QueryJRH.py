import model.conf.KJraConst as const
import pandas as pd
#レースヘッダのクエリ

def get_race_to_df(accessor):
	template = """
		select  *
		from {0} 
		order by 
			rh_id
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_program_race_to_df(accessor):
	template = """
		SELECT {0}.* , {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		order by ph_id, rh_race desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#年、距離、トラックの情報をGroupByして返す
def get_race_group_by_y(accessor, year):
	template = """
		SELECT LEFT(rh_id, 4) as rh_year,RIGHT(rh_id, 2) as rh_place,rh_track, rh_distance
		FROM {0}
		where LEFT(rh_id, 4) = '{1}'
		GROUP BY LEFT(rh_id, 4), RIGHT(rh_id, 2), rh_track, rh_distance
		
		"""
 # ORDER BY rh_year desc
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
  		year)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#年、距離、トラックの情報をGroupByして返す
def get_race_group_by_year(accessor, year):
	template = """
		SELECT LEFT(rh_id, 4) as rh_year,RIGHT(rh_id, 2) as rh_place,rh_track, rh_distance
		FROM {0}
		WHERE 
			LEFT(rh_id, 4) ='{1}'
		GROUP BY LEFT(rh_id, 4), RIGHT(rh_id, 2), rh_track, rh_distance
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		year
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#レースヘッダ一覧を返す
def get_race_headers_by_y(accessor, year):
	template = """
		select  *
		from {0} 
		where rh_id like '{1}%'
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		year)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#レースヘッダ一覧を返す
def get_race_at_by_ir_to_sr(accessor, program_id, race):
	template = """
		select  *
		from {0} 
		where 
				rh_id='{1}'
			and 
				rh_race ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		program_id,
		race
		)
	df_temp = accessor.read_sql_to_df(cmd)

	ret= pd.Series()
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret

#指定年のレースヘッダを返す。
def get_race_header_by_id(accessor, program_id):  
	template = """
		select {0}.* 
		from 
			{0}
		where 
			rh_id = '{1}' 
	"""
	cmd = template.format(const.TBL_KJDB_RACE_HEADER, program_id)
	ret = accessor.read_sql_to_df(cmd)
	return ret




def is_existed(accessor, program_id, race_no):

	template = """
		select 
			count(*) 
		from 
			{0} 
		where 
			rh_id='{1}'
		and 
			rh_race='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		program_id,
		race_no
		)
	accessor.execute(cmd)
	ret = False
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		if(0 != ret):
			ret = True
		break
	accessor.cur_close()

	return ret


def is_upd(accessor, program_id, race_no):
	ret = False
	template = """
		select 
			count(*)
		from 
			{0} 
		where 
				{0}.rh_id='{1}'
			and 
				{0}.rh_race ='{2}'
			and
				{0}.rh_upd=1
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		program_id,
		race_no
		)
	accessor.execute(cmd)
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		if(0 != ret):
			ret = True
		break
	accessor.cur_close()
	return ret



def get_upd(accessor, program_id, race_no):
	ret = 0
	template = """
		select 
			{0}.rh_upd
		from 
			{0} 
		where 
				{0}.rh_id='{1}'
			and 
				{0}.rh_race ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		program_id,
		race_no
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(0 != len(df_temp)):
		sr_temp = df_temp.iloc[0]
		ret = sr_temp['rh_upd']
	return ret

def get_current_race_until_today_to_df(accessor, year, md, hm1, hm2):
	template = """
		SELECT  *
		FROM {0}
		WHERE 
			[rh_id] like '{1}%'
			and
			(
				CLng([rh_race_hm]) > CLng('{2}')
				and 
				CLng([rh_race_hm]) < CLng('{3}')
			)
		ORDER BY rh_id DESC
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		f'{year}{md}',
		hm1, 
		hm2
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_current_race_until_tomorrow_to_df(accessor,year, md):
	template = """
		SELECT  *
		FROM {0}
		WHERE 
			[rh_id] like '{1}%'
		ORDER BY rh_id DESC
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		f'{year}{md}'	
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_latest_top_n_to_df(accessor, n):
	template = """
		SELECT  top {1} *
		FROM {0}
		ORDER BY rh_id DESC, rh_race
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		n
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_latest_top_n_to_df2(accessor, n):
	template = """
		SELECT
		TOP {2} {0}.*
		, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		order by ph_id desc, rh_race desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		n
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_latest_makedebut_top_n_to_df(accessor, n):
	template = """
		SELECT
		TOP {2} {0}.*
		, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		WHERE
		 {1}.rh_te_c2_code = '1'
		order by ph_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		n
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


#レースヘッダ一覧を返す
def get_program_and_race_at_by_ir_to_df(accessor, program_id, race):
	template = """
		select  {0}.*, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		where 
				rh_id='{2}'
			and 
				rh_race ='{3}'
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		program_id,
		race
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#レースヘッダ一覧を返す
def get_race_at_by_p_to_df(accessor, place):
	template = """
		select  {0}.*, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		where 
				ph_place='{2}'
		order by 
			ph_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		place
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#レースヘッダ一覧を返す
def get_race_at_by_yp_to_df(accessor, y, place):
	template = """
		select  {0}.*, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		where 
				{0}.ph_place='{2}'
				and
				{0}.ph_year='{3}'
		order by 
			ph_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		place,
		y
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_track_code_to_list(accessor, place_code):
	template = """
		select  distinct({0}.rh_track)
		FROM
		{0} 
		where 
			right(rh_id, 2) = '{1}'	
		order by 
			rh_track
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		place_code
		)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = df_temp['rh_track'].to_list()
	return ret

def get_distance_code_to_list(accessor, place_code, track_code):
	template = """
		select  distinct({0}.rh_distance)
		FROM
		{0} 
		where 
			right(rh_id, 2) = '{1}'
			and
			rh_track='{2}'
		order by 
			rh_distance
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		place_code,
		track_code
		)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = df_temp['rh_distance'].to_list()
	return ret

#レースヘッダ一覧を返す
def get_race_at_by_pt_to_df(accessor, place, track_code):
	template = """
		select  {0}.*, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		where 
				{0}.ph_place='{2}'
				and
				{1}.rh_track='{3}'
		order by 
			ph_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		place,
		track_code
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


#レースヘッダ一覧を返す
def get_race_at_by_ptd_to_df(accessor, place, track_code, distance_code):
	template = """
		select  {0}.*, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		where 
				{0}.ph_place='{2}'
				and
				{1}.rh_track='{3}'
				and
				{1}.rh_distance='{4}'
		order by 
			ph_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		place,
		track_code,
		distance_code
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


#レースヘッダ一覧を返す
def get_race_at_by_y_to_df(accessor, y):
	template = """
		select  {0}.*, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		where 
				{0}.ph_year='{2}'
		order by 
			ph_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		y
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_records_by_sp_code_to_df(accessor, sp_code):
	template = """
		select  {0}.*, {1}.* 
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.ph_id = {1}.rh_id 
		where 
			{1}.rh_sp_code='{2}'
		order by 
			{0}.ph_id 
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER,
		const.TBL_KJDB_RACE_HEADER,
		sp_code
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_sp_code_to_list(accessor):
	template = """
		select  distinct({0}.rh_sp_code)
		from
		{0} 
		where
		 rh_sp_code <>'0000'
		order by 
			rh_sp_code
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER
		)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = df_temp['rh_sp_code'].to_list()
	return ret



def get_hash256_to_list(accessor):
	template = """
		select  distinct({0}.rh_cnd_hash256)
		from
		{0} 
		where
			rh_sp_code
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER
		)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = df_temp['rh_cnd_hash256'].to_list()
	return ret


def get_records_by_place_to_df(accessor, place_code):
	template = """
		select  *
		FROM
		{0} 
		where 
			right(rh_id, 2) = '{1}'	
		order by 
			rh_id
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		place_code
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret