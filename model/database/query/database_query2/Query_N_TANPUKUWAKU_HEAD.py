import pyodbc
import model.conf.KJraConst as const


def get_release_time(accessor, y, md, place, race_no):
	ret =""
	template = """
		SELECT top 1 HappyoTime
		FROM [kjvan].[dbo].[{0}]
		WHERE
			{0}.Year='{1}'
			and
			{0}.Monthday='{2}'
			and
			{0}.JyoCD='{3}'
			and
			{0}.RaceNum='{4}'
		ORDER BY 
			HappyoTime DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_JODDS_TANPUKUWAKU_HEAD,
		y, 
		md, 
		place, 
		race_no
	)
	df = accessor.read_sql_to_df(cmd)
	if(len(df)):
		ret = df.iloc[0]['HappyoTime']
	return ret
