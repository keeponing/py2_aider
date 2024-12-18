import pyodbc
import model.conf.KJraConst as const
import pandas as pd

def get_all_record_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_STUD_SCORE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_record_by_stud_id_to_df(accessor, stud_id):
	template = """
		select 
			*
		from 
			{0} 
		where
			stud_id ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_STUD_SCORE,
		stud_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def is_existed(accessor, stud_id):
	template = """
		select 
			count(*)
		from 
			{0} 
		where
			stud_id ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_STUD_SCORE,
		stud_id
		)

	accessor.execute(cmd)
	ret = False
	for c in accessor.cur.fetchall():
		temp = int(c[0])
		if(0 != temp):
			ret = True
		break
	accessor.cur_close()
	return ret

def get_record_at_to_sr(accessor, stud_id):
	ret = pd.Series()
	template = """
		select 
			*
		from 
			{0} 
		where
			stud_id ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_STUD_SCORE,
		stud_id
		)
	# cmd = cmd.replace( '\n' , ' ' )
	# cmd = cmd.replace( '\t' , ' ' )	
	# print(cmd)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret


def get_all_stud_id_to_list(accessor):
	template = """
		select 
			{0}.stud_id
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_STUD_SCORE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret['stud_id'].tolist()