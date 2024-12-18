import pyodbc
import model.conf.KJraConst as const

def get_results_still_id_to_df(accessor, horse_id, year, md):
	template= """
		SELECT * 
		FROM [kjvan].[dbo].[{0}] as T1  
		INNER JOIN [kjvan].[dbo].[{1}] as T2 
		ON T1.Year=T2.Year 
			AND 
			T1.MonthDay = T2.MonthDay 
			AND
			T1.JyoCD = T2.JyoCD
			AND
			T1.RaceNum = T2.RaceNum
		WHERE
			T1.KettoNum='{2}' 
			AND
			CONVERT(decimal, T2.Year+T2.MonthDay) < {3} 
		ORDER BY 
			CONVERT(decimal, T2.Year+T2.MonthDay) DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		const.TBL_KJVAN_S_RACE,
		horse_id,
		year+md
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_prev_distance_to_df(accessor, horse_id, year, md):
	template= """
		SELECT Kyori
		FROM [kjvan].[dbo].[{0}] as T1  
		INNER JOIN [kjvan].[dbo].[{1}] as T2 
		ON T1.Year=T2.Year 
			AND 
			T1.MonthDay = T2.MonthDay 
			AND
			T1.JyoCD = T2.JyoCD
			AND
			T1.RaceNum = T2.RaceNum
		WHERE
			T1.KettoNum='{2}' 
			AND
			CONVERT(decimal, T2.Year+T2.MonthDay) < {3} 
		ORDER BY 
			CONVERT(decimal, T2.Year+T2.MonthDay) DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		const.TBL_KJVAN_S_RACE,
		horse_id,
		year+md
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_results_still_id_to_df2(accessor, horse_id, year, md):
	template= """
		SELECT *
		FROM [kjvan].[dbo].[{0}] as T1  
		INNER JOIN [kjvan].[dbo].[{1}] as T2 
		ON T1.Year=T2.Year 
			AND 
			T1.MonthDay = T2.MonthDay 
			AND
			T1.JyoCD = T2.JyoCD
			AND
			T1.RaceNum = T2.RaceNum
		WHERE
			T1.KettoNum='{2}' 
			AND
			CONVERT(decimal, T2.Year+T2.MonthDay) < {3} 
		ORDER BY 
			CONVERT(decimal, T2.Year+T2.MonthDay) DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		const.TBL_KJVAN_S_RACE,
		horse_id,
		year+md
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_sire_by_yptd(accessor, year, place, track, distance):
	template= """
		SELECT distinct([{0}].[Ketto3InfoHansyokuNum1]) as sire_id
		FROM [kjvan].[dbo].[{0}]
		WHERE [{0}].[KettoNum] IN
		(
		SELECT [KettoNum] FROM [kjvan].[dbo].[{1}]
		INNER JOIN [kjvan].[dbo].[{2}]
		ON [{1}].[Year] = [{2}].[Year]
			AND
			[{1}].[JyoCD] = [{2}].[JyoCD]
			AND
			[{1}].[MonthDay] = [{2}].[MonthDay]
		WHERE 
			[{2}].[Year] ='{3}'
			AND
			[{2}].[JyoCD] ='{4}'
			AND
			[{2}].[TrackCD]='{5}'
			AND
			[{2}].[Kyori]='{6}'
		GROUP BY [KettoNum]
		)
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA,
		const.TBL_KJVAN_S_UMA_RACE,
		const.TBL_KJVAN_S_RACE,
		year, 
		place, 
		track, 
		distance
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_rank_by_sire_id(accessor, year, place, track, distance, sire_id):
	template= """
		SELECT CAST([{1}].[KakuteiJyuni] AS int) AS rank
		FROM [kjvan].[dbo].[{0}]
		INNER JOIN [kjvan].[dbo].[{1}] 
			ON [{0}].[KettoNum] =[{1}].[KettoNum]
		INNER JOIN [kjvan].[dbo].[{2}] 
			ON 
			[{2}].[Year] = [{1}].[Year]
			AND
			[{2}].[JyoCD] = [{1}].[JyoCD]
			AND
			[{2}].[MonthDay] = [{1}].[MonthDay]
					
		WHERE 
			[{0}].[Ketto3InfoHansyokuNum1]='{7}'
			AND
			[{2}].[Year]='{3}'
			AND
			[{2}].[JyoCD]='{4}'
			AND
			[{2}].[TrackCD]='{5}'
			AND
			[{2}].[Kyori]='{6}'
			AND
			[{1}].[IJyoCD]='0'
	"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA,
		const.TBL_KJVAN_S_UMA_RACE,
		const.TBL_KJVAN_S_RACE,
		year, 
		place, 
		track, 
		distance,
		sire_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_trainer_by_year(accessor, year):
	template= """
		SELECT distinct([{0}].[ChokyosiCode]) as trainer_id
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[{0}].[Year] = '{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_rank_by_trainer_id(accessor, year, trainer_id):
	template= """
		SELECT CAST([{0}].[KakuteiJyuni] AS int) AS rank
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[{0}].[ChokyosiCode]='{2}'
			AND
			[{0}].[Year]='{1}'
			AND
			[{0}].[IJyoCD]='0'
	"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year, 
		trainer_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_jockey_by_year(accessor, year):
	template= """
		SELECT distinct([{0}].[KisyuCode]) as jockey_id
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[{0}].[Year] = '{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_rank_by_jockey_id(accessor, year, jockey_id):
	template= """
		SELECT CAST([{0}].[KakuteiJyuni] AS int) AS rank
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[{0}].[KisyuCode]='{2}'
			AND
			[{0}].[Year]='{1}'
			AND
			[{0}].[IJyoCD]='0'
	"""
	cmd = template.format(
		const.TBL_KJVAN_S_UMA_RACE,
		year, 
		jockey_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret