import pyodbc
import model.conf.KJraConst as const

#
def get_owner_to_df(accessor):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[BanusiCode]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_BANUSI
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_owner_id_to_list(accessor):
	ret = []
	template = """
		select 
			distinct([BanusiCode])
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_BANUSI,
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp['BanusiCode'].to_list()
	return ret