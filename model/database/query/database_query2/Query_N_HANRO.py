import pyodbc
import model.conf.KJraConst as const

#
def get_hanro_by_date_to_df(accessor, date):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[ChokyoDate]='{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_HANRO,
		date
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_top_10_hanro_by_horse_id_to_df(accessor, horse_id):
	template = """
		SELECT  top 10 *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[KettoNum]='{1}'
		ORDER BY
			[ChokyoDate] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_HANRO,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_hanro_by_ymdr_to_df(accessor, y,md, place, race_no):
	template = """
		SELECT
		{0}.Wakuban,
		{0}.Umaban,
		{0}.Bamei,
		{0}.Year,
		{0}.MonthDay,
		{1}.KettoNum,
		{1}.TresenKubun,
		{1}.ChokyoDate,
		{1}.ChokyoTime,
		CONVERT(float,{1}.HaronTime4)/10 ,
		CONVERT(float,{1}.HaronTime3)/10,
		CONVERT(float,{1}.HaronTime2)/10,
		CONVERT(float,{1}.LapTime4)/10,
		CONVERT(float,{1}.LapTime3)/10,
		CONVERT(float,{1}.LapTime2)/10,
		CONVERT(float,{1}.LapTime1)/10
		FROM
		{0} 
		INNER JOIN {1} 
			ON {0}.KettoNum = {1}.KettoNum
			WHERE
		{0}.Year = '{2}' 
		AND {0}.MonthDay = '{3}' 
		AND {0}.JyoCD = '{4}' 
		AND {0}.RaceNum = '{5}'
		ORDER BY {0}.Umaban, {1}.ChokyoDate DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_HANRO,
		y,md, 
		place,
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret