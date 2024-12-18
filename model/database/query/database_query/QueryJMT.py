import pyodbc
import model.conf.KJraConst as const


def get_master_trainer_list_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_TRAINER
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_master_trainer_id_list(accessor):
	template = """
		select 
			mt_id
		from 
			{0} 
		order by mt_id
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_TRAINER
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )		
	temp = accessor.read_sql_to_df(cmd)
	series = temp.iloc[:,0]
	ret = series.tolist()
	return ret