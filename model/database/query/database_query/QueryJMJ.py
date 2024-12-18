import pyodbc
import model.conf.KJraConst as const


def get_master_jockey_list_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_JOCKEY
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_master_jockey_id_list(accessor):
	template = """
		select 
			mj_id
		from 
			{0} 
		order by mj_id
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_JOCKEY
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )		
	temp = accessor.read_sql_to_df(cmd)
	series = temp.iloc[:,0]
	ret = series.tolist()
	return ret