import pyodbc
import model.conf.KJraConst as const
import pandas as pd
#統計情報値

def get_record_all_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_record_not_null_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		where 
			{0}.sv_deviation is null
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_sv_by_phid_to_sr(accessor, program_id, horse_id, is_direct=False):
	ret = pd.Series()
	y = program_id[:4]
	if('0000'!= y):
	
		if(False == is_direct):
			mdb = const.TBL_KJDB_STATISTICS_CACHE_VALIABLE_AT.format(y)
		else:
			mdb = const.TBL_KJDB_STATISTICS_CACHE_VALIABLE
		template = """
			select 
				*
			from 
				{0} 
			where
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'

			"""
		cmd = template.format(
			mdb,
			program_id,
			horse_id
			)
		df_temp = accessor.read_sql_to_df(cmd)
		if(len(df_temp)):
			ret = df_temp.iloc[0]
	return ret


def get_sv_to_sr2(accessor, program_id, horse_id):
	ret = pd.Series()
	y = program_id[:4]
	if('0000'!= y):
		mdb = const.TBL_KJDB_STATISTICS_CACHE_VALIABLE_AT.format(y)
		template = """
			select 
				*
			from 
				{0} 
			where
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'

			"""
		cmd = template.format(
			mdb,
			program_id,
			horse_id
			)
		df_temp = accessor.read_sql_to_df(cmd)
		if(len(df_temp)):
			ret = df_temp.iloc[0]
	return ret




def get_sv_by_h_to_df(accessor, horse_id):
	template = """
		select 
			*
		from 
			{0} 
		where

			sv_horse_id ='{1}'
		order by
			sv_program_id
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		horse_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_feets_to_sr(accessor, program_id, horse_id):
	template = """
		select 
			{0}.sv_feet_pb1,{0}.sv_feet_pb2,{0}.sv_feet_pb3,{0}.sv_feet_pb4
		from 
			{0} 
		where
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'

		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		program_id,
		horse_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_burden_to_sr(accessor, program_id, horse_id):
	template = """
		select 
			{0}.sv_burdern
		from 
			{0} 
		where
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'

		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		program_id,
		horse_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_odds_to_sr(accessor, program_id, horse_id):
	template = """
		select 
			{0}.sv_odds
		from 
			{0} 
		where
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'

		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		program_id,
		horse_id
		)
	ret= pd.Series()
	temp = accessor.read_sql_to_df(cmd)
	if(0 != len(temp)):
		ret = temp.iloc[0]
	return ret 

def get_weight_to_sr(accessor, program_id, horse_id):
	template = """
		select 
			{0}.sv_weight
		from 
			{0} 
		where
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'

		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		program_id,
		horse_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_sv_no_upd_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		where
			upd =0
		order by
			sv_program_id
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret
def is_existed(accessor,  program_id, horse_id):
	template = """
		select 
			count(*) 
		from 
			{0}
		where	
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		program_id,
		horse_id
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


def is_upd(accessor, program_id, horse_id):
	template = """
		select 
			count(*) 
		from 
			{0}
		where	
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'
			and 
			upd=2
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		program_id,
		horse_id
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


def is_upd3(accessor, program_id, horse_id):
	template = """
		select 
			count(*) 
		from 
			{0}
		where	
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'
			and 
			upd=3
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		program_id,
		horse_id
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

def get_upd(accessor, program_id, horse_id):

	y = program_id[:4]
	mdb = const.TBL_KJDB_STATISTICS_CACHE_VALIABLE_AT.format(y)  
	template = """
		select 
			{0}.upd
		from 
			{0} 
		where
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'

		"""
	cmd = template.format(
		mdb,
		program_id,
		horse_id
		)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = 0
	if(len(df_temp)):
		ret = df_temp.iloc[0]['upd']

	return ret

def is_null(accessor, program_id, horse_id):

	y = program_id[:4]
	mdb = const.TBL_KJDB_STATISTICS_CACHE_VALIABLE_AT.format(y)  
	template = """
		select 
			count(*)
		from 
			{0} 
		where
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'
			and
			sv_win_score_wa IS NULL
		"""
	cmd = template.format(
		mdb,
		program_id,
		horse_id
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



def get_zero_speed_exp(accessor):
	ret = pd.DataFrame()
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_zero_speed_3f_exp(accessor):
	ret = pd.DataFrame()
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_all_pid_and_hid_and_speed_exp_to_df(accessor):
	template = """
		select 
			{0}.sv_program_id,
			{0}.sv_horse_id,
			{0}.sv_speed_exp
		from 
			{0} 
		order by
			sv_program_id
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


	
def get_horse_id_by_upd(accessor, upd):
	   
	template =  """
		select 
			{0}.sv_horse_id
		from	   
			{0}
		where
			upd={1}
	"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		upd
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


	
def get_speed_exp_by_ph_to_sr(accessor, program_id, horse_id):
	ret = pd.Series()
	y = program_id[:4]
	mdb = const.TBL_KJDB_STATISTICS_CACHE_VALIABLE_AT.format(y)   
	template =  """
		select 
			{0}.sv_speed_exp
		from	   
			{0}
		where
			{0}.sv_program_id='{1}'
			and
			{0}.sv_horse_id = '{2}'
	"""
	cmd = template.format(
		mdb,
		program_id,
		horse_id,
		)
	
	df_temp = accessor.read_sql_to_df(cmd)   
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret

def get_speed_exp_list_by_ph(accessor, program_id_list, horse_id):
 
	# Create a placeholder for multiple program IDs
	formatted_ids = ', '.join([f"'{id}'" for id in program_id_list])
	
	# Construct the SQL query with multiple program IDs
	template = """
		SELECT
			{0}.sv_speed_exp
		FROM
			{0}
		WHERE
			{0}.sv_program_id IN ({1})
			AND
			{0}.sv_horse_id = '{2}'
		ORDER BY 
			sv_program_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		formatted_ids,
		horse_id,
	)
	
	# Execute the query with the program IDs
	ret = accessor.read_sql_to_df(cmd)

	return ret

def get_upd_at_to_df(accessor, upd):
	template = """
		select 
			{0}.sv_program_id, {0}.sv_horse_id
		from 
			{0} 
		where 
			upd={1}
		order by sv_program_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		upd
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  
	

