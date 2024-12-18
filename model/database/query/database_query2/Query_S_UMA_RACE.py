import pyodbc
import model.conf.KJraConst as const
import pandas as pd

def get_race_at_to_df(accessor, year, md, place_code, race_no):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#
def get_race_at_to_df2(accessor, year, md, place_code, race_no):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_at_to_df4(accessor, year, md, place_code, race_no):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret
def get_results_still_id_to_df(accessor, horse_id, year, md):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[KettoNum] = '{1}' 
		AND CONVERT(decimal, [Year]+[MonthDay]) < {2} 
	ORDER BY [Year] DESC, [MonthDay] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id,		
		year+md
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def naget_prev_race_id_by_horse_to_list(accessor, horse_id, year, monday):
	ret = [const.VOID_PID, const.VOID_PID, const.VOID_PID, const.VOID_PID]
	template = """
	SELECT top 4 ([Year]+[MonthDay]+[JyoCD]) as p_id
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[KettoNum] = '{1}' 
		AND CONVERT(decimal, [Year]+[MonthDay]) < {2} 
		AND [KakuteiJyuni] <>'00'
	ORDER BY [Year] DESC, [MonthDay] DESC
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id, 
		year+monday
	)
	df = accessor.read_sql_to_df(cmd)
	for index, row in df.iterrows():
		ret[index] = row.p_id
	return ret

def get_horses_by_pdc_to_df(accessor, td):
	template= """
		SELECT * FROM {0} as T1  
  		INNER JOIN {1} as T2 
  		ON T1.Year=T2.Year AND T1.MonthDay = T2.MonthDay AND T1.JyoCD = T2.JyoCD  AND T1.RaceNum = T2.RaceNum 
		where
		T2.JyoCD='{2}' AND
		T2.Kyori='{3}' AND
		T2.JyokenCD1='{4}' AND
		T2.JyokenCD2='{5}' AND
		T2.JyokenCD3='{6}' AND
		T2.JyokenCD4='{7}' AND
		T2.JyokenCD5='{8}' AND
		T2.SyubetuCD='{9}' AND
		T2.TrackCD='{10}' AND
		T2.TenkoCD='{11}' AND
		T2.SibaBabaCD='{12}' AND
		T2.DirtBabaCD='{13}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
		td['td_place'],
		td['td_distance'],
		td['td_class2'],
		td['td_class3'],
		td['td_class4'],
		td['td_class5over'],
		td['td_classYoung'],
		td['td_category'],
		td['td_track_cd'],
		td['td_weather'],
		td['td_turf_condition'],
		td['td_dirt_condition']
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_describe_by_pdc_to_sr(accessor, td):
	ret = pd.Series()
	template= """
		SELECT 
			COUNT(*) as CntVal,
			AVG(
				CAST(SUBSTRING (T1.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T1.Time ,2,2) as int) +
				CAST(SUBSTRING (T1.Time ,4,1) as int)/10.0
			) as AvgVal,
			STDEVP(
				CAST(SUBSTRING (T1.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T1.Time ,2,2) as int) +
				CAST(SUBSTRING (T1.Time ,4,1) as int)/10.0
			) as StdVal,
			AVG(
				CAST(SUBSTRING (T1.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T1.HaronTimeL3 ,3,1) as int)/10.0
			) as Avg3fVal,
			STDEVP(
				CAST(SUBSTRING (T1.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T1.HaronTimeL3 ,3,1) as int)/10.0
			) as Std3fVal
		FROM {0} as T1  
		INNER JOIN {1} as T2 
		ON T1.Year=T2.Year AND T1.MonthDay = T2.MonthDay AND T1.JyoCD = T2.JyoCD  AND T1.RaceNum = T2.RaceNum 
		where
		T2.JyoCD='{2}' AND
		T2.Kyori='{3}' AND
		T2.JyokenCD1='{4}' AND
		T2.JyokenCD2='{5}' AND
		T2.JyokenCD3='{6}' AND
		T2.JyokenCD4='{7}' AND
		T2.JyokenCD5='{8}' AND
		T2.SyubetuCD='{9}' AND
		T2.TrackCD='{10}' AND
		T2.TenkoCD='{11}' AND
		T2.SibaBabaCD='{12}' AND
		T2.DirtBabaCD='{13}' AND
		T1.Time<>'0000' AND
		T1.ChakusaCD<>'T' AND
		T1.ChakusaCD<>'Z' AND
		T1.ChakusaCD<>'9' AND
		T1.ChakusaCD<>'8'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
		td['td_place'],
		td['td_distance'],
		td['td_class2'],
		td['td_class3'],
		td['td_class4'],
		td['td_class5over'],
		td['td_classYoung'],
		td['td_category'],
		td['td_track_cd'],
		td['td_weather'],
		td['td_turf_condition'],
		td['td_dirt_condition']
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret


def get_race_count(accessor, horse_id, year, monday):
	template = """
		SELECT 
			count(*) 
		FROM 
			{0} 
		WHERE 
			[KettoNum] = '{1}' 
			AND CONVERT(decimal, [Year]+[MonthDay]) <= {2} 
			
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id,
		year+monday
		)
	accessor.execute(cmd)
	for c in accessor.cur.fetchall():
		ret = int(c[0])
	accessor.cur_close()
	return ret

