import pyodbc
import model.conf.KJraConst as const

#
def get_latest_place_by_date_list(accessor, y, md):
	template = """
		select JyoCD from [kjvan].[dbo].[{0}]
		WHERE Year+Monthday = ANY (
		select top 1 Year+Monthday from [kjvan].[dbo].[{0}] 
			where Year <='{1}'and MonthDay <='{2}'
			order by Year desc, Monthday desc
		) and Datakubun='2'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_SCHEDULE,
		y,
		md
	)
	ret=[]
	df = accessor.read_sql_to_df(cmd)
	for i in range(len(df)):
		dt = df.iloc[i]
		ret.append(dt['JyoCD'])
	return ret
