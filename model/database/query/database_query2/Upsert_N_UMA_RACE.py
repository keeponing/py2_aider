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
                        and
                              KettoNum='{5}'
			"""
		cmd = template.format(
			const.TBL_KJVAN_N_UMA_RACE,
			input['Year'],
 			input['MonthDay'],			
			input['JyoCD'],
			input['RaceNum'],
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
                  INSERT INTO [dbo].[{const.TBL_KJVAN_N_UMA_RACE}]
                        ([RecordSpec]
                        ,[DataKubun]
                        ,[MakeDate]
                        ,[Year]
                        ,[MonthDay]
                        ,[JyoCD]
                        ,[Kaiji]
                        ,[Nichiji]
                        ,[RaceNum]
                        ,[Wakuban]
                        ,[Umaban]
                        ,[KettoNum]
                        ,[Bamei]
                        ,[UmaKigoCD]
                        ,[SexCD]
                        ,[HinsyuCD]
                        ,[KeiroCD]
                        ,[Barei]
                        ,[TozaiCD]
                        ,[ChokyosiCode]
                        ,[ChokyosiRyakusyo]
                        ,[BanusiCode]
                        ,[BanusiName]
                        ,[Fukusyoku]
                        ,[Reserved1]
                        ,[Futan]
                        ,[FutanBefore]
                        ,[Blinker]
                        ,[Reserved2]
                        ,[KisyuCode]
                        ,[KisyuCodeBefore]
                        ,[KisyuRyakusyo]
                        ,[KisyuRyakusyoBefore]
                        ,[MinaraiCD]
                        ,[MinaraiCDBefore]
                        ,[BaTaijyu]
                        ,[ZogenFugo]
                        ,[ZogenSa]
                        ,[IJyoCD]
                        ,[NyusenJyuni]
                        ,[KakuteiJyuni]
                        ,[DochakuKubun]
                        ,[DochakuTosu]
                        ,[Time]
                        ,[ChakusaCD]
                        ,[ChakusaCDP]
                        ,[ChakusaCDPP]
                        ,[Jyuni1c]
                        ,[Jyuni2c]
                        ,[Jyuni3c]
                        ,[Jyuni4c]
                        ,[Odds]
                        ,[Ninki]
                        ,[Honsyokin]
                        ,[Fukasyokin]
                        ,[Reserved3]
                        ,[Reserved4]
                        ,[HaronTimeL4]
                        ,[HaronTimeL3]
                        ,[KettoNum1]
                        ,[Bamei1]
                        ,[KettoNum2]
                        ,[Bamei2]
                        ,[KettoNum3]
                        ,[Bamei3]
                        ,[TimeDiff]
                        ,[RecordUpKubun]
                        ,[DMKubun]
                        ,[DMTime]
                        ,[DMGosaP]
                        ,[DMGosaM]
                        ,[DMJyuni]
                        ,[KyakusituKubun])
                  VALUES
                        ('{input["RecordSpec"]}'
                        ,'{input["DataKubun"]}'
                        ,'{input["MakeDate"]}'
                        ,'{input["Year"]}'
                        ,'{input["MonthDay"]}'
                        ,'{input["JyoCD"]}'
                        ,'{input["Kaiji"]}'
                        ,'{input["Nichiji"]}'
                        ,'{input["RaceNum"]}'
                        ,'{input["Wakuban"]}'
                        ,'{input["Umaban"]}'
                        ,'{input["KettoNum"]}'
                        ,'{input["Bamei"]}'
                        ,'{input["UmaKigoCD"]}'
                        ,'{input["SexCD"]}'
                        ,'{input["HinsyuCD"]}'
                        ,'{input["KeiroCD"]}'
                        ,'{input["Barei"]}'
                        ,'{input["TozaiCD"]}'
                        ,'{input["ChokyosiCode"]}'
                        ,'{input["ChokyosiRyakusyo"]}'
                        ,'{input["BanusiCode"]}'
                        ,'{input["BanusiName"]}'
                        ,'{input["Fukusyoku"]}'
                        ,'{input["Reserved1"]}'
                        ,'{input["Futan"]}'
                        ,'{input["FutanBefore"]}'
                        ,'{input["Blinker"]}'
                        ,'{input["Reserved2"]}'
                        ,'{input["KisyuCode"]}'
                        ,'{input["KisyuCodeBefore"]}'
                        ,'{input["KisyuRyakusyo"]}'
                        ,'{input["KisyuRyakusyoBefore"]}'
                        ,'{input["MinaraiCD"]}'
                        ,'{input["MinaraiCDBefore"]}'
                        ,'{input["BaTaijyu"]}'
                        ,'{input["ZogenFugo"]}'
                        ,'{input["ZogenSa"]}'
                        ,'{input["IJyoCD"]}'
                        ,'{input["NyusenJyuni"]}'
                        ,'{input["KakuteiJyuni"]}'
                        ,'{input["DochakuKubun"]}'
                        ,'{input["DochakuTosu"]}'
                        ,'{input["Time"]}'
                        ,'{input["ChakusaCD"]}'
                        ,'{input["ChakusaCDP"]}'
                        ,'{input["ChakusaCDPP"]}'
                        ,'{input["Jyuni1c"]}'
                        ,'{input["Jyuni2c"]}'
                        ,'{input["Jyuni3c"]}'
                        ,'{input["Jyuni4c"]}'
                        ,'{input["Odds"]}'
                        ,'{input["Ninki"]}'
                        ,'{input["Honsyokin"]}'
                        ,'{input["Fukasyokin"]}'
                        ,'{input["Reserved3"]}'
                        ,'{input["Reserved4"]}'
                        ,'{input["HaronTimeL4"]}'
                        ,'{input["HaronTimeL3"]}'
                        ,'{input["KettoNum1"]}'
                        ,'{input["Bamei1"]}'
                        ,'{input["KettoNum2"]}'
                        ,'{input["Bamei2"]}'
                        ,'{input["KettoNum3"]}'
                        ,'{input["Bamei3"]}'
                        ,'{input["TimeDiff"]}'
                        ,'{input["RecordUpKubun"]}'
                        ,'{input["DMKubun"]}'
                        ,'{input["DMTime"]}'
                        ,'{input["DMGosaP"]}'
                        ,'{input["DMGosaM"]}'
                        ,'{input["DMJyuni"]}'
                        ,'{input["KyakusituKubun"]}')
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
