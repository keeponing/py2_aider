

import model.conf.KJraConst as const
import pandas as pd

def get_latest_make_date(accessor):
	ret=""
	template = """
		SELECT distinct([MakeDate])
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[MakeDate] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(0 != len(df_temp)):
		dt_temp = df_temp.iloc[0]
		ret = dt_temp['MakeDate']
	return ret
#
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
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_races_by_y_to_df(accessor, year):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [KakuteiJyuni] <>'00'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_horse_id_by_y_to_df(accessor, year):
	template = """
	SELECT {0}.[KettoNum]
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [KakuteiJyuni] <>'00'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_races_by_y_to_df2(accessor, year):
	template = """
	SELECT 
		{0}.[KettoNum],
		{0}.[Year],
		{0}.[MonthDay],
		{0}.[JyoCD],
		{0}.[Wakuban],
		{0}.[Umaban],
		{0}.[SexCD],
		{0}.[HinsyuCD],
		{0}.[KeiroCD],
		{0}.[Barei],
		{0}.[TozaiCD],
		{0}.[ChokyosiCode],
		{0}.[BanusiCode],
		{0}.[Futan],
		{0}.[Blinker],
		{0}.[KisyuCode],
		{0}.[ZogenFugo],
		{0}.[ZogenSa],
		{0}.[ChakusaCD],
		{0}.[ChakusaCDP],
		{0}.[ChakusaCDPP],
		{0}.[Odds],
		{0}.[Ninki],
		{0}.[HaronTimeL3],
		{0}.[TimeDiff],
		{0}.[KyakusituKubun],
		{0}.[KettoNum1]
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [KakuteiJyuni] <>'00'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_rank_non_zero_at_to_df(accessor, year, md, place_code, race_no):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		AND [KakuteiJyuni] <>'00'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_at_to_df2(accessor, year, md, place_code, race_no,horse_id ):
	template = """
	SELECT {0}.Futan,
			{0}.BaTaijyu,
			{0}.ZogenFugo,
			{0}.ZogenSa,
			{0}.TimeDiff,
			{0}.Time,
			{0}.HaronTimeL3,
			{0}.Ninki
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		AND [KettoNum]='{5}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no,
		horse_id
	)

 
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_at_to_df3(accessor, year, md, place_code, race_no ):
	template = """
	SELECT  {0}.KettoNum,
			{0}.Futan,
			{0}.BaTaijyu,
			{0}.ZogenFugo,
			{0}.ZogenSa,
			{0}.TimeDiff,
			{0}.Time,
			{0}.HaronTimeL3
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		AND [KakuteiJyuni] <>'00'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no,
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
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_by_hi_at_to_df(accessor, horse_id):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[KettoNum] = '{1}' 
	ORDER BY
		[Year],[Monthday]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret
#

def get_horse_at_to_df(accessor, year, md, place_code, race_no,horse_id ):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		AND [KettoNum]='{5}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no,
		horse_id
	)

 
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_by_make_date_to_df(accessor, make_date ):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[MakeDate] = '{1}' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		make_date
	)

 
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_horse_at_to_df2(accessor, year, md, horse_id ):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [KettoNum]='{3}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		horse_id
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


def get_prev_race_id_by_horse_to_list(accessor, horse_id, year, monday):
	ret = [const.VOID_PID,const.VOID_PID,const.VOID_PID,const.VOID_PID]
	template = """
	SELECT top 4 ([Year]+[MonthDay]+[JyoCD]) as p_id
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[KettoNum] = '{1}' 
		AND 
		CONVERT(decimal, [Year]+[MonthDay]) < {2} 
		AND 
		[IJyoCD]='0'
		AND
		[KakuteiJyuni] <>'00'
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


def get_same_course_prev_race_id_by_horse_to_list(accessor, horse_id, year, monday, track_cd, turf_condition, dirt_condition, distance):
	ret = [const.VOID_PID,const.VOID_PID,const.VOID_PID,const.VOID_PID]
	template = """
	SELECT top 4 (T2.[Year]+T2.[MonthDay]+T2.[JyoCD]) as p_id
	FROM {0} as T1  
	INNER JOIN {1} as T2 
	ON T1.Year=T2.Year AND T1.MonthDay = T2.MonthDay AND T1.JyoCD = T2.JyoCD  AND T1.RaceNum = T2.RaceNum 
	WHERE 
		T1.[KettoNum] = '{2}' 
		AND 
		CONVERT(decimal, T1.[Year]+T1.[MonthDay]) < {3} 
		AND
		T2.[TrackCD]='{4}'
		AND
			(
				T2.[SibaBabaCD]='{5}'
				OR
				T2.[DirtBabaCD]='{6}'
			)
		AND
		T2.[Kyori]='{7}'
		AND 
		T1.[IJyoCD]='0'
		AND
		T1.[KakuteiJyuni] <>'00'
	ORDER BY T1.[Year] DESC, T1.[MonthDay] DESC
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
		horse_id, 
		year+monday,
		track_cd,
		turf_condition,
		dirt_condition,
		distance
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
		FROM [kjvan].[dbo].[{0}] as T1  
		INNER JOIN [kjvan].[dbo].[{1}] as T2 
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
		T1.ChakusaCD<>'8' AND
		T1.KakuteiJyuni <> '00'
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
	ret =0
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


#
def get_race_by_ymdn_to_df(accessor, year, md, horse_name):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [Bamei]='{3}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		horse_name, 
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_jocky_id_to_df(accessor, horse_id, year, md):
	template = """
	SELECT [KisyuCode]
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
	df_temp = accessor.read_sql_to_df(cmd)
	ret =''
	if(len(df_temp)):
		ret = df_temp.iloc[0]['KisyuCode']
	return ret

#
def get_race_cnr_and_rank_at_to_df(accessor, year, md, place_code, race_no):
	template = """
	SELECT [Jyuni1c], [Jyuni2c], [Jyuni3c], [Jyuni4c], [KakuteiJyuni]
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


	
def get_race_zero_rank(accessor, year, md, place_code, race_no):
	template = """
	SELECT *
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		AND [KakuteiJyuni] = '00'
		AND [IJyoCD] = '0'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_race_no(accessor, horse_id, year, monday):
	ret =""
	template = """
		SELECT 
			[RaceNum]
		FROM 
			{0} 
		WHERE 
			[KettoNum] = '{1}' 
			AND 
			[Year] = '{2}' 
			AND 
			[MonthDay]= '{3}'
			
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id,
		year,
		monday
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]['RaceNum']
	return ret


def get_all_program_id_and_horse_id_to_df(accessor):
	ret = None
	template = """
	SELECT([Year]+[MonthDay]+[JyoCD]) as p_id, [KettoNum], [RaceNum]
	FROM [kjvan].[dbo].[{0}]
	ORDER BY [Year] , [MonthDay] DESC
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)

	return ret



def get_rank_sire_to_df(accessor):
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
			(
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
			)
			AND
			(
				{1}.Kakuteijyuni='01' OR
				{1}.Kakuteijyuni='02' OR
				{1}.Kakuteijyuni='03' OR
				{1}.Kakuteijyuni='04' OR
				{1}.Kakuteijyuni='05' OR
				{1}.Kakuteijyuni='06' OR
				{1}.Kakuteijyuni='07' OR
				{1}.Kakuteijyuni='08' OR
				{1}.Kakuteijyuni='09' OR
				{1}.Kakuteijyuni='10' OR
				{1}.Kakuteijyuni='11' OR
				{1}.Kakuteijyuni='12' OR
				{1}.Kakuteijyuni='13' OR
				{1}.Kakuteijyuni='14' OR
				{1}.Kakuteijyuni='15' OR
				{1}.Kakuteijyuni='16' OR
				{1}.Kakuteijyuni='17' OR
				{1}.Kakuteijyuni='18'
			)
			
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_UMA
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
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_UMA,
		y,
		md,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)

	return ret