def get_win_mul_count(accessor, horse_id, year, monday):
	template = """
		SELECT T1.Cnt as RaceCnt , T2.Cnt as WinCnt, T3.Cnt as MulCnt FROM
		(SELECT count(*) as Cnt FROM {0} WHERE CONVERT(decimal, Year+MonthDay) < {2} AND KettoNum ='{1}' )  T1,
		(SELECT count(*) as Cnt FROM {0} WHERE CONVERT(decimal, Year+MonthDay) < {2} AND KettoNum ='{1}' AND KakuteiJyuni='01' )  T2,
		(SELECT count(*) as Cnt FROM {0} WHERE CONVERT(decimal, Year+MonthDay) < {2} AND KettoNum ='{1}' AND (KakuteiJyuni='01' OR KakuteiJyuni='02' OR KakuteiJyuni='03'))  T3
	"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id, 
		year+monday
		
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_predicet_sire_by_ymdph_to_df(accessor,y, md, horse_id):
	ret = None
	template = """
		SELECT
		{1}.KettoNum,
		{1}.Kakuteijyuni, 
		{0}.JyoCD,
		{0}.Kyori,
		{0}.TrackCD,
		{1}.KettoNum1,
		{2}.Ketto3InfoHansyokuNum1,
		{2}.Ketto3InfoHansyokuNum2,
		{2}.Ketto3InfoHansyokuNum3,
		{2}.Ketto3InfoHansyokuNum4,
		{2}.Ketto3InfoHansyokuNum5,
		{2}.Ketto3InfoHansyokuNum6,
		{2}.Ketto3InfoHansyokuNum7,
		{2}.Ketto3InfoHansyokuNum8,
		{2}.Ketto3InfoHansyokuNum9,
		{2}.Ketto3InfoHansyokuNum10,
		{2}.Ketto3InfoHansyokuNum11,
		{2}.Ketto3InfoHansyokuNum12,
		{2}.Ketto3InfoHansyokuNum13,
		{2}.Ketto3InfoHansyokuNum14,
		{1}.Year
		FROM ({0} INNER JOIN {1} ON 
		({0}.RaceNum = {1}.RaceNum) AND 
		({0}.Nichiji = {1}.Nichiji) AND 
		({0}.Kaiji = {1}.Kaiji) AND 
		({0}.JyoCD = {1}.JyoCD) AND 
		({0}.Year = {1}.Year)) 
		INNER JOIN {2} ON {1}.KettoNum = {2}.KettoNum
		WHERE 
			{0}.JyoCD='01' OR 
			{0}.JyoCD='02' OR
			{0}.JyoCD='03' OR 
			{0}.JyoCD='04' OR 
			{0}.JyoCD='05' OR 
			{0}.JyoCD='06' OR 
			{0}.JyoCD='07' OR 
			{0}.JyoCD='08' OR 
			{0}.JyoCD='09' OR 
			{0}.JyoCD='10' 
			AND
			{1}.Year = '{3}'
			AND
			{1}.MonthDay='{4}'
			AND
			{1}.KettoNum='{5}'
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_S_RACE,
		const.TBL_KJVAN_S_UMA_RACE,
		const.TBL_KJVAN_S_UMA,
		y,
		md,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)

	return ret

def get_jocky_cd_by_ymdp_at_to_df(accessor, year, md, place_code):
	template = """
	SELECT distinct({0}.[KisyuCode])
	FROM {0}
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year, 
		md, 
		place_code
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret