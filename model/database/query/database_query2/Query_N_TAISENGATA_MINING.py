import pyodbc
import model.conf.KJraConst as const
import pandas as pd
# var mess = data.id.Year + " " +
# data.id.MonthDay +
# " " + data.id.JyoCD +
# " " + data.id.Kaiji +
# " " + data.id.Nichiji +
# " " + data.id.RaceNum;

def get_all_mining_at_to_df(accessor):
	ret = pd.DataFrame()
	template = """
		SELECT top *
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[Year]  DESC,
			[MonthDay]  DESC,
			[JyoCD]  DESC,
			[Kaiji]  DESC,
			[Nichiji]  DESC,
			[RaceNum]  DESC,
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_TAISENGATA_MINING
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_mining_at_to_sr(accessor, y, md, p, r):
	ret = pd.Series()
	template = """
		SELECT *
		FROM [kjvan].[dbo].[{0}]
		WHERE
			{0}.Year = '{1}' AND 
			{0}.MonthDay = '{2}' AND 
			{0}.JyoCD  = '{3}' AND 
			{0}.RaceNum = '{4}'	 	

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_TAISENGATA_MINING,
		 y, md, p,  r
	)
	ret = accessor.read_sql_to_df(cmd)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret