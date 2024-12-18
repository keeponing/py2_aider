from tkinter.tix import Tree
import pandas as pd
import model.conf.KJraConst as const

#レースヘッダのクエリ

def get_race_to_df(accessor):
	template = """
		select  *
		from {0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_HV_CACHE_VALIABLE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_hv_one_by_ih_to_sr(accessor, program_id, horse_id, is_direct=False):
	y = program_id[:4]
	if(False == is_direct):
		mdb = const.TBL_KJDB_HV_CACHE_VALIABLE_AT.format(y)
	else:
		mdb = const.TBL_KJDB_HV_CACHE_VALIABLE
	template = """
		select  
			*
		from {0} 
		where
			key_program_id ='{1}'
			and
			key_horse_id='{2}'
		"""
	cmd = template.format(
		mdb,
		program_id, 
		horse_id
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(0 == len(df_temp)):
		dict_zero = {'his_l4_p1': 0, 'his_l4_p2': 0, 'his_l4_p3': 0, 'his_l4_p4': 0}
		ret = pd.Series(dict_zero)
	else:

		ret = df_temp[['his_l4_p1', 'his_l4_p2', 'his_l4_p3', 'his_l4_p4']].iloc[0]
	return ret

def get_hv_one_by_ih_to_sr2(accessor, program_id, horse_id):
	template = """
		select  
			*
		from {0} 
		where
			key_program_id ='{1}'
			and
			key_horse_id='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_HV_CACHE_VALIABLE,
		program_id, 
		horse_id
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(0 == len(df_temp)):
		dict_zero = {
	        'his_sc_l4_p1': 0, 'his_sc_l4_p2': 0, 'his_sc_l4_p3': 0, 'his_sc_l4_p4': 0}
		ret = pd.Series(dict_zero)
	else:
		ret = df_temp[[
		 	'his_sc_l4_p1', 'his_sc_l4_p2', 'his_sc_l4_p3', 'his_sc_l4_p4']].iloc[0]
	return ret

def get_hv_one_by_ih_to_sr3(accessor, program_id, horse_id):
	ret = pd.DataFrame()
	y = int(program_id[:4])
	if(1999 < y):
		mdb = const.TBL_KJDB_HV_CACHE_VALIABLE_AT.format(y)
		template = """
			select  
				*
			from {0} 
			where
				key_program_id ='{1}'
				and
				key_horse_id='{2}'
			"""
		cmd = template.format(
			mdb,
			program_id, 
			horse_id
			)
		df_temp = accessor.read_sql_to_df(cmd)
		if(0 == len(df_temp)):
			dict_zero = {
				'his_l4_p1': 0, 'his_l4_p2': 0, 'his_l4_p3': 0, 'his_l4_p4': 0,
				'his_sc_l4_p1': 0, 'his_sc_l4_p2': 0, 'his_sc_l4_p3': 0, 'his_sc_l4_p4': 0}
			ret = pd.Series(dict_zero)
		else:
			ret = df_temp[[
				'his_l4_p1', 'his_l4_p2', 'his_l4_p3', 'his_l4_p4',
				'his_sc_l4_p1', 'his_sc_l4_p2', 'his_sc_l4_p3', 'his_sc_l4_p4'
				]].iloc[0]
	return ret

def is_existed(accessor, program_id , race_no, horse_id):

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
			desc_race_no={3}
		"""
	cmd = template.format(
		const.TBL_KJDB_HV_CACHE_VALIABLE,#0
		program_id,
		horse_id,
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


def is_existed2(accessor, program_id , horse_id):

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
	cmd = template.format(
		const.TBL_KJDB_HV_CACHE_VALIABLE,#0
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

def is_sc_null(accessor, program_id , race_no, horse_id):

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
			desc_race_no={3}
		and
			his_sc_l4_p1 is null
		"""
	cmd = template.format(
		const.TBL_KJDB_HV_CACHE_VALIABLE,#0
		program_id,
		horse_id,
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


def is_upd3(accessor, program_id, horse_id):
	template = """
		select 
			count(*) 
		from 
			{0}
		where	
			key_program_id='{1}'
			and
			key_horse_id ='{2}'
			and 
			upd=3
		"""
	cmd = template.format(
		const.TBL_KJDB_HV_CACHE_VALIABLE,
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


def get_pid_hid_by_upd3(accessor):
	template = """
		select 
			{0}.key_program_id,
			{0}.key_horse_id
		from 
			{0}
		where	
			{0}.upd=3
		"""
	cmd = template.format(
		const.TBL_KJDB_HV_CACHE_VALIABLE,
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret


#データを取得
def get_records_y_to_df(accessor, y):
	template = """
		select
			{0}.*
		from	   
			{0}
	
		"""
	mdb = const.TBL_KJDB_HV_CACHE_VALIABLE.format(y)
	cmd = template.format(
		mdb
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret  