import pyodbc
import model.conf.KJraConst as const


#
def get_sire_to_df(accessor):
	template = """
		SELECT *
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[SexCD]='1'
		ORDER BY 
			[HansyokuNum]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_HANSYOKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_id_to_df(accessor):
	template = """
		SELECT  [HansyokuNum]
		FROM [kjvan].[dbo].[{0}]
		ORDER BY 
			[HansyokuNum]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_HANSYOKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_sires_stud_scores_to_df(accessor):
	template = """
		SELECT
		dbo.N_HANSYOKU.HansyokuNum as ss_id,
		SUM(CONVERT(int, dbo.N_UMA.SogoChakukaisu1)) as ss_sc1 ,
		SUM(CONVERT(int, dbo.N_UMA.SogoChakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.SogoChakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.SogoChakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.SogoChakukaisu4)+
			CONVERT(int, dbo.N_UMA.SogoChakukaisu5)+
			CONVERT(int, dbo.N_UMA.SogoChakukaisu6)
			) as ss_scT,
		SUM(CONVERT(int, dbo.N_UMA.ChuoChakukaisu1)) as ss_cc1 ,
		SUM(CONVERT(int, dbo.N_UMA.ChuoChakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.ChuoChakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.ChuoChakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.ChuoChakukaisu4)+
			CONVERT(int, dbo.N_UMA.ChuoChakukaisu5)+
			CONVERT(int, dbo.N_UMA.ChuoChakukaisu6)
			) as ss_ccT,
		SUM(CONVERT(int, dbo.N_UMA.Ba1Chakukaisu1)) as ss_tcc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Ba1Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Ba1Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Ba1Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Ba1Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Ba1Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Ba1Chakukaisu6)
			) as ss_tccT,
		SUM(CONVERT(int, dbo.N_UMA.Ba2Chakukaisu1)) as ss_trc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Ba2Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Ba2Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Ba2Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Ba2Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Ba2Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Ba2Chakukaisu6)
			) as ss_trcT,
		SUM(CONVERT(int, dbo.N_UMA.Ba3Chakukaisu1)) as ss_tlc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Ba3Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Ba3Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Ba3Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Ba3Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Ba3Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Ba3Chakukaisu6)
			) as ss_tlcT,
		SUM(CONVERT(int, dbo.N_UMA.Ba4Chakukaisu1)) as ss_dcc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Ba4Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Ba4Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Ba4Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Ba4Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Ba4Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Ba4Chakukaisu6)
			) as ss_dccT,
		SUM(CONVERT(int, dbo.N_UMA.Ba5Chakukaisu1)) as ss_drc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Ba5Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Ba5Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Ba5Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Ba5Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Ba5Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Ba5Chakukaisu6)
			) as ss_drcT,
		SUM(CONVERT(int, dbo.N_UMA.Ba6Chakukaisu1)) as ss_dlc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Ba6Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Ba6Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Ba6Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Ba6Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Ba6Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Ba6Chakukaisu6)
			) as ss_dlcT,
		SUM(CONVERT(int, dbo.N_UMA.Ba7Chakukaisu1)) as ss_olc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Ba7Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Ba7Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Ba7Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Ba7Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Ba7Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Ba7Chakukaisu6)
			) as ss_olcT,
		SUM(CONVERT(int, dbo.N_UMA.Kyori1Chakukaisu1)) as ss_tstc1,
		SUM(CONVERT(int, dbo.N_UMA.Kyori1Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Kyori1Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Kyori1Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Kyori1Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Kyori1Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Kyori1Chakukaisu6)
			) as ss_tstcT,
		SUM(CONVERT(int, dbo.N_UMA.Kyori2Chakukaisu1)) as ss_tmdc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Kyori2Chakukaisu1)+ 
			CONVERT(int, dbo.N_UMA.Kyori2Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Kyori2Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Kyori2Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Kyori2Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Kyori2Chakukaisu6)
			) as  ss_tmdcT,
		SUM(CONVERT(int, dbo.N_UMA.Kyori3Chakukaisu1)) as ss_tlgc1 ,
		SUM(CONVERT(int, dbo.N_UMA.Kyori3Chakukaisu1)+ 
			CONVERT(int, dbo.N_UMA.Kyori3Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Kyori3Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Kyori3Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Kyori3Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Kyori3Chakukaisu6)
			) as  ss_tlgcT,
		SUM(CONVERT(int, dbo.N_UMA.Kyori4Chakukaisu1)) as ss_dstc1,
		SUM(CONVERT(int, dbo.N_UMA.Kyori4Chakukaisu1)+ 	
			CONVERT(int, dbo.N_UMA.Kyori4Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Kyori4Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Kyori4Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Kyori4Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Kyori4Chakukaisu6)
			) as ss_dstcT,
		SUM(CONVERT(int, dbo.N_UMA.Kyori5Chakukaisu1)) as ss_dmdc1,
		SUM(CONVERT(int, dbo.N_UMA.Kyori5Chakukaisu1)+ 
			CONVERT(int, dbo.N_UMA.Kyori5Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Kyori5Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Kyori5Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Kyori5Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Kyori5Chakukaisu6)
			) as  ss_dmdcT,
		SUM(CONVERT(int, dbo.N_UMA.Kyori6Chakukaisu1)) as ss_dlgc1,
		SUM(CONVERT(int, dbo.N_UMA.Kyori6Chakukaisu1)+ 
			CONVERT(int, dbo.N_UMA.Kyori6Chakukaisu2)+ 
			CONVERT(int, dbo.N_UMA.Kyori6Chakukaisu3)+ 
			CONVERT(int, dbo.N_UMA.Kyori6Chakukaisu4)+
			CONVERT(int, dbo.N_UMA.Kyori6Chakukaisu5)+
			CONVERT(int, dbo.N_UMA.Kyori6Chakukaisu6)
			) as  ss_dlgcT
		FROM
		dbo.N_HANSYOKU 
		INNER JOIN dbo.N_UMA 
			ON dbo.N_HANSYOKU.HansyokuNum = dbo.N_UMA.Ketto3InfoHansyokuNum1 
		WHERE
		dbo.N_HANSYOKU.SexCD='1'
		GROUP BY
		dbo.N_HANSYOKU.HansyokuNum
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_HANSYOKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_sire_id_name_to_df(accessor):
	template = """
		SELECT HansyokuNum,Bamei
		FROM [kjvan].[dbo].[{0}]
		WHERE
			[SexCD]='1'
		ORDER BY 
			[HansyokuNum]
		"""
	cmd = template.format(
		const.TBL_KJVAN_N_HANSYOKU
	)
	ret = accessor.read_sql_to_df(cmd)
	return ret