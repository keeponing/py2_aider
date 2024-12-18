import pyodbc
import model.conf.KJraConst as const

def get_describe(accessor, id):
	template = """	
		select 
				{0}.*
			from
				{0}
			where  
			(
				{0}.td_id = '{1}'
			)
		"""
	cmd = template.format(
		const.TBL_KJDB_TIME_DESCRIBES,
		id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret
	
#データが存在するか
def is_existed(accessor, te_id):
	template = """
		select
			count(*) 
		from 
			{0} 
		where 
			{0}.td_id='{1}' 
		"""
	cmd = template.format(const.TBL_KJDB_TIME_DESCRIBES, te_id)
	accessor.execute(cmd)
	ret =False
	total_count = 0
	for c in accessor.cur.fetchall():
		total_count = int(c[0])
		if(total_count != 0):
			ret = True
		break
	accessor.cur_close()
	return ret