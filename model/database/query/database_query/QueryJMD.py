import pyodbc
import model.conf.KJraConst as const

def get_department_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_DEPARTMENT
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_master_department_to_df(accessor):
	template = """
		select 
			{0}.*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_DEPARTMENT
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_master_department_sire_is_to_df(accessor, sire_id):
	template = """
		select 
			md_id
		from 
			{0} 
		where
			{0}.md_sire_id1 ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_DEPARTMENT,
		sire_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def is_existed(accessor, sire_id):
	
	template = """
		select 
			count(*) 
		from 
			{0} 
		where 
			md_id='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_DEPARTMENT,
		sire_id
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
