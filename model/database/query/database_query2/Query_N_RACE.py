import pyodbc
import model.conf.KJraConst as const

def get_race_to_df(accessor):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		ORDER BY [Year] , [MonthDay] 
		"""
	
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_to_df2(accessor):
	template = """
		SELECT  *
		ORDER BY 
			[Year] DESC
			,[MonthDay] DESC

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_by_year_to_df(accessor, year):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE [Year] ='{1}'
			AND
			([DataKubun] <> '9'OR [DataKubun] <> '0')
		ORDER BY 
			[Year] 
			,[MonthDay] desc
			
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_place_code_by_makedate_to_df(accessor, makedate):
	template = """
		SELECT  
			distinct([JyoCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE [MakeDate] ='{1}'
		ORDER BY 
			[JyoCD]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		makedate
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_by_ymdp_to_df(accessor, year, md, place):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] ='{1}'
			AND
			[MonthDay] ='{2}'
			AND
			[JyoCD] ='{3}'
			AND
			[DataKubun] <> '9'
		ORDER BY 
			[Year] 
			,[MonthDay] desc
			
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year,
		md,
		place
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_by_ymdpr_to_df(accessor, year, md, place, race_no):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] ='{1}'
			AND
			[MonthDay] ='{2}'
			AND
			[JyoCD] ='{3}'
			AND
			[RaceNum]='{4}'
			AND
			[DataKubun] <> '9'
		ORDER BY 
			[Year] 
			,[MonthDay] desc
			
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year,
		md,
		place,
		race_no
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_place_to_df(accessor):
	template = """
		SELECT  distinct([JyoCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_distance_to_df(accessor):
	template = """
		SELECT  distinct([Kyori])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_track_cd_to_df(accessor):
	template = """
		SELECT  distinct([TrackCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[DataKubun] <> '9'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_race_by_year_to_df2(accessor, year):
	template = """
		SELECT  [Year],
				[MonthDay],
				[JyoCD],
				[RaceNum],
				[TenkoCD],
				[TrackCD],
				[Kyori],
				[SibaBabaCD],
				[DirtBabaCD],
				[SyubetuCD],
				[GradeCD],
				[JyokenCD1],
				[JyokenCD2],
				[JyokenCD3],
				[JyokenCD4],
				[JyokenCD5],
				[JyuryoCD]
		FROM [kjvan].[dbo].[{0}]
		WHERE [Year] ={1}
		ORDER BY 
			[Year]
			,[MonthDay]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_race_by_makedate_to_df(accessor, makedate):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE [MakeDate] ='{1}'
		ORDER BY 
			[Year]
			,[MonthDay]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		makedate
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_datakubun_over_2_by_makedate_to_df(accessor, makedate):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[MakeDate] ='{1}'
			and
			[DataKubun] >= '2'
		ORDER BY 
			[Year]
			,[MonthDay]
			,[JyoCD] desc
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		makedate
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_by_makedate_and_md_to_df(accessor, makedate, year, md):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[MakeDate] ='{1}'
			and
			[Year] = '{2}'
			and
			[MonthDay] = '{3}'
		ORDER BY 
			[Year]
			,[MonthDay]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		makedate,
		year,
		md
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_by_year_and_md_to_df(accessor,  year, md, place, race_no):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] = '{1}'
			and
			[MonthDay] = '{2}'
			and
			[RaceNum] = '{3}'
			and
			[JyoCD] = '{4}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year,
		md,
		race_no,
		place
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_race_by_year_and_md_to_df2(accessor,  year, md, place):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] = '{1}'
			and
			[MonthDay] = '{2}'
			and
			[JyoCD] = '{3}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year,
		md,
		place
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret
def get_mean_and_std_condition_code(accessor):
	template = """
		select [JyoCD]+'_'+[Kyori]+'_'+[JyokenCD1]+'_'+[JyokenCD2]+'_'+[JyokenCD3]+'_'+[JyokenCD4]+'_'+[JyokenCD5]+'_'+[SyubetuCD]+'_'+[TrackCD]+'_'+[TenkoCD]+'_'+[SibaBabaCD]+'_'+[DirtBabaCD] as td_id,
		[JyoCD], [Kyori], [JyokenCD1],[JyokenCD2],[JyokenCD3],[JyokenCD4],[JyokenCD5], [SyubetuCD], [TrackCD], [TenkoCD], [SibaBabaCD], [DirtBabaCD]
		from [kjvan].[dbo].[{0}]
		where JyoCD in
		(
		select [JyoCD]
		from [kjvan].[dbo].[{0}]
		group by [JyoCD]
		)
		group by [JyoCD], [Kyori], [JyokenCD1], [JyokenCD2], [JyokenCD3],[JyokenCD4],[JyokenCD5], [SyubetuCD], [TrackCD], [TenkoCD], [SibaBabaCD], [DirtBabaCD]
		order by [JyoCD]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_mean_and_std_condition_code_by_place(accessor, y, md, place):
	template = """
		select [JyoCD]+'_'+[Kyori]+'_'+[JyokenCD1]+'_'+[JyokenCD2]+'_'+[JyokenCD3]+'_'+[JyokenCD4]+'_'+[JyokenCD5]+'_'+[SyubetuCD]+'_'+[TrackCD]+'_'+[TenkoCD]+'_'+[SibaBabaCD]+'_'+[DirtBabaCD] as td_id,
		[JyoCD], [Kyori], [JyokenCD1],[JyokenCD2],[JyokenCD3],[JyokenCD4],[JyokenCD5], [SyubetuCD], [TrackCD], [TenkoCD], [SibaBabaCD], [DirtBabaCD]
		from 
			[kjvan].[dbo].[{0}]
		where 
			[Year] = '{1}'
			and
			[MonthDay] = '{2}'
			and
			[JyoCD] ='{3}'
		group by [JyoCD], [Kyori], [JyokenCD1], [JyokenCD2], [JyokenCD3],[JyokenCD4],[JyokenCD5], [SyubetuCD], [TrackCD], [TenkoCD], [SibaBabaCD], [DirtBabaCD]
		order by [JyoCD]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
		md,
		place
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_current_race_until_tomorrow_to_df(accessor,year, md1):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			
			[Year] = '{1}'
			and
			(
				[MonthDay] = '{2}'
			)
		ORDER BY Year DESC, MonthDay DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year, 
		md1
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_latest_top_n_to_df(accessor, n):
	template = """
		SELECT  top {1} *
		FROM [kjvan].[dbo].[{0}]
			
		ORDER BY Year DESC, MonthDay DESC, RaceNum DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		n
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_current_race_until_today_to_df(accessor,year, md, hm1, hm2):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[DataKubun] ='2'
			and
			[Year] = '{1}'
			and
			[MonthDay] = '{2}'
			and
			(
				CONVERT(int,[HassoTime]) > CONVERT(int,'{3}')
				and 
				CONVERT(int,[HassoTime]) < CONVERT(int,'{4}')
			)
		ORDER BY Year DESC, MonthDay DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year, 
		md, 
		hm1, 
		hm2
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_latest_make_date(accessor):
	ret=""
	template = """
		SELECT distinct([MakeDate])
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[MakeDate] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(0 != len(df_temp)):
		dt_temp = df_temp.iloc[0]
		ret = dt_temp['MakeDate']
	return ret


def get_all_make_date(accessor):
	template = """
		SELECT distinct([MakeDate])
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[MakeDate] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_distances_by_yp(accessor, y, place_cd):
	template = """
		SELECT distinct([Kyori])
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] ='{1}'
			AND
			[JyoCD] = '{2}'
		ORDER BY 
			[Kyori] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
		place_cd
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_places_y(accessor, y):
	template = """
		SELECT distinct([JyoCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] ='{1}'
		ORDER BY 
			[JyoCD] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_track_cd_by_ypd(accessor, y, place_cd, distance):
	template = """
		SELECT distinct([TrackCD])
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] = '{1}'
			AND
			[JyoCD] = '{2}'
			AND
			[Kyori] = '{3}'
		ORDER BY 
			[TrackCD] DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
		place_cd,
		distance
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_all_year(accessor):
	template = """
		SELECT distinct([Year])
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[Year]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret
def get_tecode_bpd_to_df(accessor, program_id, race):
	template = """

	SELECT	
 	CASE jyoCD
		WHEN '01' THEN '01'
		WHEN '02' THEN '02'
		WHEN '03' THEN '03'
		WHEN '04' THEN '04'
		WHEN '05' THEN '05'
		WHEN '06' THEN '06'
		WHEN '07' THEN '07'
		WHEN '08' THEN '08'
		WHEN '09' THEN '09'
		WHEN '10' THEN '10'
		ELSE '99'
		END
	+
	CASE TrackCD 
		WHEN '10'THEN'T'
		WHEN '11'THEN'T'
		WHEN '12'THEN'T'
		WHEN '13'THEN'T'
		WHEN '14'THEN'T'
		WHEN '15'THEN'T'
		WHEN '16'THEN'T'
		WHEN '17'THEN'T'
		WHEN '18'THEN'T'
		WHEN '19'THEN'T'
		WHEN '20'THEN'T'
		WHEN '21'THEN'T'
		WHEN '22'THEN'T'
		WHEN '23'THEN'D'
		WHEN '24'THEN'D'
		WHEN '25'THEN'D'
		WHEN '26'THEN'D'
		WHEN '27'THEN'D'
		WHEN '28'THEN'D'
		WHEN '29'THEN'D'
		WHEN '51'THEN'T'
		WHEN '52'THEN'T'
		WHEN '53'THEN'T'
		WHEN '54'THEN'T'
		WHEN '55'THEN'T'
		WHEN '56'THEN'T'
		WHEN '57'THEN'T'
		WHEN '58'THEN'T'
		WHEN '59'THEN'T'
		ELSE 'EL'
		END 	
	+
	CASE Kyori
		WHEN '0760' THEN '0714'
		WHEN '0800' THEN '0714'
		WHEN '0820' THEN '0714'
		WHEN '0850' THEN '0714'
		WHEN '0900' THEN '0714'
		WHEN '0950' THEN '0714'
		WHEN '1000' THEN '0714'
		WHEN '1010' THEN '0714'
		WHEN '1100' THEN '0714'
		WHEN '1130' THEN '0714'
		WHEN '1150' THEN '0714'
		WHEN '1175' THEN '0714'
		WHEN '1180' THEN '0714'
		WHEN '1190' THEN '0714'
		WHEN '1200' THEN '0714'
		WHEN '1225' THEN '0714'
		WHEN '1230' THEN '0714'
		WHEN '1250' THEN '0714'
		WHEN '1300' THEN '0714'
		WHEN '1330' THEN '0714'
		WHEN '1350' THEN '0714'
		WHEN '1390' THEN '0714'
		WHEN '1400' THEN '0714'
		WHEN '1410' THEN '1418'
		WHEN '1430' THEN '1418'
		WHEN '1445' THEN '1418'
		WHEN '1490' THEN '1418'
		WHEN '1500' THEN '1418'
		WHEN '1550' THEN '1418'
		WHEN '1590' THEN '1418'
		WHEN '1600' THEN '1418'
		WHEN '1620' THEN '1418'
		WHEN '1640' THEN '1418'
		WHEN '1650' THEN '1418'
		WHEN '1660' THEN '1418'
		WHEN '1670' THEN '1418'
		WHEN '1690' THEN '1418'
		WHEN '1700' THEN '1418'
		WHEN '1750' THEN '1418'
		WHEN '1760' THEN '1418'
		WHEN '1777' THEN '1418'
		WHEN '1790' THEN '1418'
		WHEN '1800' THEN '1418'
		WHEN '1856' THEN '1823'
		WHEN '1870' THEN '1823'
		WHEN '1900' THEN '1823'
		WHEN '1950' THEN '1823'
		WHEN '1980' THEN '1823'
		WHEN '1990' THEN '1823'
		WHEN '2000' THEN '1823'
		WHEN '2018' THEN '1823'
		WHEN '2020' THEN '1823'
		WHEN '2025' THEN '1823'
		WHEN '2040' THEN '1823'
		WHEN '2050' THEN '1823'
		WHEN '2080' THEN '1823'
		WHEN '2100' THEN '1823'
		WHEN '2150' THEN '1823'
		WHEN '2200' THEN '1823'
		WHEN '2226' THEN '1823'
		WHEN '2250' THEN '1823'
		WHEN '2300' THEN '1823'
		WHEN '2350' THEN '2330'
		WHEN '2380' THEN '2330'
		WHEN '2390' THEN '2330'
		WHEN '2400' THEN '2330'
		WHEN '2410' THEN '2330'
		WHEN '2418' THEN '2330'
		WHEN '2425' THEN '2330'
		WHEN '2435' THEN '2330'
		WHEN '2450' THEN '2330'
		WHEN '2485' THEN '2330'
		WHEN '2490' THEN '2330'
		WHEN '2500' THEN '2330'
		WHEN '2600' THEN '2330'
		WHEN '2700' THEN '2330'
		WHEN '2750' THEN '2330'
		WHEN '2770' THEN '2330'
		WHEN '2800' THEN '2330'
		WHEN '2850' THEN '2330'
		WHEN '2860' THEN '2330'
		WHEN '2880' THEN '2330'
		WHEN '2890' THEN '2330'
		WHEN '2900' THEN '2330'
		WHEN '2910' THEN '2330'
		WHEN '2920' THEN '2330'
		WHEN '2930' THEN '2330'
		WHEN '2950' THEN '2330'
		WHEN '2970' THEN '2330'
		WHEN '3000' THEN '30OV'
		WHEN '3100' THEN '30OV'
		WHEN '3110' THEN '30OV'
		WHEN '3140' THEN '30OV'
		WHEN '3170' THEN '30OV'
		WHEN '3180' THEN '30OV'
		WHEN '3190' THEN '30OV'
		WHEN '3200' THEN '30OV'
		WHEN '3210' THEN '30OV'
		WHEN '3250' THEN '30OV'
		WHEN '3280' THEN '30OV'
		WHEN '3284' THEN '30OV'
		WHEN '3285' THEN '30OV'
		WHEN '3290' THEN '30OV'
		WHEN '3300' THEN '30OV'
		WHEN '3330' THEN '30OV'
		WHEN '3350' THEN '30OV'
		WHEN '3370' THEN '30OV'
		WHEN '3380' THEN '30OV'
		WHEN '3390' THEN '30OV'
		WHEN '3400' THEN '30OV'
		WHEN '3430' THEN '30OV'
		WHEN '3500' THEN '30OV'
		WHEN '3570' THEN '30OV'
		WHEN '3600' THEN '30OV'
		WHEN '3700' THEN '30OV'
		WHEN '3717' THEN '30OV'
		WHEN '3760' THEN '30OV'
		WHEN '3790' THEN '30OV'
		WHEN '3800' THEN '30OV'
		WHEN '3900' THEN '30OV'
		WHEN '3930' THEN '30OV'
		WHEN '4000' THEN '30OV'
		WHEN '4100' THEN '30OV'
		WHEN '4200' THEN '30OV'
		WHEN '4250' THEN '30OV'
		WHEN '4260' THEN '30OV'
		WHEN '4300' THEN '30OV'
		WHEN '4400' THEN '30OV'
		WHEN '4530' THEN '30OV'
		WHEN '4700' THEN '30OV'
		ELSE '0000'
	    END 	
	AS TeBPDCode
	FROM {0} 
	WHERE
		Year ='{1}'
		AND
		MonthDay='{2}'
		AND
		JyoCD='{3}'
		AND
		RaceNum='{4}'
		"""
	temp =str(program_id)
	y = temp[:4]
	md = temp[4:8]
	place = temp[8:10]
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
		md,
		place,
		race
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_te_bpd_list(accessor):
	template = """

	SELECT	
	DISTINCT(
	CASE jyoCD
		WHEN '01' THEN '01'
		WHEN '02' THEN '02'
		WHEN '03' THEN '03'
		WHEN '04' THEN '04'
		WHEN '05' THEN '05'
		WHEN '06' THEN '06'
		WHEN '07' THEN '07'
		WHEN '08' THEN '08'
		WHEN '09' THEN '09'
		WHEN '10' THEN '10'
		ELSE '99'
		END
	+
	CASE TrackCD 
		WHEN '10'THEN'T'
		WHEN '11'THEN'T'
		WHEN '12'THEN'T'
		WHEN '13'THEN'T'
		WHEN '14'THEN'T'
		WHEN '15'THEN'T'
		WHEN '16'THEN'T'
		WHEN '17'THEN'T'
		WHEN '18'THEN'T'
		WHEN '19'THEN'T'
		WHEN '20'THEN'T'
		WHEN '21'THEN'T'
		WHEN '22'THEN'T'
		WHEN '23'THEN'D'
		WHEN '24'THEN'D'
		WHEN '25'THEN'D'
		WHEN '26'THEN'D'
		WHEN '27'THEN'D'
		WHEN '28'THEN'D'
		WHEN '29'THEN'D'
		WHEN '51'THEN'T'
		WHEN '52'THEN'T'
		WHEN '53'THEN'T'
		WHEN '54'THEN'T'
		WHEN '55'THEN'T'
		WHEN '56'THEN'T'
		WHEN '57'THEN'T'
		WHEN '58'THEN'T'
		WHEN '59'THEN'T'
		ELSE 'EL'
		END 	
	+

	CASE Kyori
		WHEN '0760' THEN '0714'
		WHEN '0800' THEN '0714'
		WHEN '0820' THEN '0714'
		WHEN '0850' THEN '0714'
		WHEN '0900' THEN '0714'
		WHEN '0950' THEN '0714'
		WHEN '1000' THEN '0714'
		WHEN '1010' THEN '0714'
		WHEN '1100' THEN '0714'
		WHEN '1130' THEN '0714'
		WHEN '1150' THEN '0714'
		WHEN '1175' THEN '0714'
		WHEN '1180' THEN '0714'
		WHEN '1190' THEN '0714'
		WHEN '1200' THEN '0714'
		WHEN '1225' THEN '0714'
		WHEN '1230' THEN '0714'
		WHEN '1250' THEN '0714'
		WHEN '1300' THEN '0714'
		WHEN '1330' THEN '0714'
		WHEN '1350' THEN '0714'
		WHEN '1390' THEN '0714'
		WHEN '1400' THEN '0714'
		WHEN '1410' THEN '1418'
		WHEN '1430' THEN '1418'
		WHEN '1445' THEN '1418'
		WHEN '1490' THEN '1418'
		WHEN '1500' THEN '1418'
		WHEN '1550' THEN '1418'
		WHEN '1590' THEN '1418'
		WHEN '1600' THEN '1418'
		WHEN '1620' THEN '1418'
		WHEN '1640' THEN '1418'
		WHEN '1650' THEN '1418'
		WHEN '1660' THEN '1418'
		WHEN '1670' THEN '1418'
		WHEN '1690' THEN '1418'
		WHEN '1700' THEN '1418'
		WHEN '1750' THEN '1418'
		WHEN '1760' THEN '1418'
		WHEN '1777' THEN '1418'
		WHEN '1790' THEN '1418'
		WHEN '1800' THEN '1418'
		WHEN '1856' THEN '1823'
		WHEN '1870' THEN '1823'
		WHEN '1900' THEN '1823'
		WHEN '1950' THEN '1823'
		WHEN '1980' THEN '1823'
		WHEN '1990' THEN '1823'
		WHEN '2000' THEN '1823'
		WHEN '2018' THEN '1823'
		WHEN '2020' THEN '1823'
		WHEN '2025' THEN '1823'
		WHEN '2040' THEN '1823'
		WHEN '2050' THEN '1823'
		WHEN '2080' THEN '1823'
		WHEN '2100' THEN '1823'
		WHEN '2150' THEN '1823'
		WHEN '2200' THEN '1823'
		WHEN '2226' THEN '1823'
		WHEN '2250' THEN '1823'
		WHEN '2300' THEN '1823'
		WHEN '2350' THEN '2330'
		WHEN '2380' THEN '2330'
		WHEN '2390' THEN '2330'
		WHEN '2400' THEN '2330'
		WHEN '2410' THEN '2330'
		WHEN '2418' THEN '2330'
		WHEN '2425' THEN '2330'
		WHEN '2435' THEN '2330'
		WHEN '2450' THEN '2330'
		WHEN '2485' THEN '2330'
		WHEN '2490' THEN '2330'
		WHEN '2500' THEN '2330'
		WHEN '2600' THEN '2330'
		WHEN '2700' THEN '2330'
		WHEN '2750' THEN '2330'
		WHEN '2770' THEN '2330'
		WHEN '2800' THEN '2330'
		WHEN '2850' THEN '2330'
		WHEN '2860' THEN '2330'
		WHEN '2880' THEN '2330'
		WHEN '2890' THEN '2330'
		WHEN '2900' THEN '2330'
		WHEN '2910' THEN '2330'
		WHEN '2920' THEN '2330'
		WHEN '2930' THEN '2330'
		WHEN '2950' THEN '2330'
		WHEN '2970' THEN '2330'
		WHEN '3000' THEN '30OV'
		WHEN '3100' THEN '30OV'
		WHEN '3110' THEN '30OV'
		WHEN '3140' THEN '30OV'
		WHEN '3170' THEN '30OV'
		WHEN '3180' THEN '30OV'
		WHEN '3190' THEN '30OV'
		WHEN '3200' THEN '30OV'
		WHEN '3210' THEN '30OV'
		WHEN '3250' THEN '30OV'
		WHEN '3280' THEN '30OV'
		WHEN '3284' THEN '30OV'
		WHEN '3285' THEN '30OV'
		WHEN '3290' THEN '30OV'
		WHEN '3300' THEN '30OV'
		WHEN '3330' THEN '30OV'
		WHEN '3350' THEN '30OV'
		WHEN '3370' THEN '30OV'
		WHEN '3380' THEN '30OV'
		WHEN '3390' THEN '30OV'
		WHEN '3400' THEN '30OV'
		WHEN '3430' THEN '30OV'
		WHEN '3500' THEN '30OV'
		WHEN '3570' THEN '30OV'
		WHEN '3600' THEN '30OV'
		WHEN '3700' THEN '30OV'
		WHEN '3717' THEN '30OV'
		WHEN '3760' THEN '30OV'
		WHEN '3790' THEN '30OV'
		WHEN '3800' THEN '30OV'
		WHEN '3900' THEN '30OV'
		WHEN '3930' THEN '30OV'
		WHEN '4000' THEN '30OV'
		WHEN '4100' THEN '30OV'
		WHEN '4200' THEN '30OV'
		WHEN '4250' THEN '30OV'
		WHEN '4260' THEN '30OV'
		WHEN '4300' THEN '30OV'
		WHEN '4400' THEN '30OV'
		WHEN '4530' THEN '30OV'
		WHEN '4700' THEN '30OV'
		ELSE '0000'
		END
		)
		AS TeBPDCode
		
		FROM {0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_tecode_bd_to_df(accessor, program_id, race):
	template = """

	SELECT	
	CASE TrackCD 
		WHEN '10'THEN'T'
		WHEN '11'THEN'T'
		WHEN '12'THEN'T'
		WHEN '13'THEN'T'
		WHEN '14'THEN'T'
		WHEN '15'THEN'T'
		WHEN '16'THEN'T'
		WHEN '17'THEN'T'
		WHEN '18'THEN'T'
		WHEN '19'THEN'T'
		WHEN '20'THEN'T'
		WHEN '21'THEN'T'
		WHEN '22'THEN'T'
		WHEN '23'THEN'D'
		WHEN '24'THEN'D'
		WHEN '25'THEN'D'
		WHEN '26'THEN'D'
		WHEN '27'THEN'D'
		WHEN '28'THEN'D'
		WHEN '29'THEN'D'
		WHEN '51'THEN'T'
		WHEN '52'THEN'T'
		WHEN '53'THEN'T'
		WHEN '54'THEN'T'
		WHEN '55'THEN'T'
		WHEN '56'THEN'T'
		WHEN '57'THEN'T'
		WHEN '58'THEN'T'
		WHEN '59'THEN'T'
		ELSE 'EL'
		END 	
	+
	CASE Kyori
		WHEN '0760' THEN '0714'
		WHEN '0800' THEN '0714'
		WHEN '0820' THEN '0714'
		WHEN '0850' THEN '0714'
		WHEN '0900' THEN '0714'
		WHEN '0950' THEN '0714'
		WHEN '1000' THEN '0714'
		WHEN '1010' THEN '0714'
		WHEN '1100' THEN '0714'
		WHEN '1130' THEN '0714'
		WHEN '1150' THEN '0714'
		WHEN '1175' THEN '0714'
		WHEN '1180' THEN '0714'
		WHEN '1190' THEN '0714'
		WHEN '1200' THEN '0714'
		WHEN '1225' THEN '0714'
		WHEN '1230' THEN '0714'
		WHEN '1250' THEN '0714'
		WHEN '1300' THEN '0714'
		WHEN '1330' THEN '0714'
		WHEN '1350' THEN '0714'
		WHEN '1390' THEN '0714'
		WHEN '1400' THEN '0714'
		WHEN '1410' THEN '1418'
		WHEN '1430' THEN '1418'
		WHEN '1445' THEN '1418'
		WHEN '1490' THEN '1418'
		WHEN '1500' THEN '1418'
		WHEN '1550' THEN '1418'
		WHEN '1590' THEN '1418'
		WHEN '1600' THEN '1418'
		WHEN '1620' THEN '1418'
		WHEN '1640' THEN '1418'
		WHEN '1650' THEN '1418'
		WHEN '1660' THEN '1418'
		WHEN '1670' THEN '1418'
		WHEN '1690' THEN '1418'
		WHEN '1700' THEN '1418'
		WHEN '1750' THEN '1418'
		WHEN '1760' THEN '1418'
		WHEN '1777' THEN '1418'
		WHEN '1790' THEN '1418'
		WHEN '1800' THEN '1418'
		WHEN '1856' THEN '1823'
		WHEN '1870' THEN '1823'
		WHEN '1900' THEN '1823'
		WHEN '1950' THEN '1823'
		WHEN '1980' THEN '1823'
		WHEN '1990' THEN '1823'
		WHEN '2000' THEN '1823'
		WHEN '2018' THEN '1823'
		WHEN '2020' THEN '1823'
		WHEN '2025' THEN '1823'
		WHEN '2040' THEN '1823'
		WHEN '2050' THEN '1823'
		WHEN '2080' THEN '1823'
		WHEN '2100' THEN '1823'
		WHEN '2150' THEN '1823'
		WHEN '2200' THEN '1823'
		WHEN '2226' THEN '1823'
		WHEN '2250' THEN '1823'
		WHEN '2300' THEN '1823'
		WHEN '2350' THEN '2330'
		WHEN '2380' THEN '2330'
		WHEN '2390' THEN '2330'
		WHEN '2400' THEN '2330'
		WHEN '2410' THEN '2330'
		WHEN '2418' THEN '2330'
		WHEN '2425' THEN '2330'
		WHEN '2435' THEN '2330'
		WHEN '2450' THEN '2330'
		WHEN '2485' THEN '2330'
		WHEN '2490' THEN '2330'
		WHEN '2500' THEN '2330'
		WHEN '2600' THEN '2330'
		WHEN '2700' THEN '2330'
		WHEN '2750' THEN '2330'
		WHEN '2770' THEN '2330'
		WHEN '2800' THEN '2330'
		WHEN '2850' THEN '2330'
		WHEN '2860' THEN '2330'
		WHEN '2880' THEN '2330'
		WHEN '2890' THEN '2330'
		WHEN '2900' THEN '2330'
		WHEN '2910' THEN '2330'
		WHEN '2920' THEN '2330'
		WHEN '2930' THEN '2330'
		WHEN '2950' THEN '2330'
		WHEN '2970' THEN '2330'
		WHEN '3000' THEN '30OV'
		WHEN '3100' THEN '30OV'
		WHEN '3110' THEN '30OV'
		WHEN '3140' THEN '30OV'
		WHEN '3170' THEN '30OV'
		WHEN '3180' THEN '30OV'
		WHEN '3190' THEN '30OV'
		WHEN '3200' THEN '30OV'
		WHEN '3210' THEN '30OV'
		WHEN '3250' THEN '30OV'
		WHEN '3280' THEN '30OV'
		WHEN '3284' THEN '30OV'
		WHEN '3285' THEN '30OV'
		WHEN '3290' THEN '30OV'
		WHEN '3300' THEN '30OV'
		WHEN '3330' THEN '30OV'
		WHEN '3350' THEN '30OV'
		WHEN '3370' THEN '30OV'
		WHEN '3380' THEN '30OV'
		WHEN '3390' THEN '30OV'
		WHEN '3400' THEN '30OV'
		WHEN '3430' THEN '30OV'
		WHEN '3500' THEN '30OV'
		WHEN '3570' THEN '30OV'
		WHEN '3600' THEN '30OV'
		WHEN '3700' THEN '30OV'
		WHEN '3717' THEN '30OV'
		WHEN '3760' THEN '30OV'
		WHEN '3790' THEN '30OV'
		WHEN '3800' THEN '30OV'
		WHEN '3900' THEN '30OV'
		WHEN '3930' THEN '30OV'
		WHEN '4000' THEN '30OV'
		WHEN '4100' THEN '30OV'
		WHEN '4200' THEN '30OV'
		WHEN '4250' THEN '30OV'
		WHEN '4260' THEN '30OV'
		WHEN '4300' THEN '30OV'
		WHEN '4400' THEN '30OV'
		WHEN '4530' THEN '30OV'
		WHEN '4700' THEN '30OV'
		ELSE '0000'
	    END 	
	AS TeBDCode
	FROM {0} 
	WHERE
		Year ='{1}'
		AND
		MonthDay='{2}'
		AND
		JyoCD='{3}'
		AND
		RaceNum='{4}'
		"""
	temp =str(program_id)
	y = temp[:4]
	md = temp[4:8]
	place = temp[8:10]
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
		md,
		place,
		race
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )		
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_te_bd_list(accessor):
	template = """

	SELECT	
	DISTINCT(
	CASE TrackCD 
		WHEN '10'THEN'T'
		WHEN '11'THEN'T'
		WHEN '12'THEN'T'
		WHEN '13'THEN'T'
		WHEN '14'THEN'T'
		WHEN '15'THEN'T'
		WHEN '16'THEN'T'
		WHEN '17'THEN'T'
		WHEN '18'THEN'T'
		WHEN '19'THEN'T'
		WHEN '20'THEN'T'
		WHEN '21'THEN'T'
		WHEN '22'THEN'T'
		WHEN '23'THEN'D'
		WHEN '24'THEN'D'
		WHEN '25'THEN'D'
		WHEN '26'THEN'D'
		WHEN '27'THEN'D'
		WHEN '28'THEN'D'
		WHEN '29'THEN'D'
		WHEN '51'THEN'T'
		WHEN '52'THEN'T'
		WHEN '53'THEN'T'
		WHEN '54'THEN'T'
		WHEN '55'THEN'T'
		WHEN '56'THEN'T'
		WHEN '57'THEN'T'
		WHEN '58'THEN'T'
		WHEN '59'THEN'T'
		ELSE 'EL'
		END 	
	+

	CASE Kyori
		WHEN '0760' THEN '0714'
		WHEN '0800' THEN '0714'
		WHEN '0820' THEN '0714'
		WHEN '0850' THEN '0714'
		WHEN '0900' THEN '0714'
		WHEN '0950' THEN '0714'
		WHEN '1000' THEN '0714'
		WHEN '1010' THEN '0714'
		WHEN '1100' THEN '0714'
		WHEN '1130' THEN '0714'
		WHEN '1150' THEN '0714'
		WHEN '1175' THEN '0714'
		WHEN '1180' THEN '0714'
		WHEN '1190' THEN '0714'
		WHEN '1200' THEN '0714'
		WHEN '1225' THEN '0714'
		WHEN '1230' THEN '0714'
		WHEN '1250' THEN '0714'
		WHEN '1300' THEN '0714'
		WHEN '1330' THEN '0714'
		WHEN '1350' THEN '0714'
		WHEN '1390' THEN '0714'
		WHEN '1400' THEN '0714'
		WHEN '1410' THEN '1418'
		WHEN '1430' THEN '1418'
		WHEN '1445' THEN '1418'
		WHEN '1490' THEN '1418'
		WHEN '1500' THEN '1418'
		WHEN '1550' THEN '1418'
		WHEN '1590' THEN '1418'
		WHEN '1600' THEN '1418'
		WHEN '1620' THEN '1418'
		WHEN '1640' THEN '1418'
		WHEN '1650' THEN '1418'
		WHEN '1660' THEN '1418'
		WHEN '1670' THEN '1418'
		WHEN '1690' THEN '1418'
		WHEN '1700' THEN '1418'
		WHEN '1750' THEN '1418'
		WHEN '1760' THEN '1418'
		WHEN '1777' THEN '1418'
		WHEN '1790' THEN '1418'
		WHEN '1800' THEN '1418'
		WHEN '1856' THEN '1823'
		WHEN '1870' THEN '1823'
		WHEN '1900' THEN '1823'
		WHEN '1950' THEN '1823'
		WHEN '1980' THEN '1823'
		WHEN '1990' THEN '1823'
		WHEN '2000' THEN '1823'
		WHEN '2018' THEN '1823'
		WHEN '2020' THEN '1823'
		WHEN '2025' THEN '1823'
		WHEN '2040' THEN '1823'
		WHEN '2050' THEN '1823'
		WHEN '2080' THEN '1823'
		WHEN '2100' THEN '1823'
		WHEN '2150' THEN '1823'
		WHEN '2200' THEN '1823'
		WHEN '2226' THEN '1823'
		WHEN '2250' THEN '1823'
		WHEN '2300' THEN '1823'
		WHEN '2350' THEN '2330'
		WHEN '2380' THEN '2330'
		WHEN '2390' THEN '2330'
		WHEN '2400' THEN '2330'
		WHEN '2410' THEN '2330'
		WHEN '2418' THEN '2330'
		WHEN '2425' THEN '2330'
		WHEN '2435' THEN '2330'
		WHEN '2450' THEN '2330'
		WHEN '2485' THEN '2330'
		WHEN '2490' THEN '2330'
		WHEN '2500' THEN '2330'
		WHEN '2600' THEN '2330'
		WHEN '2700' THEN '2330'
		WHEN '2750' THEN '2330'
		WHEN '2770' THEN '2330'
		WHEN '2800' THEN '2330'
		WHEN '2850' THEN '2330'
		WHEN '2860' THEN '2330'
		WHEN '2880' THEN '2330'
		WHEN '2890' THEN '2330'
		WHEN '2900' THEN '2330'
		WHEN '2910' THEN '2330'
		WHEN '2920' THEN '2330'
		WHEN '2930' THEN '2330'
		WHEN '2950' THEN '2330'
		WHEN '2970' THEN '2330'
		WHEN '3000' THEN '30OV'
		WHEN '3100' THEN '30OV'
		WHEN '3110' THEN '30OV'
		WHEN '3140' THEN '30OV'
		WHEN '3170' THEN '30OV'
		WHEN '3180' THEN '30OV'
		WHEN '3190' THEN '30OV'
		WHEN '3200' THEN '30OV'
		WHEN '3210' THEN '30OV'
		WHEN '3250' THEN '30OV'
		WHEN '3280' THEN '30OV'
		WHEN '3284' THEN '30OV'
		WHEN '3285' THEN '30OV'
		WHEN '3290' THEN '30OV'
		WHEN '3300' THEN '30OV'
		WHEN '3330' THEN '30OV'
		WHEN '3350' THEN '30OV'
		WHEN '3370' THEN '30OV'
		WHEN '3380' THEN '30OV'
		WHEN '3390' THEN '30OV'
		WHEN '3400' THEN '30OV'
		WHEN '3430' THEN '30OV'
		WHEN '3500' THEN '30OV'
		WHEN '3570' THEN '30OV'
		WHEN '3600' THEN '30OV'
		WHEN '3700' THEN '30OV'
		WHEN '3717' THEN '30OV'
		WHEN '3760' THEN '30OV'
		WHEN '3790' THEN '30OV'
		WHEN '3800' THEN '30OV'
		WHEN '3900' THEN '30OV'
		WHEN '3930' THEN '30OV'
		WHEN '4000' THEN '30OV'
		WHEN '4100' THEN '30OV'
		WHEN '4200' THEN '30OV'
		WHEN '4250' THEN '30OV'
		WHEN '4260' THEN '30OV'
		WHEN '4300' THEN '30OV'
		WHEN '4400' THEN '30OV'
		WHEN '4530' THEN '30OV'
		WHEN '4700' THEN '30OV'
		ELSE '0000'
		END
		)
		AS TeBDCode
		
		FROM {0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )		
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_tecode_c_to_df(accessor, program_id, race):
	template = """
	SELECT	
	({0}.JyokenCD1+{0}.JyokenCD2+{0}.JyokenCD3+{0}.JyokenCD4+{0}.JyokenCD5)
	AS TeCCode
	FROM {0}
	WHERE
		Year ='{1}'
		AND
		MonthDay='{2}'
		AND
		JyoCD='{3}'
		AND
		RaceNum='{4}'
		"""
	temp =str(program_id)
	y = temp[:4]
	md = temp[4:8]
	place = temp[8:10]
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
		md,
		place,
		race
	)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )		
	ret = accessor.read_sql_to_df(cmd)

	return ret


def get_te_c_list(accessor):
	template = """

		SELECT	
		DISTINCT(
		({0}.JyokenCD1+{0}.JyokenCD2+{0}.JyokenCD3+{0}.JyokenCD4+{0}.JyokenCD5)
		)
		AS TeCCode
		FROM {0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_tecode_bpds_to_df(accessor, program_id, race):
	template = """

	SELECT	
 	CASE jyoCD
		WHEN '01' THEN '01'
		WHEN '02' THEN '02'
		WHEN '03' THEN '03'
		WHEN '04' THEN '04'
		WHEN '05' THEN '05'
		WHEN '06' THEN '06'
		WHEN '07' THEN '07'
		WHEN '08' THEN '08'
		WHEN '09' THEN '09'
		WHEN '10' THEN '10'
		ELSE '99'
		END
	+
	CASE TrackCD 
		WHEN '10'THEN'T'
		WHEN '11'THEN'T'
		WHEN '12'THEN'T'
		WHEN '13'THEN'T'
		WHEN '14'THEN'T'
		WHEN '15'THEN'T'
		WHEN '16'THEN'T'
		WHEN '17'THEN'T'
		WHEN '18'THEN'T'
		WHEN '19'THEN'T'
		WHEN '20'THEN'T'
		WHEN '21'THEN'T'
		WHEN '22'THEN'T'
		WHEN '23'THEN'D'
		WHEN '24'THEN'D'
		WHEN '25'THEN'D'
		WHEN '26'THEN'D'
		WHEN '27'THEN'D'
		WHEN '28'THEN'D'
		WHEN '29'THEN'D'
		WHEN '51'THEN'T'
		WHEN '52'THEN'T'
		WHEN '53'THEN'T'
		WHEN '54'THEN'T'
		WHEN '55'THEN'T'
		WHEN '56'THEN'T'
		WHEN '57'THEN'T'
		WHEN '58'THEN'T'
		WHEN '59'THEN'T'
		ELSE 'EL'
		END 	
	+
	CASE Kyori
		WHEN '0760' THEN '0714'
		WHEN '0800' THEN '0714'
		WHEN '0820' THEN '0714'
		WHEN '0850' THEN '0714'
		WHEN '0900' THEN '0714'
		WHEN '0950' THEN '0714'
		WHEN '1000' THEN '0714'
		WHEN '1010' THEN '0714'
		WHEN '1100' THEN '0714'
		WHEN '1130' THEN '0714'
		WHEN '1150' THEN '0714'
		WHEN '1175' THEN '0714'
		WHEN '1180' THEN '0714'
		WHEN '1190' THEN '0714'
		WHEN '1200' THEN '0714'
		WHEN '1225' THEN '0714'
		WHEN '1230' THEN '0714'
		WHEN '1250' THEN '0714'
		WHEN '1300' THEN '0714'
		WHEN '1330' THEN '0714'
		WHEN '1350' THEN '0714'
		WHEN '1390' THEN '0714'
		WHEN '1400' THEN '0714'
		WHEN '1410' THEN '1418'
		WHEN '1430' THEN '1418'
		WHEN '1445' THEN '1418'
		WHEN '1490' THEN '1418'
		WHEN '1500' THEN '1418'
		WHEN '1550' THEN '1418'
		WHEN '1590' THEN '1418'
		WHEN '1600' THEN '1418'
		WHEN '1620' THEN '1418'
		WHEN '1640' THEN '1418'
		WHEN '1650' THEN '1418'
		WHEN '1660' THEN '1418'
		WHEN '1670' THEN '1418'
		WHEN '1690' THEN '1418'
		WHEN '1700' THEN '1418'
		WHEN '1750' THEN '1418'
		WHEN '1760' THEN '1418'
		WHEN '1777' THEN '1418'
		WHEN '1790' THEN '1418'
		WHEN '1800' THEN '1418'
		WHEN '1856' THEN '1823'
		WHEN '1870' THEN '1823'
		WHEN '1900' THEN '1823'
		WHEN '1950' THEN '1823'
		WHEN '1980' THEN '1823'
		WHEN '1990' THEN '1823'
		WHEN '2000' THEN '1823'
		WHEN '2018' THEN '1823'
		WHEN '2020' THEN '1823'
		WHEN '2025' THEN '1823'
		WHEN '2040' THEN '1823'
		WHEN '2050' THEN '1823'
		WHEN '2080' THEN '1823'
		WHEN '2100' THEN '1823'
		WHEN '2150' THEN '1823'
		WHEN '2200' THEN '1823'
		WHEN '2226' THEN '1823'
		WHEN '2250' THEN '1823'
		WHEN '2300' THEN '1823'
		WHEN '2350' THEN '2330'
		WHEN '2380' THEN '2330'
		WHEN '2390' THEN '2330'
		WHEN '2400' THEN '2330'
		WHEN '2410' THEN '2330'
		WHEN '2418' THEN '2330'
		WHEN '2425' THEN '2330'
		WHEN '2435' THEN '2330'
		WHEN '2450' THEN '2330'
		WHEN '2485' THEN '2330'
		WHEN '2490' THEN '2330'
		WHEN '2500' THEN '2330'
		WHEN '2600' THEN '2330'
		WHEN '2700' THEN '2330'
		WHEN '2750' THEN '2330'
		WHEN '2770' THEN '2330'
		WHEN '2800' THEN '2330'
		WHEN '2850' THEN '2330'
		WHEN '2860' THEN '2330'
		WHEN '2880' THEN '2330'
		WHEN '2890' THEN '2330'
		WHEN '2900' THEN '2330'
		WHEN '2910' THEN '2330'
		WHEN '2920' THEN '2330'
		WHEN '2930' THEN '2330'
		WHEN '2950' THEN '2330'
		WHEN '2970' THEN '2330'
		WHEN '3000' THEN '30OV'
		WHEN '3100' THEN '30OV'
		WHEN '3110' THEN '30OV'
		WHEN '3140' THEN '30OV'
		WHEN '3170' THEN '30OV'
		WHEN '3180' THEN '30OV'
		WHEN '3190' THEN '30OV'
		WHEN '3200' THEN '30OV'
		WHEN '3210' THEN '30OV'
		WHEN '3250' THEN '30OV'
		WHEN '3280' THEN '30OV'
		WHEN '3284' THEN '30OV'
		WHEN '3285' THEN '30OV'
		WHEN '3290' THEN '30OV'
		WHEN '3300' THEN '30OV'
		WHEN '3330' THEN '30OV'
		WHEN '3350' THEN '30OV'
		WHEN '3370' THEN '30OV'
		WHEN '3380' THEN '30OV'
		WHEN '3390' THEN '30OV'
		WHEN '3400' THEN '30OV'
		WHEN '3430' THEN '30OV'
		WHEN '3500' THEN '30OV'
		WHEN '3570' THEN '30OV'
		WHEN '3600' THEN '30OV'
		WHEN '3700' THEN '30OV'
		WHEN '3717' THEN '30OV'
		WHEN '3760' THEN '30OV'
		WHEN '3790' THEN '30OV'
		WHEN '3800' THEN '30OV'
		WHEN '3900' THEN '30OV'
		WHEN '3930' THEN '30OV'
		WHEN '4000' THEN '30OV'
		WHEN '4100' THEN '30OV'
		WHEN '4200' THEN '30OV'
		WHEN '4250' THEN '30OV'
		WHEN '4260' THEN '30OV'
		WHEN '4300' THEN '30OV'
		WHEN '4400' THEN '30OV'
		WHEN '4530' THEN '30OV'
		WHEN '4700' THEN '30OV'
		ELSE '0000'
	    END 
	+
		TokuNum	
	AS TeBPDSCode
	FROM {0} 
	WHERE
		Year ='{1}'
		AND
		MonthDay='{2}'
		AND
		JyoCD='{3}'
		AND
		RaceNum='{4}'
		"""
	temp =str(program_id)
	y = temp[:4]
	md = temp[4:8]
	place = temp[8:10]
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
		md,
		place,
		race
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_tecode_bpds_list(accessor):
	template = """

	SELECT	
	DISTINCT(
	CASE jyoCD
		WHEN '01' THEN '01'
		WHEN '02' THEN '02'
		WHEN '03' THEN '03'
		WHEN '04' THEN '04'
		WHEN '05' THEN '05'
		WHEN '06' THEN '06'
		WHEN '07' THEN '07'
		WHEN '08' THEN '08'
		WHEN '09' THEN '09'
		WHEN '10' THEN '10'
		ELSE '99'
		END
	+
	CASE TrackCD 
		WHEN '10'THEN'T'
		WHEN '11'THEN'T'
		WHEN '12'THEN'T'
		WHEN '13'THEN'T'
		WHEN '14'THEN'T'
		WHEN '15'THEN'T'
		WHEN '16'THEN'T'
		WHEN '17'THEN'T'
		WHEN '18'THEN'T'
		WHEN '19'THEN'T'
		WHEN '20'THEN'T'
		WHEN '21'THEN'T'
		WHEN '22'THEN'T'
		WHEN '23'THEN'D'
		WHEN '24'THEN'D'
		WHEN '25'THEN'D'
		WHEN '26'THEN'D'
		WHEN '27'THEN'D'
		WHEN '28'THEN'D'
		WHEN '29'THEN'D'
		WHEN '51'THEN'T'
		WHEN '52'THEN'T'
		WHEN '53'THEN'T'
		WHEN '54'THEN'T'
		WHEN '55'THEN'T'
		WHEN '56'THEN'T'
		WHEN '57'THEN'T'
		WHEN '58'THEN'T'
		WHEN '59'THEN'T'
		ELSE 'EL'
		END 	
	+

	CASE Kyori
		WHEN '0760' THEN '0714'
		WHEN '0800' THEN '0714'
		WHEN '0820' THEN '0714'
		WHEN '0850' THEN '0714'
		WHEN '0900' THEN '0714'
		WHEN '0950' THEN '0714'
		WHEN '1000' THEN '0714'
		WHEN '1010' THEN '0714'
		WHEN '1100' THEN '0714'
		WHEN '1130' THEN '0714'
		WHEN '1150' THEN '0714'
		WHEN '1175' THEN '0714'
		WHEN '1180' THEN '0714'
		WHEN '1190' THEN '0714'
		WHEN '1200' THEN '0714'
		WHEN '1225' THEN '0714'
		WHEN '1230' THEN '0714'
		WHEN '1250' THEN '0714'
		WHEN '1300' THEN '0714'
		WHEN '1330' THEN '0714'
		WHEN '1350' THEN '0714'
		WHEN '1390' THEN '0714'
		WHEN '1400' THEN '0714'
		WHEN '1410' THEN '1418'
		WHEN '1430' THEN '1418'
		WHEN '1445' THEN '1418'
		WHEN '1490' THEN '1418'
		WHEN '1500' THEN '1418'
		WHEN '1550' THEN '1418'
		WHEN '1590' THEN '1418'
		WHEN '1600' THEN '1418'
		WHEN '1620' THEN '1418'
		WHEN '1640' THEN '1418'
		WHEN '1650' THEN '1418'
		WHEN '1660' THEN '1418'
		WHEN '1670' THEN '1418'
		WHEN '1690' THEN '1418'
		WHEN '1700' THEN '1418'
		WHEN '1750' THEN '1418'
		WHEN '1760' THEN '1418'
		WHEN '1777' THEN '1418'
		WHEN '1790' THEN '1418'
		WHEN '1800' THEN '1418'
		WHEN '1856' THEN '1823'
		WHEN '1870' THEN '1823'
		WHEN '1900' THEN '1823'
		WHEN '1950' THEN '1823'
		WHEN '1980' THEN '1823'
		WHEN '1990' THEN '1823'
		WHEN '2000' THEN '1823'
		WHEN '2018' THEN '1823'
		WHEN '2020' THEN '1823'
		WHEN '2025' THEN '1823'
		WHEN '2040' THEN '1823'
		WHEN '2050' THEN '1823'
		WHEN '2080' THEN '1823'
		WHEN '2100' THEN '1823'
		WHEN '2150' THEN '1823'
		WHEN '2200' THEN '1823'
		WHEN '2226' THEN '1823'
		WHEN '2250' THEN '1823'
		WHEN '2300' THEN '1823'
		WHEN '2350' THEN '2330'
		WHEN '2380' THEN '2330'
		WHEN '2390' THEN '2330'
		WHEN '2400' THEN '2330'
		WHEN '2410' THEN '2330'
		WHEN '2418' THEN '2330'
		WHEN '2425' THEN '2330'
		WHEN '2435' THEN '2330'
		WHEN '2450' THEN '2330'
		WHEN '2485' THEN '2330'
		WHEN '2490' THEN '2330'
		WHEN '2500' THEN '2330'
		WHEN '2600' THEN '2330'
		WHEN '2700' THEN '2330'
		WHEN '2750' THEN '2330'
		WHEN '2770' THEN '2330'
		WHEN '2800' THEN '2330'
		WHEN '2850' THEN '2330'
		WHEN '2860' THEN '2330'
		WHEN '2880' THEN '2330'
		WHEN '2890' THEN '2330'
		WHEN '2900' THEN '2330'
		WHEN '2910' THEN '2330'
		WHEN '2920' THEN '2330'
		WHEN '2930' THEN '2330'
		WHEN '2950' THEN '2330'
		WHEN '2970' THEN '2330'
		WHEN '3000' THEN '30OV'
		WHEN '3100' THEN '30OV'
		WHEN '3110' THEN '30OV'
		WHEN '3140' THEN '30OV'
		WHEN '3170' THEN '30OV'
		WHEN '3180' THEN '30OV'
		WHEN '3190' THEN '30OV'
		WHEN '3200' THEN '30OV'
		WHEN '3210' THEN '30OV'
		WHEN '3250' THEN '30OV'
		WHEN '3280' THEN '30OV'
		WHEN '3284' THEN '30OV'
		WHEN '3285' THEN '30OV'
		WHEN '3290' THEN '30OV'
		WHEN '3300' THEN '30OV'
		WHEN '3330' THEN '30OV'
		WHEN '3350' THEN '30OV'
		WHEN '3370' THEN '30OV'
		WHEN '3380' THEN '30OV'
		WHEN '3390' THEN '30OV'
		WHEN '3400' THEN '30OV'
		WHEN '3430' THEN '30OV'
		WHEN '3500' THEN '30OV'
		WHEN '3570' THEN '30OV'
		WHEN '3600' THEN '30OV'
		WHEN '3700' THEN '30OV'
		WHEN '3717' THEN '30OV'
		WHEN '3760' THEN '30OV'
		WHEN '3790' THEN '30OV'
		WHEN '3800' THEN '30OV'
		WHEN '3900' THEN '30OV'
		WHEN '3930' THEN '30OV'
		WHEN '4000' THEN '30OV'
		WHEN '4100' THEN '30OV'
		WHEN '4200' THEN '30OV'
		WHEN '4250' THEN '30OV'
		WHEN '4260' THEN '30OV'
		WHEN '4300' THEN '30OV'
		WHEN '4400' THEN '30OV'
		WHEN '4530' THEN '30OV'
		WHEN '4700' THEN '30OV'
		ELSE '0000'
		END
	+
	TokuNum
	)
	AS TeBPDSCode
	
	FROM {0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_tokunum_by_ymdp(accessor, year, md, place, race_no):
	template = """
		SELECT  [TokuNum]
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] ='{1}'
			AND
			[MonthDay] ='{2}'
			AND
			[JyoCD] ='{3}'
			AND
			[RaceNum] ='{4}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year,
		md,
		place,
		race_no
	)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = '0000'
	if(len(df_temp)):
		ret = df_temp.iloc[0]['TokuNum']
	return ret

def get_dpt_by_ymdp(accessor, y):
	template = """
		select distinct JyoCD, Kyori, TrackCD 
		FROM [kjvan].[dbo].[{0}]
		WHERE 
			[Year] ='{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		y,
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_place_track_distance_by_year_to_df(accessor, year):
	template = """
		SELECT  
			distinct JyoCD, TrackCD, Kyori
		FROM [kjvan].[dbo].[{0}]
		WHERE [Year] ='{1}'
			AND
			(JyoCD ='01' or
			JyoCD ='02' or
			JyoCD ='03' or
			JyoCD ='04' or
			JyoCD ='05' or
			JyoCD ='06' or
			JyoCD ='07' or
			JyoCD ='08' or
			JyoCD ='09' or
			JyoCD ='10')

		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		year
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_place_id_to_list(accessor):
	ret = []
	template = """
		select 
			distinct([JyoCD])
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_RACE,
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp['JyoCD'].to_list()
	return ret