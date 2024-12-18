import pyodbc
import model.conf.KJraConst as const

#
def get_trainer_to_df(accessor):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[ChokyosiCode]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_CHOKYO
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_trainer_id_to_list(accessor):
	ret = []
	template = """
		select 
			distinct([ChokyosiCode])
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_CHOKYO,
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp['ChokyosiCode'].to_list()
	return ret