def get_oldest_year_active_duty(accessor):
	ret ='2000'
	template = """
		SELECT  {1}.Year
		FROM {0} INNER JOIN {1} ON {0}.KettoNum = {1}.KettoNum
		WHERE ((({0}.DelKubun)='0'))
		ORDER BY {1}.Year

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		const.TBL_KJVAN_N_UMA_RACE
	)
	df_year = accessor.read_sql_to_df(cmd)
	if(0!=len(df_year)):
		ret = df_year.iloc[0]['Year']
	return ret	


def get_frame_to_df(accessor):
	template = """
		SELECT  distinct([Wakuban])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_umaban_to_df(accessor):
	template = """
		SELECT  distinct([Umaban])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_sex_cd_to_df(accessor):
	template = """
		SELECT  distinct([SexCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_old_to_df(accessor):
	template = """
		SELECT  distinct([Barei])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_tozai_cd_to_df(accessor):
	template = """
		SELECT  distinct([TozaiCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_trainer_cd_to_df(accessor):
	template = """
		SELECT  distinct([ChokyosiCode])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_owner_cd_to_df(accessor):
	template = """
		SELECT  distinct([BanusiCode])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_burden_to_df(accessor):
	template = """
		SELECT  distinct([Futan])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_blinker_to_df(accessor):
	template = """
		SELECT  distinct([Blinker])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_jockey_to_df(accessor):
	template = """
		SELECT  distinct([KisyuCode])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_chakusa_cd_to_df(accessor):
	template = """
		SELECT  distinct([ChakusaCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_chakusap_cd_to_df(accessor):
	template = """
		SELECT  distinct([ChakusaCDP])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_chakusapp_cd_to_df(accessor):
	template = """
		SELECT  distinct([ChakusaCDPP])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	
def get_rank_sire_ymdph_to_df(accessor,y, md, horse_id):
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
			( 
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
			)
			AND
			{1}.Year = '{3}'
			AND
			{1}.MonthDay='{4}'
			AND
			{1}.KettoNum='{5}'
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_UMA,
		y,
		md,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)

	return ret	



def get_horse_id_by_ymdpr_to_df(accessor, year, md, place_code, race_no ):
	template = """
	SELECT  {0}.KettoNum
	FROM [kjvan].[dbo].[{0}]
	WHERE 
		[Year] = '{1}' 
		AND [MonthDay]= '{2}'
		AND [JyoCD]= '{3}'
		AND [RaceNum]='{4}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code, 
		race_no,
	)

	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_base_time_by_ypdc_to_sr(accessor, y,p,d,t):
	template= """
		SELECT
			COUNT(*) as CntVal,
			AVG(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as AvgVal,
			STDEVP(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as StdVal,
			AVG(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Avg3fVal,
			STDEVP(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Std3fVal

		FROM {0} as T1 
			INNER  JOIN {1} as T2  
			ON 	(T1.RaceNum = T2.RaceNum) AND 
				(T1.Nichiji = T2.Nichiji) AND
				(T1.Kaiji = T2.Kaiji) AND 
				(T1.JyoCD = T2.JyoCD) AND 
				(T1.Year = T2.Year)
		WHERE 
		(
			(
				(T2.KakuteiJyuni)='01' Or 
				(T2.KakuteiJyuni)='02' Or 
				(T2.KakuteiJyuni)='03' Or 
				(T2.KakuteiJyuni)='04' Or 
				(T2.KakuteiJyuni)='05'
			) 
			AND
			((T1.JyokenCD1)='005' Or (T1.JyokenCD1)='010' Or (T1.JyokenCD1)='016' Or (T1.JyokenCD1)='000') AND 
			((T1.JyokenCD2)='005' Or (T1.JyokenCD2)='010' Or (T1.JyokenCD2)='016' Or (T1.JyokenCD2)='000') AND 
			((T1.JyokenCD3)='005' Or (T1.JyokenCD3)='010' Or (T1.JyokenCD3)='016' Or (T1.JyokenCD3)='000') AND 
			((T1.JyokenCD4)='005' Or (T1.JyokenCD4)='010' Or (T1.JyokenCD4)='016' Or (T1.JyokenCD4)='000') AND 
			((T1.JyokenCD5)='005' Or (T1.JyokenCD5)='010' Or (T1.JyokenCD5)='016' Or (T1.JyokenCD5)='000')
			AND
			(
					( T1.Year='{2}'  OR T1.Year='{3}' )
				AND 
					T1.JyoCD='{4}' 
				AND 
					T1.Kyori='{5}' 
				AND 
					T1.TrackCD='{6}'
				AND 
				(
				(T2.KakuteiJyuni)='01' Or 
				(T2.KakuteiJyuni)='02' Or 
				(T2.KakuteiJyuni)='03' Or 
				(T2.KakuteiJyuni)='04' Or 
				(T2.KakuteiJyuni)='05'
				) 
				AND
				(
				T2.KakuteiJyuni <>'00'
				OR 
				T2.Time <>'0000'
				)
			)
		)

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,	
		y,
		int(y)-1,
		p,
		d,
		t
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	df_temp  = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	else:
		ret['CntVal'] = 0
	return ret


def get_base_time_by_ypdc_to_sr2(accessor, y,p,d,t):
	template= """
		SELECT
			COUNT(*) as CntVal,
			AVG(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as AvgVal,
			STDEVP(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as StdVal,
			AVG(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Avg3fVal,
			STDEVP(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Std3fVal

		FROM {0} as T1 
			INNER  JOIN {1} as T2  
			ON 	(T1.RaceNum = T2.RaceNum) AND 
				(T1.Nichiji = T2.Nichiji) AND
				(T1.Kaiji = T2.Kaiji) AND 
				(T1.JyoCD = T2.JyoCD) AND 
				(T1.Year = T2.Year)
		WHERE 
		(
			((T2.KakuteiJyuni)='01' Or (T2.KakuteiJyuni)='02' Or (T2.KakuteiJyuni)='03') 
			AND
			(
					( T1.Year='{2}'  OR T1.Year='{3}' )
				AND 
					T1.JyoCD='{4}' 
				AND 
					T1.Kyori='{5}' 
				AND 
					T1.TrackCD='{6}'
				AND 
				(
				(T2.KakuteiJyuni)='01' Or 
				(T2.KakuteiJyuni)='02' Or 
				(T2.KakuteiJyuni)='03' Or 
				(T2.KakuteiJyuni)='04' Or 
				(T2.KakuteiJyuni)='05'
				) 
				AND
				(
				T2.KakuteiJyuni <>'00'
				OR 
				T2.Time <>'0000'
				)
			)
		)

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,	
		y,
		int(y)-1,
		p,
		d,
		t
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	df_temp  = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	else:
		ret['CntVal'] = 0
	return ret


def get_base_time_by_ypdc_to_sr3(accessor, y,p,d,t):
	template= """
		SELECT
			COUNT(*) as CntVal,
			AVG(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as AvgVal,
			STDEVP(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as StdVal,
			AVG(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Avg3fVal,
			STDEVP(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Std3fVal

		FROM {0} as T1 
			INNER  JOIN {1} as T2  
			ON 	(T1.RaceNum = T2.RaceNum) AND 
				(T1.Nichiji = T2.Nichiji) AND
				(T1.Kaiji = T2.Kaiji) AND 
				(T1.JyoCD = T2.JyoCD) AND 
				(T1.Year = T2.Year)
		WHERE 
		(
		
				( T1.Year='{2}'  OR T1.Year='{3}' )
			AND 
				T1.JyoCD='{4}' 
			AND 
				T1.Kyori='{5}' 
			AND 
				T1.TrackCD='{6}'
			AND 
				(
				(T2.KakuteiJyuni)='01' Or 
				(T2.KakuteiJyuni)='02' Or 
				(T2.KakuteiJyuni)='03' Or 
				(T2.KakuteiJyuni)='04' Or 
				(T2.KakuteiJyuni)='05'
				) 
			AND
				(
				T2.KakuteiJyuni <>'00'
				OR 
				T2.Time <>'0000'
				)
		)

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,	
		y,
		int(y)-1,
		p,
		d,
		t
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	df_temp  = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	else:
		ret['CntVal'] = 0
	return ret

def get_distance_base_time_by_d_to_sr(accessor, d):
	ret = pd.Series()
	template= """
		SELECT
			COUNT(*) as CntVal,
			AVG(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as AvgVal,
			STDEVP(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as StdVal,
			AVG(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Avg3fVal,
			STDEVP(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Std3fVal

		FROM {0} as T1 
			INNER  JOIN {1} as T2  
			ON 	(T1.RaceNum = T2.RaceNum) AND 
				(T1.Nichiji = T2.Nichiji) AND
				(T1.Kaiji = T2.Kaiji) AND 
				(T1.JyoCD = T2.JyoCD) AND 
				(T1.Year = T2.Year)
		WHERE 
		(
				T1.Kyori='{2}' 
				AND 
				(
				(T2.KakuteiJyuni)='01' Or 
				(T2.KakuteiJyuni)='02' Or 
				(T2.KakuteiJyuni)='03' Or 
				(T2.KakuteiJyuni)='04' Or 
				(T2.KakuteiJyuni)='05'
				) 
		)

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,	
		d,
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	df_temp  = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	else:
		ret['CntVal'] = 0
	return ret
def get_runtime(accessor):
	template = """
		SELECT T1.Year, T1.Monthday, T1.JyoCD, T1.TrackCD, T1.Kyori, T1.RaceNum, T2.KettoNum, T2.Time, T2.Futan,T2.KakuteiJyuni
		FROM {0} as T1 			
			INNER  JOIN {1} as T2  
			ON 	(T1.RaceNum = T2.RaceNum) AND 
				(T1.Nichiji = T2.Nichiji) AND
				(T1.Kaiji = T2.Kaiji) AND 
				(T1.JyoCD = T2.JyoCD) AND 
				(T1.Year = T2.Year)
				
		ORDER BY T1.Year , T1.Monthday

	"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,		
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

	
def get_all_average_time(accessor):
	template = """
		SELECT 
		T1.Year,  
		T1.MonthDay,  
		T1.JyoCD,  
		T1.Kyori, 
		T1.TrackCD, 
		T1.RaceNum,
		COUNT(*) as CntVal,    
		AVG(CAST(SUBSTRING (T2.Time ,1,1) as int)*60 +      CAST(SUBSTRING (T2.Time ,2,2) as int) +     CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0    ) as AvgVal,    
		STDEVP(CAST(SUBSTRING (T2.Time ,1,1) as int)*60 +      CAST(SUBSTRING (T2.Time ,2,2) as int) +     CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0    ) as StdVal,    
		AVG(CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +     CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0    ) as Avg3fVal,    
		STDEVP(CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +     CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0    ) as Std3fVal    
		FROM {0} as T1     
		INNER  JOIN {1} as T2      
		ON  
		(T1.RaceNum = T2.RaceNum) AND      
		(T1.Nichiji = T2.Nichiji) AND     
		(T1.Kaiji = T2.Kaiji) AND      
		(T1.JyoCD = T2.JyoCD) AND      
		(T1.Year = T2.Year)   
		WHERE    
		(
			(T2.KakuteiJyuni)='01' Or 
			(T2.KakuteiJyuni)='02' Or 
			(T2.KakuteiJyuni)='03' Or 
			(T2.KakuteiJyuni)='04' Or 
			(T2.KakuteiJyuni)='05'
		)
		GROUP BY T1.Year, T1.MonthDay, T1.RaceNum, T1.JyoCD, T1.Kyori, T1.TrackCD
		ORDER BY T1.Year ,T1.JyoCD , T1.Kyori , T1.TrackCD , T1.MonthDay ,T1.RaceNum 

	"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,		
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

	
def get_average_time_by_ymdr_to_df(accessor,y, md, race_no):
	template = """
		SELECT 
		T1.Year,  
		T1.MonthDay,  
		T1.JyoCD,  
		T1.Kyori, 
		T1.TrackCD, 
		T1.RaceNum,
		COUNT(*) as CntVal,    
		AVG(CAST(SUBSTRING (T2.Time ,1,1) as int)*60 +      CAST(SUBSTRING (T2.Time ,2,2) as int) +     CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0    ) as AvgVal,    
		STDEVP(CAST(SUBSTRING (T2.Time ,1,1) as int)*60 +      CAST(SUBSTRING (T2.Time ,2,2) as int) +     CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0    ) as StdVal,    
		AVG(CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +     CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0    ) as Avg3fVal,    
		STDEVP(CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +     CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0    ) as Std3fVal    
		FROM {0} as T1     
		INNER  JOIN {1} as T2      
		ON  
		(T1.RaceNum = T2.RaceNum) AND      
		(T1.Nichiji = T2.Nichiji) AND     
		(T1.Kaiji = T2.Kaiji) AND      
		(T1.JyoCD = T2.JyoCD) AND      
		(T1.Year = T2.Year)   
	WHERE
			( 
			T1.JyoCD='01' OR 
			T1.JyoCD='02' OR
			T1.JyoCD='03' OR 
			T1.JyoCD='04' OR 
			T1.JyoCD='05' OR 
			T1.JyoCD='06' OR 
			T1.JyoCD='07' OR 
			T1.JyoCD='08' OR 
			T1.JyoCD='09' OR 
			T1.JyoCD='10' 
			)
			AND
			T1.Year = '{2}'
			AND
			T1.MonthDay='{3}'
			AND
			T1.RaceNum='{4}'
		GROUP BY T1.Year, T1.MonthDay, T1.RaceNum, T1.JyoCD, T1.Kyori, T1.TrackCD
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		y,
		md,
		race_no
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_record_by_ymdh_to_df(accessor,y, md, horse_id):
	template = """
		SELECT 
		T1.Year, 
		T1.MonthDay, 
		T1.JyoCD, 
		T1.RaceNum, 
		T1.Kyori, 
		T1.TrackCD, 
		T2.KettoNum,
		T2.KakuteiJyuni,
		T2.Time,
		T2.Futan,
		T2.HaronTimeL3
		FROM {0} AS T1
		INNER JOIN {1} as T2
		 ON 
		(T1.Kaiji = T2.Kaiji) AND 
		(T1.Nichiji = T2.Nichiji) AND 
		(T1.RaceNum = T2.RaceNum) AND 
		(T1.JyoCD = T2.JyoCD) AND 
		(T1.MonthDay = T2.MonthDay) AND 
		(T1.Year = T2.Year)
		WHERE
			T1.Year = '{2}'
			AND
			T1.MonthDay = '{3}'
			AND
			T2.KettoNum = '{4}'
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		y,
		md,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_record_by_y_to_df(accessor,y):
	template = """
		SELECT 
		T1.Year, 
		T1.MonthDay, 
		T1.JyoCD, 
		T1.RaceNum, 
		T1.Kyori, 
		T1.JyokenCD1,
		T1.JyokenCD2,
		T1.JyokenCD3,
		T1.JyokenCD4,
  		T1.JyokenCD5,
  		T1.SyubetuCD,
		T1.TrackCD, 
  		T1.TenkoCD, 
    	T1.SibaBabaCD, 
     	T1.DirtBabaCD, 
		T2.KettoNum,
		T2.KakuteiJyuni,
		T2.Time,
		T2.Futan,
		T2.HaronTimeL3
		FROM {0} AS T1
		INNER JOIN {1} as T2
		 ON 
		(T1.Kaiji = T2.Kaiji) AND 
		(T1.Nichiji = T2.Nichiji) AND 
		(T1.RaceNum = T2.RaceNum) AND 
		(T1.JyoCD = T2.JyoCD) AND 
		(T1.MonthDay = T2.MonthDay) AND 
		(T1.Year = T2.Year)
		WHERE
			T1.Year = '{2}'
		"""
  
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		y
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_y_m_d_p_kettonum_to_df(accessor):
	template = """
		SELECT  
			[MakeDate],[Year], [MonthDay], [JyoCD], [RaceNum], [KettoNum]
		FROM [kjvan].[dbo].[{0}]
	
		ORDER BY 
			[Year] DESC
			,[MonthDay] DESC

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_at_ymd_to_df(accessor, horse_id):
	template = """
	SELECT distinct([Year]+[MonthDay]+[JyoCD]) as p_id
	FROM [kjvan].[dbo].[{0}]
	WHERE KettoNUM='{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_at_y_to_df(accessor, horse_id):
	template = """
	SELECT distinct([Year]) as y
	FROM [kjvan].[dbo].[{0}]
	WHERE KettoNUM='{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


	#
def get_race_and_horse_id__at_to_df(accessor):
	template = """
	SELECT {0}.[Year], {0}.[MonthDay], {0}.[JyoCD], {0}.[RaceNum], {0}.[KettoNum]
	FROM [kjvan].[dbo].[{0}]
	
	"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


	#
def get_oddsp(accessor):
	template = """
	SELECT 
		{0}.Year+{0}.MonthDay+{0}.JyoCD as pid, 
		{0}.KettoNum, 
		1/NULLIF((CONVERT(int, {0}.Odds)/10.0), 0) as oddsp 
	from {0} 
	
	"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA_RACE
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
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		md, 
		place_code
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_base_time_maiden_race_by_yptd_to_sr(accessor, y,p,t,d):
	template= """
		SELECT
			COUNT(*) as CntVal,
			AVG(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as AvgVal,
			STDEVP(
				CAST(SUBSTRING (T2.Time ,1,1) as int)*60 + 
				CAST(SUBSTRING (T2.Time ,2,2) as int) +
				CAST(SUBSTRING (T2.Time ,4,1) as int)/10.0
			) as StdVal,
			AVG(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Avg3fVal,
			STDEVP(
				CAST(SUBSTRING (T2.HaronTimeL3 ,1,2) as int) +
				CAST(SUBSTRING (T2.HaronTimeL3 ,3,1) as int)/10.0
			) as Std3fVal

		FROM {0} as T1 
			INNER  JOIN {1} as T2  
			ON 	(T1.RaceNum = T2.RaceNum) AND 
				(T1.Nichiji = T2.Nichiji) AND
				(T1.Kaiji = T2.Kaiji) AND 
				(T1.JyoCD = T2.JyoCD) AND 
				(T1.Year = T2.Year)
		WHERE 
		(
			(
				(T2.KakuteiJyuni)='01' Or 
				(T2.KakuteiJyuni)='02' Or 
				(T2.KakuteiJyuni)='03' Or 
				(T2.KakuteiJyuni)='04' Or 
				(T2.KakuteiJyuni)='05'
			) 
			AND
			(
				((T1.JyokenCD1)='701' Or (T1.JyokenCD1)='703' Or (T1.JyokenCD1)='000') AND 
				((T1.JyokenCD2)='701' Or (T1.JyokenCD2)='703' Or (T1.JyokenCD2)='000') AND 
				((T1.JyokenCD3)='701' Or (T1.JyokenCD3)='703' Or (T1.JyokenCD3)='000') AND 
				((T1.JyokenCD4)='701' Or (T1.JyokenCD4)='703' Or (T1.JyokenCD4)='000') AND 
				((T1.JyokenCD5)='701' Or (T1.JyokenCD5)='703' Or (T1.JyokenCD5)='000')
			)
			AND
			(
					T1.Year='{2}' 
				AND 
					T1.JyoCD='{3}' 
				AND 
					T1.Kyori='{4}' 
				AND 
					T1.TrackCD='{5}'
				AND 
				(
				(T2.KakuteiJyuni)='01' Or 
				(T2.KakuteiJyuni)='02' Or 
				(T2.KakuteiJyuni)='03' Or 
				(T2.KakuteiJyuni)='04' Or 
				(T2.KakuteiJyuni)='05'
				) 
				AND
				(
				T2.KakuteiJyuni <>'00'
				OR 
				T2.Time <>'0000'
				)
			)
		)

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,	
		y,
		p,
		d,
		t
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	df_temp  = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	else:
		ret['CntVal'] = 0
	return ret