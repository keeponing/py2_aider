import pandas as pd
import model.conf.KJraConst as const

def get_result_at_to_sr(accessor, year, md, place, race_no):
	ret = pd.Series()
	template= """
		SELECT
			*
		FROM [kjvan].[dbo].[{0}] 
		WHERE
			{0}.Year='{1}' 
			AND
			{0}.MonthDay='{2}' 
			AND
			{0}.JyoCD='{3}' 
			AND
			{0}.RaceNum='{4}' 
			AND
			{0}.DataKubun='1' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_HARAI,
		year,
		md,
		place, 
		race_no
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret


def get_result_to_sr(accessor, year, md, place, race_no):
	template= """
		SELECT
			*
		FROM [kjvan].[dbo].[{0}] 
		WHERE
			{0}.Year='{1}' 
			AND
			{0}.MonthDay='{2}' 
			AND
			{0}.JyoCD='{3}' 
			AND
			{0}.RaceNum='{4}' 
			AND
			{0}.DataKubun='1' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_HARAI,
		year,
		md,
		place, 
		race_no
	)
	ret = pd.Series()
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret