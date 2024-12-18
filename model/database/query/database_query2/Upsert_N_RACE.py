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
					Year='{1}' 
				and
					MonthDay='{2}' 
				and
					JyoCD='{3}' 	
				and
					RaceNum='{4}' 
			"""
		cmd = template.format(
			const.TBL_KJVAN_N_RACE,
			input['Year'],
 			input['MonthDay'],			
			input['JyoCD'],
			input['RaceNum']		
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
                  INSERT INTO [{const.TBL_KJVAN_N_RACE}]
                        ([RecordSpec]
                        ,[DataKubun]
                        ,[MakeDate]
                        ,[Year]
                        ,[MonthDay]
                        ,[JyoCD]
                        ,[Kaiji]
                        ,[Nichiji]
                        ,[RaceNum]
                        ,[YoubiCD]
                        ,[TokuNum]
                        ,[Hondai]
                        ,[Fukudai]
                        ,[Kakko]
                        ,[HondaiEng]
                        ,[FukudaiEng]
                        ,[KakkoEng]
                        ,[Ryakusyo10]
                        ,[Ryakusyo6]
                        ,[Ryakusyo3]
                        ,[Kubun]
                        ,[Nkai]
                        ,[GradeCD]
                        ,[GradeCDBefore]
                        ,[SyubetuCD]
                        ,[KigoCD]
                        ,[JyuryoCD]
                        ,[JyokenCD1]
                        ,[JyokenCD2]
                        ,[JyokenCD3]
                        ,[JyokenCD4]
                        ,[JyokenCD5]
                        ,[JyokenName]
                        ,[Kyori]
                        ,[KyoriBefore]
                        ,[TrackCD]
                        ,[TrackCDBefore]
                        ,[CourseKubunCD]
                        ,[CourseKubunCDBefore]
                        ,[Honsyokin1]
                        ,[Honsyokin2]
                        ,[Honsyokin3]
                        ,[Honsyokin4]
                        ,[Honsyokin5]
                        ,[Honsyokin6]
                        ,[Honsyokin7]
                        ,[HonsyokinBefore1]
                        ,[HonsyokinBefore2]
                        ,[HonsyokinBefore3]
                        ,[HonsyokinBefore4]
                        ,[HonsyokinBefore5]
                        ,[Fukasyokin1]
                        ,[Fukasyokin2]
                        ,[Fukasyokin3]
                        ,[Fukasyokin4]
                        ,[Fukasyokin5]
                        ,[FukasyokinBefore1]
                        ,[FukasyokinBefore2]
                        ,[FukasyokinBefore3]
                        ,[HassoTime]
                        ,[HassoTimeBefore]
                        ,[TorokuTosu]
                        ,[SyussoTosu]
                        ,[NyusenTosu]
                        ,[TenkoCD]
                        ,[SibaBabaCD]
                        ,[DirtBabaCD]
                        ,[LapTime1]
                        ,[LapTime2]
                        ,[LapTime3]
                        ,[LapTime4]
                        ,[LapTime5]
                        ,[LapTime6]
                        ,[LapTime7]
                        ,[LapTime8]
                        ,[LapTime9]
                        ,[LapTime10]
                        ,[LapTime11]
                        ,[LapTime12]
                        ,[LapTime13]
                        ,[LapTime14]
                        ,[LapTime15]
                        ,[LapTime16]
                        ,[LapTime17]
                        ,[LapTime18]
                        ,[LapTime19]
                        ,[LapTime20]
                        ,[LapTime21]
                        ,[LapTime22]
                        ,[LapTime23]
                        ,[LapTime24]
                        ,[LapTime25]
                        ,[SyogaiMileTime]
                        ,[HaronTimeS3]
                        ,[HaronTimeS4]
                        ,[HaronTimeL3]
                        ,[HaronTimeL4]
                        ,[Corner1]
                        ,[Syukaisu1]
                        ,[Jyuni1]
                        ,[Corner2]
                        ,[Syukaisu2]
                        ,[Jyuni2]
                        ,[Corner3]
                        ,[Syukaisu3]
                        ,[Jyuni3]
                        ,[Corner4]
                        ,[Syukaisu4]
                        ,[Jyuni4]
                        ,[RecordUpKubun])
                  VALUES
                        (
                         '{input["RecordSpec"]}'
                        ,'{input["DataKubun"]}'
                        ,'{input["MakeDate"]}'
                        ,'{input["Year"]}'
                        ,'{input["MonthDay"]}'
                        ,'{input["JyoCD"]}'
                        ,'{input["Kaiji"]}'
                        ,'{input["Nichiji"]}'
                        ,'{input["RaceNum"]}'
                        ,'{input["YoubiCD"]}'
                        ,'{input["TokuNum"]}'
                        ,'{input["Hondai"]}'
                        ,'{input["Fukudai"]}'
                        ,'{input["Kakko"]}'
                        ,'{input["HondaiEng"]}'
                        ,'{input["FukudaiEng"]}'
                        ,'{input["KakkoEng"]}'
                        ,'{input["Ryakusyo10"]}'
                        ,'{input["Ryakusyo6"]}'
                        ,'{input["Ryakusyo3"]}'
                        ,'{input["Kubun"]}'
                        ,'{input["Nkai"]}'
                        ,'{input["GradeCD"]}'
                        ,'{input["GradeCDBefore"]}'
                        ,'{input["SyubetuCD"]}'
                        ,'{input["KigoCD"]}'
                        ,'{input["JyuryoCD"]}'
                        ,'{input["JyokenCD1"]}'
                        ,'{input["JyokenCD2"]}'
                        ,'{input["JyokenCD3"]}'
                        ,'{input["JyokenCD4"]}'
                        ,'{input["JyokenCD5"]}'
                        ,'{input["JyokenName"]}'
                        ,'{input["Kyori"]}'
                        ,'{input["KyoriBefore"]}'
                        ,'{input["TrackCD"]}'
                        ,'{input["TrackCDBefore"]}'
                        ,'{input["CourseKubunCD"]}'
                        ,'{input["CourseKubunCDBefore"]}'
                        ,'{input["Honsyokin1"]}'
                        ,'{input["Honsyokin2"]}'
                        ,'{input["Honsyokin3"]}'
                        ,'{input["Honsyokin4"]}'
                        ,'{input["Honsyokin5"]}'
                        ,'{input["Honsyokin6"]}'
                        ,'{input["Honsyokin7"]}'
                        ,'{input["HonsyokinBefore1"]}'
                        ,'{input["HonsyokinBefore2"]}'
                        ,'{input["HonsyokinBefore3"]}'
                        ,'{input["HonsyokinBefore4"]}'
                        ,'{input["HonsyokinBefore5"]}'
                        ,'{input["Fukasyokin1"]}'
                        ,'{input["Fukasyokin2"]}'
                        ,'{input["Fukasyokin3"]}'
                        ,'{input["Fukasyokin4"]}'
                        ,'{input["Fukasyokin5"]}'
                        ,'{input["FukasyokinBefore1"]}'
                        ,'{input["FukasyokinBefore2"]}'
                        ,'{input["FukasyokinBefore3"]}'
                        ,'{input["HassoTime"]}'
                        ,'{input["HassoTimeBefore"]}'
                        ,'{input["TorokuTosu"]}'
                        ,'{input["SyussoTosu"]}'
                        ,'{input["NyusenTosu"]}'
                        ,'{input["TenkoCD"]}'
                        ,'{input["SibaBabaCD"]}'
                        ,'{input["DirtBabaCD"]}'
                        ,'{input["LapTime1"]}'
                        ,'{input["LapTime2"]}'
                        ,'{input["LapTime3"]}'
                        ,'{input["LapTime4"]}'
                        ,'{input["LapTime5"]}'
                        ,'{input["LapTime6"]}'
                        ,'{input["LapTime7"]}'
                        ,'{input["LapTime8"]}'
                        ,'{input["LapTime9"]}'
                        ,'{input["LapTime10"]}'
                        ,'{input["LapTime11"]}'
                        ,'{input["LapTime12"]}'
                        ,'{input["LapTime13"]}'
                        ,'{input["LapTime14"]}'
                        ,'{input["LapTime15"]}'
                        ,'{input["LapTime16"]}'
                        ,'{input["LapTime17"]}'
                        ,'{input["LapTime18"]}'
                        ,'{input["LapTime19"]}'
                        ,'{input["LapTime20"]}'
                        ,'{input["LapTime21"]}'
                        ,'{input["LapTime22"]}'
                        ,'{input["LapTime23"]}'
                        ,'{input["LapTime24"]}'
                        ,'{input["LapTime25"]}'
                        ,'{input["SyogaiMileTime"]}'
                        ,'{input["HaronTimeS3"]}'
                        ,'{input["HaronTimeS4"]}'
                        ,'{input["HaronTimeL3"]}'
                        ,'{input["HaronTimeL4"]}'
                        ,'{input["Corner1"]}'
                        ,'{input["Syukaisu1"]}'
                        ,'{input["Jyuni1"]}'
                        ,'{input["Corner2"]}'
                        ,'{input["Syukaisu2"]}'
                        ,'{input["Jyuni2"]}'
                        ,'{input["Corner3"]}'
                        ,'{input["Syukaisu3"]}'
                        ,'{input["Jyuni3"]}'
                        ,'{input["Corner4"]}'
                        ,'{input["Syukaisu4"]}'
                        ,'{input["Jyuni4"]}'
                        ,'{input["RecordUpKubun"]}')	
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
