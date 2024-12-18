import pyodbc
import model.conf.KJraConst as const

#
def get_jockey_to_df(accessor):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[KisyuCode]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_KISYU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_jockey_name_by_id(accessor, jocky_id):
	template = """
		SELECT  [KisyuRyakusyo]
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[KisyuCode]='{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_KISYU,
		jocky_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_jockey_id_to_list(accessor):
	ret = []
	template = """
		select 
			distinct([KisyuCode])
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_KISYU,
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp['KisyuCode'].to_list()
	return ret