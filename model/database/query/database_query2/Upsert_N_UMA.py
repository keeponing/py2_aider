import os
import inspect
from model.conf.KJraConfig import TRAIN_FILE_PATH
import model.conf.KJraConst as const


def upsert(accessor, input):
	ret =False
	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				KettoNum='{1}' 
			"""
		cmd = template.format(
			const.TBL_KJVAN_N_UMA,
			input['KettoNum']	
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , '' )
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			if(count!=0):                
				break	  
		if 0 ==  count:  
			cmd = f"""
                  INSERT INTO [{const.TBL_KJVAN_N_UMA}]
                        ([RecordSpec]
                        ,[DataKubun]
                        ,[MakeDate]
                        ,[KettoNum]
                        ,[DelKubun]
                        ,[RegDate]
                        ,[DelDate]
                        ,[BirthDate]
                        ,[Bamei]
                        ,[BameiKana]
                        ,[BameiEng]
                        ,[ZaikyuFlag]
                        ,[Reserved]
                        ,[UmaKigoCD]
                        ,[SexCD]
                        ,[HinsyuCD]
                        ,[KeiroCD]
                        ,[Ketto3InfoHansyokuNum1]
                        ,[Ketto3InfoBamei1]
                        ,[Ketto3InfoHansyokuNum2]
                        ,[Ketto3InfoBamei2]
                        ,[Ketto3InfoHansyokuNum3]
                        ,[Ketto3InfoBamei3]
                        ,[Ketto3InfoHansyokuNum4]
                        ,[Ketto3InfoBamei4]
                        ,[Ketto3InfoHansyokuNum5]
                        ,[Ketto3InfoBamei5]
                        ,[Ketto3InfoHansyokuNum6]
                        ,[Ketto3InfoBamei6]
                        ,[Ketto3InfoHansyokuNum7]
                        ,[Ketto3InfoBamei7]
                        ,[Ketto3InfoHansyokuNum8]
                        ,[Ketto3InfoBamei8]
                        ,[Ketto3InfoHansyokuNum9]
                        ,[Ketto3InfoBamei9]
                        ,[Ketto3InfoHansyokuNum10]
                        ,[Ketto3InfoBamei10]
                        ,[Ketto3InfoHansyokuNum11]
                        ,[Ketto3InfoBamei11]
                        ,[Ketto3InfoHansyokuNum12]
                        ,[Ketto3InfoBamei12]
                        ,[Ketto3InfoHansyokuNum13]
                        ,[Ketto3InfoBamei13]
                        ,[Ketto3InfoHansyokuNum14]
                        ,[Ketto3InfoBamei14]
                        ,[TozaiCD]
                        ,[ChokyosiCode]
                        ,[ChokyosiRyakusyo]
                        ,[Syotai]
                        ,[BreederCode]
                        ,[BreederName]
                        ,[SanchiName]
                        ,[BanusiCode]
                        ,[BanusiName]
                        ,[RuikeiHonsyoHeiti]
                        ,[RuikeiHonsyoSyogai]
                        ,[RuikeiFukaHeichi]
                        ,[RuikeiFukaSyogai]
                        ,[RuikeiSyutokuHeichi]
                        ,[RuikeiSyutokuSyogai]
                        ,[SogoChakukaisu1]
                        ,[SogoChakukaisu2]
                        ,[SogoChakukaisu3]
                        ,[SogoChakukaisu4]
                        ,[SogoChakukaisu5]
                        ,[SogoChakukaisu6]
                        ,[ChuoChakukaisu1]
                        ,[ChuoChakukaisu2]
                        ,[ChuoChakukaisu3]
                        ,[ChuoChakukaisu4]
                        ,[ChuoChakukaisu5]
                        ,[ChuoChakukaisu6]
                        ,[Ba1Chakukaisu1]
                        ,[Ba1Chakukaisu2]
                        ,[Ba1Chakukaisu3]
                        ,[Ba1Chakukaisu4]
                        ,[Ba1Chakukaisu5]
                        ,[Ba1Chakukaisu6]
                        ,[Ba2Chakukaisu1]
                        ,[Ba2Chakukaisu2]
                        ,[Ba2Chakukaisu3]
                        ,[Ba2Chakukaisu4]
                        ,[Ba2Chakukaisu5]
                        ,[Ba2Chakukaisu6]
                        ,[Ba3Chakukaisu1]
                        ,[Ba3Chakukaisu2]
                        ,[Ba3Chakukaisu3]
                        ,[Ba3Chakukaisu4]
                        ,[Ba3Chakukaisu5]
                        ,[Ba3Chakukaisu6]
                        ,[Ba4Chakukaisu1]
                        ,[Ba4Chakukaisu2]
                        ,[Ba4Chakukaisu3]
                        ,[Ba4Chakukaisu4]
                        ,[Ba4Chakukaisu5]
                        ,[Ba4Chakukaisu6]
                        ,[Ba5Chakukaisu1]
                        ,[Ba5Chakukaisu2]
                        ,[Ba5Chakukaisu3]
                        ,[Ba5Chakukaisu4]
                        ,[Ba5Chakukaisu5]
                        ,[Ba5Chakukaisu6]
                        ,[Ba6Chakukaisu1]
                        ,[Ba6Chakukaisu2]
                        ,[Ba6Chakukaisu3]
                        ,[Ba6Chakukaisu4]
                        ,[Ba6Chakukaisu5]
                        ,[Ba6Chakukaisu6]
                        ,[Ba7Chakukaisu1]
                        ,[Ba7Chakukaisu2]
                        ,[Ba7Chakukaisu3]
                        ,[Ba7Chakukaisu4]
                        ,[Ba7Chakukaisu5]
                        ,[Ba7Chakukaisu6]
                        ,[Jyotai1Chakukaisu1]
                        ,[Jyotai1Chakukaisu2]
                        ,[Jyotai1Chakukaisu3]
                        ,[Jyotai1Chakukaisu4]
                        ,[Jyotai1Chakukaisu5]
                        ,[Jyotai1Chakukaisu6]
                        ,[Jyotai2Chakukaisu1]
                        ,[Jyotai2Chakukaisu2]
                        ,[Jyotai2Chakukaisu3]
                        ,[Jyotai2Chakukaisu4]
                        ,[Jyotai2Chakukaisu5]
                        ,[Jyotai2Chakukaisu6]
                        ,[Jyotai3Chakukaisu1]
                        ,[Jyotai3Chakukaisu2]
                        ,[Jyotai3Chakukaisu3]
                        ,[Jyotai3Chakukaisu4]
                        ,[Jyotai3Chakukaisu5]
                        ,[Jyotai3Chakukaisu6]
                        ,[Jyotai4Chakukaisu1]
                        ,[Jyotai4Chakukaisu2]
                        ,[Jyotai4Chakukaisu3]
                        ,[Jyotai4Chakukaisu4]
                        ,[Jyotai4Chakukaisu5]
                        ,[Jyotai4Chakukaisu6]
                        ,[Jyotai5Chakukaisu1]
                        ,[Jyotai5Chakukaisu2]
                        ,[Jyotai5Chakukaisu3]
                        ,[Jyotai5Chakukaisu4]
                        ,[Jyotai5Chakukaisu5]
                        ,[Jyotai5Chakukaisu6]
                        ,[Jyotai6Chakukaisu1]
                        ,[Jyotai6Chakukaisu2]
                        ,[Jyotai6Chakukaisu3]
                        ,[Jyotai6Chakukaisu4]
                        ,[Jyotai6Chakukaisu5]
                        ,[Jyotai6Chakukaisu6]
                        ,[Jyotai7Chakukaisu1]
                        ,[Jyotai7Chakukaisu2]
                        ,[Jyotai7Chakukaisu3]
                        ,[Jyotai7Chakukaisu4]
                        ,[Jyotai7Chakukaisu5]
                        ,[Jyotai7Chakukaisu6]
                        ,[Jyotai8Chakukaisu1]
                        ,[Jyotai8Chakukaisu2]
                        ,[Jyotai8Chakukaisu3]
                        ,[Jyotai8Chakukaisu4]
                        ,[Jyotai8Chakukaisu5]
                        ,[Jyotai8Chakukaisu6]
                        ,[Jyotai9Chakukaisu1]
                        ,[Jyotai9Chakukaisu2]
                        ,[Jyotai9Chakukaisu3]
                        ,[Jyotai9Chakukaisu4]
                        ,[Jyotai9Chakukaisu5]
                        ,[Jyotai9Chakukaisu6]
                        ,[Jyotai10Chakukaisu1]
                        ,[Jyotai10Chakukaisu2]
                        ,[Jyotai10Chakukaisu3]
                        ,[Jyotai10Chakukaisu4]
                        ,[Jyotai10Chakukaisu5]
                        ,[Jyotai10Chakukaisu6]
                        ,[Jyotai11Chakukaisu1]
                        ,[Jyotai11Chakukaisu2]
                        ,[Jyotai11Chakukaisu3]
                        ,[Jyotai11Chakukaisu4]
                        ,[Jyotai11Chakukaisu5]
                        ,[Jyotai11Chakukaisu6]
                        ,[Jyotai12Chakukaisu1]
                        ,[Jyotai12Chakukaisu2]
                        ,[Jyotai12Chakukaisu3]
                        ,[Jyotai12Chakukaisu4]
                        ,[Jyotai12Chakukaisu5]
                        ,[Jyotai12Chakukaisu6]
                        ,[Kyori1Chakukaisu1]
                        ,[Kyori1Chakukaisu2]
                        ,[Kyori1Chakukaisu3]
                        ,[Kyori1Chakukaisu4]
                        ,[Kyori1Chakukaisu5]
                        ,[Kyori1Chakukaisu6]
                        ,[Kyori2Chakukaisu1]
                        ,[Kyori2Chakukaisu2]
                        ,[Kyori2Chakukaisu3]
                        ,[Kyori2Chakukaisu4]
                        ,[Kyori2Chakukaisu5]
                        ,[Kyori2Chakukaisu6]
                        ,[Kyori3Chakukaisu1]
                        ,[Kyori3Chakukaisu2]
                        ,[Kyori3Chakukaisu3]
                        ,[Kyori3Chakukaisu4]
                        ,[Kyori3Chakukaisu5]
                        ,[Kyori3Chakukaisu6]
                        ,[Kyori4Chakukaisu1]
                        ,[Kyori4Chakukaisu2]
                        ,[Kyori4Chakukaisu3]
                        ,[Kyori4Chakukaisu4]
                        ,[Kyori4Chakukaisu5]
                        ,[Kyori4Chakukaisu6]
                        ,[Kyori5Chakukaisu1]
                        ,[Kyori5Chakukaisu2]
                        ,[Kyori5Chakukaisu3]
                        ,[Kyori5Chakukaisu4]
                        ,[Kyori5Chakukaisu5]
                        ,[Kyori5Chakukaisu6]
                        ,[Kyori6Chakukaisu1]
                        ,[Kyori6Chakukaisu2]
                        ,[Kyori6Chakukaisu3]
                        ,[Kyori6Chakukaisu4]
                        ,[Kyori6Chakukaisu5]
                        ,[Kyori6Chakukaisu6]
                        ,[Kyakusitu1]
                        ,[Kyakusitu2]
                        ,[Kyakusitu3]
                        ,[Kyakusitu4]
                        ,[RaceCount])
                  VALUES
                        ('{input["RecordSpec"]}'
                        ,'{input["DataKubun"]}'
                        ,'{input["MakeDate"]}'
                        ,'{input["KettoNum"]}'
                        ,'{input["DelKubun"]}'
                        ,'{input["RegDate"]}'
                        ,'{input["DelDate"]}'
                        ,'{input["BirthDate"]}'
                        ,'{input["Bamei"]}'
                        ,'{input["BameiKana"]}'
                        ,'{input["BameiEng"]}'
                        ,'{input["ZaikyuFlag"]}'
                        ,'{input["Reserved"]}'
                        ,'{input["UmaKigoCD"]}'
                        ,'{input["SexCD"]}'
                        ,'{input["HinsyuCD"]}'
                        ,'{input["KeiroCD"]}'
                        ,'{input["Ketto3InfoHansyokuNum1"]}'
                        ,'{input["Ketto3InfoBamei1"]}'
                        ,'{input["Ketto3InfoHansyokuNum2"]}'
                        ,'{input["Ketto3InfoBamei2"]}'
                        ,'{input["Ketto3InfoHansyokuNum3"]}'
                        ,'{input["Ketto3InfoBamei3"]}'
                        ,'{input["Ketto3InfoHansyokuNum4"]}'
                        ,'{input["Ketto3InfoBamei4"]}'
                        ,'{input["Ketto3InfoHansyokuNum5"]}'
                        ,'{input["Ketto3InfoBamei5"]}'
                        ,'{input["Ketto3InfoHansyokuNum6"]}'
                        ,'{input["Ketto3InfoBamei6"]}'
                        ,'{input["Ketto3InfoHansyokuNum7"]}'
                        ,'{input["Ketto3InfoBamei7"]}'
                        ,'{input["Ketto3InfoHansyokuNum8"]}'
                        ,'{input["Ketto3InfoBamei8"]}'
                        ,'{input["Ketto3InfoHansyokuNum9"]}'
                        ,'{input["Ketto3InfoBamei9"]}'
                        ,'{input["Ketto3InfoHansyokuNum10"]}'
                        ,'{input["Ketto3InfoBamei10"]}'
                        ,'{input["Ketto3InfoHansyokuNum11"]}'
                        ,'{input["Ketto3InfoBamei11"]}'
                        ,'{input["Ketto3InfoHansyokuNum12"]}'
                        ,'{input["Ketto3InfoBamei12"]}'
                        ,'{input["Ketto3InfoHansyokuNum13"]}'
                        ,'{input["Ketto3InfoBamei13"]}'
                        ,'{input["Ketto3InfoHansyokuNum14"]}'
                        ,'{input["Ketto3InfoBamei14"]}'
                        ,'{input["TozaiCD"]}'
                        ,'{input["ChokyosiCode"]}'
                        ,'{input["ChokyosiRyakusyo"]}'
                        ,'{input["Syotai"]}'
                        ,'{input["BreederCode"]}'
                        ,'{input["BreederName,"]}'
                        ,'{input["SanchiName"]}'
                        ,'{input["BanusiCode"]}'
                        ,'{input["BanusiName"]}'
                        ,'{input["RuikeiHonsyoHeiti"]}'
                        ,'{input["RuikeiHonsyoSyogai"]}'
                        ,'{input["RuikeiFukaHeichi"]}'
                        ,'{input["RuikeiFukaSyogai"]}'
                        ,'{input["RuikeiSyutokuHeichi"]}'
                        ,'{input["RuikeiSyutokuSyogai"]}'
                        ,'{input["SogoChakukaisu1"]}'
                        ,'{input["SogoChakukaisu2"]}'
                        ,'{input["SogoChakukaisu3"]}'
                        ,'{input["SogoChakukaisu4"]}'
                        ,'{input["SogoChakukaisu5"]}'
                        ,'{input["SogoChakukaisu6"]}'
                        ,'{input["ChuoChakukaisu1"]}'
                        ,'{input["ChuoChakukaisu2"]}'
                        ,'{input["ChuoChakukaisu3"]}'
                        ,'{input["ChuoChakukaisu4"]}'
                        ,'{input["ChuoChakukaisu5"]}'
                        ,'{input["ChuoChakukaisu6"]}'
                        ,'{input["Ba1Chakukaisu1"]}'
                        ,'{input["Ba1Chakukaisu2"]}'
                        ,'{input["Ba1Chakukaisu3"]}'
                        ,'{input["Ba1Chakukaisu4"]}'
                        ,'{input["Ba1Chakukaisu5"]}'
                        ,'{input["Ba1Chakukaisu6"]}'
                        ,'{input["Ba2Chakukaisu1"]}'
                        ,'{input["Ba2Chakukaisu2"]}'
                        ,'{input["Ba2Chakukaisu3"]}'
                        ,'{input["Ba2Chakukaisu4"]}'
                        ,'{input["Ba2Chakukaisu5"]}'
                        ,'{input["Ba2Chakukaisu6"]}'
                        ,'{input["Ba3Chakukaisu1"]}'
                        ,'{input["Ba3Chakukaisu2"]}'
                        ,'{input["Ba3Chakukaisu3"]}'
                        ,'{input["Ba3Chakukaisu4"]}'
                        ,'{input["Ba3Chakukaisu5"]}'
                        ,'{input["Ba3Chakukaisu6"]}'
                        ,'{input["Ba4Chakukaisu1"]}'
                        ,'{input["Ba4Chakukaisu2"]}'
                        ,'{input["Ba4Chakukaisu3"]}'
                        ,'{input["Ba4Chakukaisu4"]}'
                        ,'{input["Ba4Chakukaisu5"]}'
                        ,'{input["Ba4Chakukaisu6"]}'
                        ,'{input["Ba5Chakukaisu1"]}'
                        ,'{input["Ba5Chakukaisu2"]}'
                        ,'{input["Ba5Chakukaisu3"]}'
                        ,'{input["Ba5Chakukaisu4"]}'
                        ,'{input["Ba5Chakukaisu5"]}'
                        ,'{input["Ba5Chakukaisu6"]}'
                        ,'{input["Ba6Chakukaisu1"]}'
                        ,'{input["Ba6Chakukaisu2"]}'
                        ,'{input["Ba6Chakukaisu3"]}'
                        ,'{input["Ba6Chakukaisu4"]}'
                        ,'{input["Ba6Chakukaisu5"]}'
                        ,'{input["Ba6Chakukaisu6"]}'
                        ,'{input["Ba7Chakukaisu1"]}'
                        ,'{input["Ba7Chakukaisu2"]}'
                        ,'{input["Ba7Chakukaisu3"]}'
                        ,'{input["Ba7Chakukaisu4"]}'
                        ,'{input["Ba7Chakukaisu5"]}'
                        ,'{input["Ba7Chakukaisu6"]}'
                        ,'{input["Jyotai1Chakukaisu1"]}'
                        ,'{input["Jyotai1Chakukaisu2"]}'
                        ,'{input["Jyotai1Chakukaisu3"]}'
                        ,'{input["Jyotai1Chakukaisu4"]}'
                        ,'{input["Jyotai1Chakukaisu5"]}'
                        ,'{input["Jyotai1Chakukaisu6"]}'
                        ,'{input["Jyotai2Chakukaisu1"]}'
                        ,'{input["Jyotai2Chakukaisu2"]}'
                        ,'{input["Jyotai2Chakukaisu3"]}'
                        ,'{input["Jyotai2Chakukaisu4"]}'
                        ,'{input["Jyotai2Chakukaisu5"]}'
                        ,'{input["Jyotai2Chakukaisu6"]}'
                        ,'{input["Jyotai3Chakukaisu1"]}'
                        ,'{input["Jyotai3Chakukaisu2"]}'
                        ,'{input["Jyotai3Chakukaisu3"]}'
                        ,'{input["Jyotai3Chakukaisu4"]}'
                        ,'{input["Jyotai3Chakukaisu5"]}'
                        ,'{input["Jyotai3Chakukaisu6"]}'
                        ,'{input["Jyotai4Chakukaisu1"]}'
                        ,'{input["Jyotai4Chakukaisu2"]}'
                        ,'{input["Jyotai4Chakukaisu3"]}'
                        ,'{input["Jyotai4Chakukaisu4"]}'
                        ,'{input["Jyotai4Chakukaisu5"]}'
                        ,'{input["Jyotai4Chakukaisu6"]}'
                        ,'{input["Jyotai5Chakukaisu1"]}'
                        ,'{input["Jyotai5Chakukaisu2"]}'
                        ,'{input["Jyotai5Chakukaisu3"]}'
                        ,'{input["Jyotai5Chakukaisu4"]}'
                        ,'{input["Jyotai5Chakukaisu5"]}'
                        ,'{input["Jyotai5Chakukaisu6"]}'
                        ,'{input["Jyotai6Chakukaisu1"]}'
                        ,'{input["Jyotai6Chakukaisu2"]}'
                        ,'{input["Jyotai6Chakukaisu3"]}'
                        ,'{input["Jyotai6Chakukaisu4"]}'
                        ,'{input["Jyotai6Chakukaisu5"]}'
                        ,'{input["Jyotai6Chakukaisu6"]}'
                        ,'{input["Jyotai7Chakukaisu1"]}'
                        ,'{input["Jyotai7Chakukaisu2"]}'
                        ,'{input["Jyotai7Chakukaisu3"]}'
                        ,'{input["Jyotai7Chakukaisu4"]}'
                        ,'{input["Jyotai7Chakukaisu5"]}'
                        ,'{input["Jyotai7Chakukaisu6"]}'
                        ,'{input["Jyotai8Chakukaisu1"]}'
                        ,'{input["Jyotai8Chakukaisu2"]}'
                        ,'{input["Jyotai8Chakukaisu3"]}'
                        ,'{input["Jyotai8Chakukaisu4"]}'
                        ,'{input["Jyotai8Chakukaisu5"]}'
                        ,'{input["Jyotai8Chakukaisu6"]}'
                        ,'{input["Jyotai9Chakukaisu1"]}'
                        ,'{input["Jyotai9Chakukaisu2"]}'
                        ,'{input["Jyotai9Chakukaisu3"]}'
                        ,'{input["Jyotai9Chakukaisu4"]}'
                        ,'{input["Jyotai9Chakukaisu5"]}'
                        ,'{input["Jyotai9Chakukaisu6"]}'
                        ,'{input["Jyotai10Chakukaisu1"]}'
                        ,'{input["Jyotai10Chakukaisu2"]}'
                        ,'{input["Jyotai10Chakukaisu3"]}'
                        ,'{input["Jyotai10Chakukaisu4"]}'
                        ,'{input["Jyotai10Chakukaisu5"]}'
                        ,'{input["Jyotai10Chakukaisu6"]}'
                        ,'{input["Jyotai11Chakukaisu1"]}'
                        ,'{input["Jyotai11Chakukaisu2"]}'
                        ,'{input["Jyotai11Chakukaisu3"]}'
                        ,'{input["Jyotai11Chakukaisu4"]}'
                        ,'{input["Jyotai11Chakukaisu5"]}'
                        ,'{input["Jyotai11Chakukaisu6"]}'
                        ,'{input["Jyotai12Chakukaisu1"]}'
                        ,'{input["Jyotai12Chakukaisu2"]}'
                        ,'{input["Jyotai12Chakukaisu3"]}'
                        ,'{input["Jyotai12Chakukaisu4"]}'
                        ,'{input["Jyotai12Chakukaisu5"]}'
                        ,'{input["Jyotai12Chakukaisu6"]}'
                        ,'{input["Kyori1Chakukaisu1"]}'
                        ,'{input["Kyori1Chakukaisu2"]}'
                        ,'{input["Kyori1Chakukaisu3"]}'
                        ,'{input["Kyori1Chakukaisu4"]}'
                        ,'{input["Kyori1Chakukaisu5"]}'
                        ,'{input["Kyori1Chakukaisu6"]}'
                        ,'{input["Kyori2Chakukaisu1"]}'
                        ,'{input["Kyori2Chakukaisu2"]}'
                        ,'{input["Kyori2Chakukaisu3"]}'
                        ,'{input["Kyori2Chakukaisu4"]}'
                        ,'{input["Kyori2Chakukaisu5"]}'
                        ,'{input["Kyori2Chakukaisu6"]}'
                        ,'{input["Kyori3Chakukaisu1"]}'
                        ,'{input["Kyori3Chakukaisu2"]}'
                        ,'{input["Kyori3Chakukaisu3"]}'
                        ,'{input["Kyori3Chakukaisu4"]}'
                        ,'{input["Kyori3Chakukaisu5"]}'
                        ,'{input["Kyori3Chakukaisu6"]}'
                        ,'{input["Kyori4Chakukaisu1"]}'
                        ,'{input["Kyori4Chakukaisu2"]}'
                        ,'{input["Kyori4Chakukaisu3"]}'
                        ,'{input["Kyori4Chakukaisu4"]}'
                        ,'{input["Kyori4Chakukaisu5"]}'
                        ,'{input["Kyori4Chakukaisu6"]}'
                        ,'{input["Kyori5Chakukaisu1"]}'
                        ,'{input["Kyori5Chakukaisu2"]}'
                        ,'{input["Kyori5Chakukaisu3"]}'
                        ,'{input["Kyori5Chakukaisu4"]}'
                        ,'{input["Kyori5Chakukaisu5"]}'
                        ,'{input["Kyori5Chakukaisu6"]}'
                        ,'{input["Kyori6Chakukaisu1"]}'
                        ,'{input["Kyori6Chakukaisu2"]}'
                        ,'{input["Kyori6Chakukaisu3"]}'
                        ,'{input["Kyori6Chakukaisu4"]}'
                        ,'{input["Kyori6Chakukaisu5"]}'
                        ,'{input["Kyori6Chakukaisu6"]}'
                        ,'{input["Kyakusitu1"]}'
                        ,'{input["Kyakusitu2"]}'
                        ,'{input["Kyakusitu3"]}'
                        ,'{input["Kyakusitu4"]}'
                        ,'{input["RaceCount"]}')

                              """
			print(f"Insert {input['Year']} {input['MonthDay']} {input['JyoCD']} {input['RaceNum']}")
  
			cmd = cmd.replace( '\n' , ' ' )
			cmd = cmd.replace( '\t' , '' )
			accessor.cur_close()					 
			accessor.execute(cmd)
			accessor.commit() 
			accessor.cur_close()
			ret =True
		else:
			# template = """
			# 		update 
			# 			{0} 
			# 		set
			# 			ms_name ='{2}',
			# 			ms_race_count={3},
			# 			ms_win_count={4},
			# 			ms_mul_count={5},
			# 			upd=1
			# 		where 
			# 			ms_id ='{1}'
			# 		"""
			# cmd = template.format(
			# 	const.TBL_KJDB_MASTER_SIRE, 
			# 	id,
			# 	name,
			# 	racecount, 
			# 	win_count, 
			# 	mul_count
			# 	)
			i=0

		
		# cmd = cmd.replace( '\n' , ' ' )
		# cmd = cmd.replace( '\t' , '' )					 
		# accessor.execute(cmd)
		# accessor.commit()
		# accessor.cur_close()
		
	except Exception as e: 
		i=0
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	return ret
