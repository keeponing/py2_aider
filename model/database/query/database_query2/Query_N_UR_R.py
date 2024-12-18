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
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
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
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
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
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
		horse_id,
		year+md
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_rank_and_distance_still_id_to_df(accessor, horse_id, year, md):
	template= """
		SELECT KakuteiJyuni,Kyori
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
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
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
		const.TBL_KJVAN_N_UMA,
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
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
		const.TBL_KJVAN_N_UMA,
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
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
		const.TBL_KJVAN_N_UMA_RACE,
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
		const.TBL_KJVAN_N_UMA_RACE,
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
		const.TBL_KJVAN_N_UMA_RACE,
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
		const.TBL_KJVAN_N_UMA_RACE,
		year, 
		jockey_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


	
def get_distance_still_id_to_df(accessor, horse_id, year, md):
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
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
		horse_id,
		year+md
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_sire_by_make_date(accessor, make_date):
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
			[{2}].[MakeDate] ='{3}'
		GROUP BY [KettoNum]
		)
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
		make_date
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_sire_score(accessor, sire_id):
	template= """
		SELECT 
  			CAST([{1}].[KakuteiJyuni] AS int) AS rank
		FROM [kjvan].[dbo].[{1}] 
		WHERE [{1}].[KettoNum] IN
		(
			SELECT 
				[KettoNum] 
			FROM 
				[kjvan].[dbo].[{1}] 
			INNER JOIN [kjvan].[dbo].[{2}]
			ON [{1}].[Year] = [{2}].[Year]
				AND
				[{1}].[JyoCD] = [{2}].[JyoCD]
				AND
				[{1}].[MonthDay] = [{2}].[MonthDay]
			WHERE [{1}].[KettoNum] IN
			(
				SELECT 
					[KettoNum] 
				FROM 	
					[{0}]
				WHERE 
					[{0}].[Ketto3InfoHansyokuNum1]='{3}'	
			)
		
		)
			
	"""
	# template= """
	# 	SELECT
	# 		CAST([{1}].[KakuteiJyuni] AS int) AS rank
	# 	FROM [kjvan].[dbo].[{1}]
	# 	WHERE 
	# 	[kjvan].[dbo].[{1}].[KettoNum] IN
	# 	(
	# 	SELECT [KettoNum] FROM [kjvan].[dbo].[{1}]
	# 	INNER JOIN [kjvan].[dbo].[{2}]
	# 	ON [{1}].[Year] = [{2}].[Year]
	# 		AND
	# 		[{1}].[JyoCD] = [{2}].[JyoCD]
	# 		AND
	# 		[{1}].[MonthDay] = [{2}].[MonthDay]
	# 	)
	# 	and
	# 	[kjvan].[dbo].[{0}].[Ketto3InfoHansyokuNum1]='{3}'
	# 	"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		const.TBL_KJVAN_N_UMA_RACE,
		const.TBL_KJVAN_N_RACE,
		sire_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_rank_by_hc_to_df(accessor, horse_id, cls01, cls02, cls03, cls04, cls05):
	template= """	
		SELECT CAST(T2.[KakuteiJyuni] AS int) AS rank FROM {0} as T1  
		INNER JOIN {1} as T2 
		ON T1.Year=T2.Year AND T1.MonthDay = T2.MonthDay AND T1.JyoCD = T2.JyoCD  AND T1.RaceNum = T2.RaceNum 
		WHERE 
			T2.KettoNum='[2}'
			and
				T1.JyokenCD1 = '[3}'
			and
				T1.JyokenCD2 = '[4}'
			and
				T1.JyokenCD3 = '[5}'
			and
				T1.JyokenCD4 = '[6}'
			and		   
				T1.JyokenCD5 = '[7}'
	"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		horse_id,
		cls01,
		cls02,
		cls03,
		cls04,
		cls05
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_dedicated_records_by_toku_num(accessor, toku_num):
	cmd= f"""		
		SELECT
			dbo.N_UMA_RACE.*
		FROM
		N_RACE
		INNER JOIN dbo.N_UMA_RACE
			ON N_RACE.Year = dbo.N_UMA_RACE.Year 
			AND N_RACE.MonthDay = dbo.N_UMA_RACE.MonthDay
			AND N_RACE.JyoCD = dbo.N_UMA_RACE.JyoCD 
			AND N_RACE.Kaiji = dbo.N_UMA_RACE.Kaiji 
			AND N_RACE.Nichiji = dbo.N_UMA_RACE.Nichiji 
			AND N_RACE.RaceNum = dbo.N_UMA_RACE.RaceNum
		WHERE N_RACE.TokuNum='{toku_num}'
		order by N_RACE.Year , N_RACE.MonthDay , N_RACE.JyoCD
	"""

	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_rantime_by_pdt_to_df(accessor,  p, d, t):
	template = """
	SELECT 
		 dbo.{1}.Time 
	FROM
		N_RACE
		INNER JOIN dbo.{1}
			ON dbo.{0}.Year = dbo.{1}.Year 
			AND dbo.{0}.MonthDay = dbo.{1}.MonthDay
			AND dbo.{0}.JyoCD = dbo.{1}.JyoCD 
			AND dbo.{0}.Kaiji = dbo.{1}.Kaiji 
			AND dbo.{0}.Nichiji = dbo.{1}.Nichiji 
			AND dbo.{0}.RaceNum = dbo.{1}.RaceNum
	WHERE 
		{0}.Year ='{2}'
		AND
		{0}.JyoCD ='{3}'
		AND		
		{0}.TrackCD ='{4}'
	"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		const.TBL_KJVAN_N_UMA_RACE,
		p, 
		d, 
		t
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret