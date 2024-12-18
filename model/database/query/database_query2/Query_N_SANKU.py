import pyodbc
import model.conf.KJraConst as const

#
def get_sanku_to_df(accessor):
	template = """
		SELECT *
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[KettoNum]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_SANKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_id_to_df(accessor):
	template = """
		SELECT  [KettoNum]
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[KettoNum]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_SANKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret
def get_production_to_df(accessor):
	template = """
		SELECT *
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[KettoNum]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_SANKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_blood_to_df(accessor):
	template = """
		SELECT
			[KettoNum]
			, [FNum]
			, [MNum]
			, [FFNum]
			, [FMNum] 
			, [MFNum] 
			, [MMNum] 
			, [FFFNum] 
			, [FFMNum] 
			, [FMFNum] 
			, [FMMNum] 
			, [MFFNum] 
			, [MFMNum] 
			, [MMFNum] 
			, [MMMNum]  
		FROM [kjvan].[dbo].[{0}]		
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_SANKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_sire_id_to_list(accessor):
	ret = []
	template = """
		select 
			distinct([FNum])
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_SANKU,
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp['FNum'].to_list()
	return ret