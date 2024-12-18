import pyodbc
import model.conf.KJraConst as const


def get_record_by_ymdrprh_to_df(accessor, y, md, rt, place, race_no, horse_no):
	template = """
		SELECT top 1 *
		FROM [kjvan].[dbo].[{0}]
		WHERE
			{0}.Year='{1}'
			and
			{0}.Monthday='{2}'
			and
			{0}.HappyoTime='{3}'
			and
			{0}.JyoCD='{4}'
			and
			{0}.RaceNum='{5}'
			and
			{0}.Umaban='{6}'
		ORDER BY 
			HappyoTime DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_JODDS_TANPUKU,
		y, 
		md, 
		rt,
		place, 
		race_no,
		horse_no
	)
	ret = accessor.read_sql_to_df(cmd)

	return ret
