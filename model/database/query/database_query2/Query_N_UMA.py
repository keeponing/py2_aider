import pyodbc
import model.conf.KJraConst as const
import pandas as pd

def get_all_uma_at_to_df(accessor):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		ORDER BY [KettoNum]  DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_active_ducty_uma_at_to_df(accessor):
	template = """
		SELECT *
		FROM [kjvan].[dbo].[{0}]
		WHERE
		  {0}.DelKubun = '0'
		ORDER BY [KettoNum]  DESC
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_uma_at_to_df2(accessor):
	template = """
		SELECT *
		FROM [kjvan].[dbo].[{0}]
		WHERE
			DelKubun='0'
		ORDER BY [KettoNum]  
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_horse_id_by_y_at_to_df(accessor, y):
	template = """
		SELECT  [KettoNum]  
		FROM [kjvan].[dbo].[{0}]
		WHERE [KettoNum] like '{1}%'
		ORDER BY [KettoNum]  
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		y
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret
def get_all_horse_id_at_to_df(accessor):
	template = """
		SELECT  [KettoNum]  
		FROM [kjvan].[dbo].[{0}]
		ORDER BY [KettoNum] 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_horse_id_and_stud_id_at_to_df(accessor):
	template = """
		SELECT  
		KettoNum,
		Ketto3InfoHansyokuNum1,
		Ketto3InfoHansyokuNum2,
		Ketto3InfoHansyokuNum3,
		Ketto3InfoHansyokuNum4,
		Ketto3InfoHansyokuNum5,
		Ketto3InfoHansyokuNum6,
		Ketto3InfoHansyokuNum7,
		Ketto3InfoHansyokuNum8,
		Ketto3InfoHansyokuNum9,
		Ketto3InfoHansyokuNum10,
		Ketto3InfoHansyokuNum11,
		Ketto3InfoHansyokuNum12,
		Ketto3InfoHansyokuNum13,
		Ketto3InfoHansyokuNum14
		FROM [kjvan].[dbo].[{0}]
		ORDER BY [KettoNum] 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_uma_at_to_sr(accessor, horse_id):
	ret = pd.Series()
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]		
		WHERE
			[KettoNum] = '{1}' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		horse_id
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret

#
def get_sire_id_to_sr(accessor, horse_id):
	ret =""
	template = """
		SELECT  [Ketto3InfoHansyokuNum1]
		FROM [kjvan].[dbo].[{0}]		
		WHERE
			[KettoNum] = '{1}' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		horse_id
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]['Ketto3InfoHansyokuNum1']
	return ret

def get_uma_by_sire_id_to_df(accessor, sire_id):
	template = """
		SELECT  *
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[Ketto3InfoHansyokuNum1]='{1}'
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		sire_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_trainer_at_to_df_by_horse_id(accessor, horse_id):
	ret =""
	template = """
		SELECT  [ChokyosiCode]
		FROM [kjvan].[dbo].[{0}]		
		WHERE
			[KettoNum] = '{1}' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		horse_id
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]['ChokyosiCode']
	return ret


def get_feet_by_h_at_to_df(accessor, horse_id):
	template = """
		SELECT  
			{0}.Kyakusitu1,
			{0}.Kyakusitu2,
			{0}.Kyakusitu3,
			{0}.Kyakusitu4
		FROM [kjvan].[dbo].[{0}]		
		WHERE
			[KettoNum] = '{1}' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		horse_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_horse_id_by_stud_id_to_df(accessor, stud_id):
	template = """
		SELECT  
			{0}.KettoNum
		FROM [kjvan].[dbo].[{0}]		
		WHERE
			[Ketto3InfoHansyokuNum1] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum2] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum3] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum4] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum5] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum6] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum7] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum8] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum9] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum10] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum11] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum12] = '{1}' 
			OR
			[Ketto3InfoHansyokuNum13] = '{1}' 		
			OR
			[Ketto3InfoHansyokuNum14] = '{1}' 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		stud_id
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_oldest_horse_id_active_duty(accessor):
	ret = ""
	template = """
		SELECT top 1 [KettoNum]
		FROM [kjvan].[dbo].[{0}]
		WHERE
			DelKubun='0'
		ORDER BY [KettoNum]  
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]['KettoNum']
	return ret


def get_all_sire_id_to_df(accessor):
	template = """
		SELECT  distinct([Ketto3InfoHansyokuNum1])
		FROM [kjvan].[dbo].[{0}]
		ORDER BY [Ketto3InfoHansyokuNum1] 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_bloods_to_sr(accessor, horse_id):
	ret =pd.Series()
	template = """
		SELECT  
			[KettoNum],
			[Ketto3InfoHansyokuNum1] ,
			[Ketto3InfoHansyokuNum2] , 
			[Ketto3InfoHansyokuNum3] , 
			[Ketto3InfoHansyokuNum4] , 
			[Ketto3InfoHansyokuNum5] , 
			[Ketto3InfoHansyokuNum6] , 
			[Ketto3InfoHansyokuNum7] , 
			[Ketto3InfoHansyokuNum8] , 
			[Ketto3InfoHansyokuNum9] , 
			[Ketto3InfoHansyokuNum10] , 
			[Ketto3InfoHansyokuNum11] , 
			[Ketto3InfoHansyokuNum12] , 
			[Ketto3InfoHansyokuNum13] , 
			[Ketto3InfoHansyokuNum14] 
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[KettoNum] = '{1}'
		ORDER BY [KettoNum] 
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_UMA,
		horse_id
	)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret