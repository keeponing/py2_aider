import pyodbc
import model.conf.KJraConst as const
import pandas as pd

def get_odds_and_vote_to_sr(accessor, year, md, place, race_no, horse_no):
	ret = pd.Series()
	template= """
		SELECT
			top 1
			[TanOdds]
			,[TanNinki]
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
			{0}.Umaban='{5}' 
		order by HappyoTime desc
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_JODDS_TANPUKU,
		year,
		md,
		place, 
		race_no, 
		horse_no
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret
