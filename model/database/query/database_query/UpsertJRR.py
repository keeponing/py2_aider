#Jra S  馬成績ヘッダ
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, rr, is_direct =False):

	try:
		#2019110203
		rr_r_id =rr['rr_r_id']
		y = rr_r_id[:4]
		if(False == is_direct):
			mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		else:
			mdb = const.TBL_KJDB_RACE_RESULT
		template = """
			select 
				count(*) 
			from {0}  
				where 
						rr_r_id ='{1}' 
					and 
						rr_r_race ='{2}'
					and 
						rr_r_horse_id='{3}'
		"""
		cmd = template.format(mdb, 
							rr['rr_r_id'],
							rr['rr_r_race'],
							rr['rr_r_horse_id'],
							)
		accessor.execute(cmd)
		count=0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			template = """
					insert into {0} 
					(  
						rr_r_id,
						rr_r_race,
						rr_r_horse_id,
						rr_r_horse_no,
						rr_r_horse_name,
						rr_r_rank,
						rr_r_waku,
						rr_r_blinker,
						rr_r_age,
						rr_r_gender,
						rr_r_burden,
						rr_r_jockey,
						rr_r_j_id,
						rr_r_j_mark,
						rr_r_time,
						rr_r_diff1,
						rr_r_diff2,
						rr_r_diff3,
						rr_r_f3_time,
						rr_r_weight,
						rr_r_gal_sign,
						rr_r_gal_val,
						rr_r_trainer,
						rr_r_t_id,
						rr_r_vote,
						rr_r_corner1,
						rr_r_corner2,
						rr_r_corner3,
						rr_r_corner4,
						rr_r_horse_sign,
						rr_r_varieties,
						rr_r_belongs,
						rr_r_o_id,
						rr_r_odds,
						rr_r_time_diff,
						rr_m_jra_bilongs,
						rr_m_blood01,
						rr_m_blood02,
						rr_m_blood03,
						rr_m_blood04,
						rr_m_blood05,
						rr_m_blood06,
						rr_m_blood07,
						rr_m_blood08,
						rr_m_blood09,
						rr_m_blood10,
						rr_m_blood11,
						rr_m_blood12,
						rr_m_blood13,
						rr_m_blood14,
						rr_m_feet1,
						rr_m_feet2,
						rr_m_feet3,
						rr_m_feet4,
						rr_h_prev_id1,
						rr_h_prev_id2,
						rr_h_prev_id3,
						rr_h_prev_id4,
						rr_a_deviation,
						rr_a_deviation3f,
						rr_a_race_count,
						rr_r_err,
						rr_h_sc_prev_id1,
						rr_h_sc_prev_id2,
						rr_h_sc_prev_id3,
						rr_h_sc_prev_id4,
						upd
						) values (
						'{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}',
						'{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}',
						'{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}',
						'{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}','{40}',
						'{41}','{42}','{43}','{44}','{45}','{46}','{47}','{48}','{49}','{50}',
						'{51}','{52}','{53}','{54}','{55}','{56}','{57}','{58}', {59} , {60} ,
						 {61} ,'{62}','{63}','{64}','{65}','{66}', {67}
						)
						"""
		else:
			template = """
					update {0} 
					set 
						rr_r_horse_no='{4}',
						rr_r_horse_name='{5}',
						rr_r_rank='{6}',
						rr_r_waku='{7}',
						rr_r_blinker='{8}',
						rr_r_age='{9}',
						rr_r_gender='{10}',
						rr_r_burden='{11}',
						rr_r_jockey='{12}',
						rr_r_j_id='{13}',
						rr_r_j_mark='{14}',
						rr_r_time='{15}',
						rr_r_diff1='{16}',
						rr_r_diff2='{17}',
						rr_r_diff3='{18}',
						rr_r_f3_time='{19}',
						rr_r_weight='{20}',
						rr_r_gal_sign='{21}',
						rr_r_gal_val='{22}',
						rr_r_trainer='{23}',
						rr_r_t_id='{24}',
						rr_r_vote ='{25}',
						rr_r_corner1 ='{26}',
						rr_r_corner2 ='{27}',
						rr_r_corner3 ='{28}',
						rr_r_corner4 ='{29}',
						rr_r_horse_sign ='{30}',
						rr_r_varieties='{31}',
						rr_r_belongs='{32}',
						rr_r_o_id='{33}',
						rr_r_odds='{34}',
						rr_r_time_diff='{35}',
						rr_m_jra_bilongs='{36}',
						rr_m_blood01='{37}',
						rr_m_blood02='{38}',
						rr_m_blood03='{39}',
						rr_m_blood04='{40}',
						rr_m_blood05='{41}',
						rr_m_blood06='{42}',
						rr_m_blood07='{43}',
						rr_m_blood08='{44}',
						rr_m_blood09='{45}',
						rr_m_blood10='{46}',
						rr_m_blood11='{47}',
						rr_m_blood12='{48}',
						rr_m_blood13='{49}',
						rr_m_blood14='{50}',
						rr_m_feet1='{51}',
						rr_m_feet2='{52}',
						rr_m_feet3='{53}',
						rr_m_feet4='{54}',
						rr_h_prev_id1='{55}',
						rr_h_prev_id2='{56}',
						rr_h_prev_id3='{57}',
						rr_h_prev_id4='{58}',
						rr_a_deviation={59},
						rr_a_deviation3f={60},
						rr_a_race_count ={61},
						rr_r_err='{62}',
						rr_h_sc_prev_id1='{63}',
						rr_h_sc_prev_id2='{64}',
						rr_h_sc_prev_id3='{65}',
						rr_h_sc_prev_id4='{66}',
						upd={67}

					where 
						rr_r_id='{1}' 
						and 
						rr_r_race='{2}' 
						and 
						rr_r_horse_id='{3}' 
						"""	
		accessor.cur_close()
		cmd = template.format(
			mdb,#0
			rr['rr_r_id'], #1
			rr['rr_r_race'],#2
			rr['rr_r_horse_id'],#3
			rr['rr_r_horse_no'],#4
			rr['rr_r_horse_name'],#5
			rr['rr_r_rank'],#6
			rr['rr_r_waku'],#7
			rr['rr_r_blinker'],#8
			rr['rr_r_age'],#9
			rr['rr_r_gender'],#10
			rr['rr_r_burden'],#11
			rr['rr_r_jockey'],#12
			rr['rr_r_j_id'],#13
			rr['rr_r_j_mark'],#14
			rr['rr_r_time'],#15
			rr['rr_r_diff1'],#16
			rr['rr_r_diff2'],#17
			rr['rr_r_diff3'],#18
			rr['rr_r_f3_time'],#19
			rr['rr_r_weight'],#20
			rr['rr_r_gal_sign'],#21
			rr['rr_r_gal_val'],#22
			rr['rr_r_trainer'],#23
			rr['rr_r_t_id'],#24
			rr['rr_r_vote'],#25
			rr['rr_r_corner1'],#26
			rr['rr_r_corner2'],#27
			rr['rr_r_corner3'],#28
			rr['rr_r_corner4'],#29
			rr['rr_r_horse_sign'],#30
			rr['rr_r_varieties'],#31
			rr['rr_r_belongs'],#32
			rr['rr_r_o_id'],#33
			rr['rr_r_odds'],#34
			rr['rr_r_time_diff'],#35
			rr['rr_m_jra_bilongs'],#36
			rr['rr_m_blood01'],#37
			rr['rr_m_blood02'],#38
			rr['rr_m_blood03'],#39
			rr['rr_m_blood04'],#40
			rr['rr_m_blood05'],#41
			rr['rr_m_blood06'],#42
			rr['rr_m_blood07'],#43
			rr['rr_m_blood08'],#44
			rr['rr_m_blood09'],#45
			rr['rr_m_blood10'],#46
			rr['rr_m_blood11'],#47
			rr['rr_m_blood12'],#48
			rr['rr_m_blood13'],#49
			rr['rr_m_blood14'],#50
			rr['rr_m_feet1'],#51
			rr['rr_m_feet2'],#52
			rr['rr_m_feet3'],#53
			rr['rr_m_feet4'],#54
			rr['rr_h_prev_id1'],#55
			rr['rr_h_prev_id2'],#56
			rr['rr_h_prev_id3'],#57
			rr['rr_h_prev_id4'],#58
			rr['rr_a_deviation'],#59
			rr['rr_a_deviation3f'],#60
			rr['rr_a_race_count'],#61	
			rr['rr_r_err'],#62	
			rr['rr_h_sc_prev_id1'],#63
			rr['rr_h_sc_prev_id2'],#64
			rr['rr_h_sc_prev_id3'],#65
			rr['rr_h_sc_prev_id4'],#66
			rr['upd']#67

			)

		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )			 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert2(accessor, rr):

	try:
		
		mdb = const.TBL_KJDB_RACE_RESULT
		template = """
			select 
				count(*) 
			from {0}  
				where 
						rr_r_id ='{1}' 
					and 
						rr_r_race ='{2}'
					and 
						rr_r_horse_id='{3}'
		"""
		cmd = template.format(mdb, 
							rr['rr_r_id'],
							rr['rr_r_race'],
							rr['rr_r_horse_id'],
							)
		accessor.execute(cmd)
		count=0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			template = """
					insert into {0} 
					(  
						rr_r_id,
						rr_r_race,
						rr_r_horse_id,
						rr_r_horse_no,
						rr_r_horse_name,
						rr_r_rank,
						rr_r_waku,
						rr_r_blinker,
						rr_r_age,
						rr_r_gender,
						rr_r_burden,
						rr_r_jockey,
						rr_r_j_id,
						rr_r_j_mark,
						rr_r_time,
						rr_r_diff1,
						rr_r_diff2,
						rr_r_diff3,
						rr_r_f3_time,
						rr_r_weight,
						rr_r_gal_sign,
						rr_r_gal_val,
						rr_r_trainer,
						rr_r_t_id,
						rr_r_vote,
						rr_r_corner1,
						rr_r_corner2,
						rr_r_corner3,
						rr_r_corner4,
						rr_r_horse_sign,
						rr_r_varieties,
						rr_r_belongs,
						rr_r_o_id,
						rr_r_odds,
						rr_r_time_diff,
						rr_m_jra_bilongs,
						rr_m_blood01,
						rr_m_blood02,
						rr_m_blood03,
						rr_m_blood04,
						rr_m_blood05,
						rr_m_blood06,
						rr_m_blood07,
						rr_m_blood08,
						rr_m_blood09,
						rr_m_blood10,
						rr_m_blood11,
						rr_m_blood12,
						rr_m_blood13,
						rr_m_blood14,
						rr_m_feet1,
						rr_m_feet2,
						rr_m_feet3,
						rr_m_feet4,
						rr_h_prev_id1,
						rr_h_prev_id2,
						rr_h_prev_id3,
						rr_h_prev_id4,
						rr_a_deviation,
						rr_a_deviation3f,
						rr_a_race_count,
						rr_r_err,
						rr_h_sc_prev_id1,
						rr_h_sc_prev_id2,
						rr_h_sc_prev_id3,
						rr_h_sc_prev_id4,
						upd
						) values (
						'{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}',
						'{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}',
						'{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}',
						'{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}','{40}',
						'{41}','{42}','{43}','{44}','{45}','{46}','{47}','{48}','{49}','{50}',
						'{51}','{52}','{53}','{54}','{55}','{56}','{57}','{58}', {59} , {60} ,
						 {61} ,'{62}','{63}','{64}','{65}','{66}', {67}
						)
						"""
		else:
			template = """
					update {0} 
					set 
						rr_r_horse_no='{4}',
						rr_r_horse_name='{5}',
						rr_r_rank='{6}',
						rr_r_waku='{7}',
						rr_r_blinker='{8}',
						rr_r_age='{9}',
						rr_r_gender='{10}',
						rr_r_burden='{11}',
						rr_r_jockey='{12}',
						rr_r_j_id='{13}',
						rr_r_j_mark='{14}',
						rr_r_time='{15}',
						rr_r_diff1='{16}',
						rr_r_diff2='{17}',
						rr_r_diff3='{18}',
						rr_r_f3_time='{19}',
						rr_r_weight='{20}',
						rr_r_gal_sign='{21}',
						rr_r_gal_val='{22}',
						rr_r_trainer='{23}',
						rr_r_t_id='{24}',
						rr_r_vote ='{25}',
						rr_r_corner1 ='{26}',
						rr_r_corner2 ='{27}',
						rr_r_corner3 ='{28}',
						rr_r_corner4 ='{29}',
						rr_r_horse_sign ='{30}',
						rr_r_varieties='{31}',
						rr_r_belongs='{32}',
						rr_r_o_id='{33}',
						rr_r_odds='{34}',
						rr_r_time_diff='{35}',
						rr_m_jra_bilongs='{36}',
						rr_m_blood01='{37}',
						rr_m_blood02='{38}',
						rr_m_blood03='{39}',
						rr_m_blood04='{40}',
						rr_m_blood05='{41}',
						rr_m_blood06='{42}',
						rr_m_blood07='{43}',
						rr_m_blood08='{44}',
						rr_m_blood09='{45}',
						rr_m_blood10='{46}',
						rr_m_blood11='{47}',
						rr_m_blood12='{48}',
						rr_m_blood13='{49}',
						rr_m_blood14='{50}',
						rr_m_feet1='{51}',
						rr_m_feet2='{52}',
						rr_m_feet3='{53}',
						rr_m_feet4='{54}',
						rr_h_prev_id1='{55}',
						rr_h_prev_id2='{56}',
						rr_h_prev_id3='{57}',
						rr_h_prev_id4='{58}',
						rr_a_deviation={59},
						rr_a_deviation3f={60},
						rr_a_race_count ={61},
						rr_r_err='{62}',
						rr_h_sc_prev_id1='{63}',
						rr_h_sc_prev_id2='{64}',
						rr_h_sc_prev_id3='{65}',
						rr_h_sc_prev_id4='{66}',
						upd={67}

					where 
						rr_r_id='{1}' 
						and 
						rr_r_race='{2}' 
						and 
						rr_r_horse_id='{3}' 
						"""	
		accessor.cur_close()
		cmd = template.format(
			mdb,#0
			rr['rr_r_id'], #1
			rr['rr_r_race'],#2
			rr['rr_r_horse_id'],#3
			rr['rr_r_horse_no'],#4
			rr['rr_r_horse_name'],#5
			rr['rr_r_rank'],#6
			rr['rr_r_waku'],#7
			rr['rr_r_blinker'],#8
			rr['rr_r_age'],#9
			rr['rr_r_gender'],#10
			rr['rr_r_burden'],#11
			rr['rr_r_jockey'],#12
			rr['rr_r_j_id'],#13
			rr['rr_r_j_mark'],#14
			rr['rr_r_time'],#15
			rr['rr_r_diff1'],#16
			rr['rr_r_diff2'],#17
			rr['rr_r_diff3'],#18
			rr['rr_r_f3_time'],#19
			rr['rr_r_weight'],#20
			rr['rr_r_gal_sign'],#21
			rr['rr_r_gal_val'],#22
			rr['rr_r_trainer'],#23
			rr['rr_r_t_id'],#24
			rr['rr_r_vote'],#25
			rr['rr_r_corner1'],#26
			rr['rr_r_corner2'],#27
			rr['rr_r_corner3'],#28
			rr['rr_r_corner4'],#29
			rr['rr_r_horse_sign'],#30
			rr['rr_r_varieties'],#31
			rr['rr_r_belongs'],#32
			rr['rr_r_o_id'],#33
			rr['rr_r_odds'],#34
			rr['rr_r_time_diff'],#35
			rr['rr_m_jra_bilongs'],#36
			rr['rr_m_blood01'],#37
			rr['rr_m_blood02'],#38
			rr['rr_m_blood03'],#39
			rr['rr_m_blood04'],#40
			rr['rr_m_blood05'],#41
			rr['rr_m_blood06'],#42
			rr['rr_m_blood07'],#43
			rr['rr_m_blood08'],#44
			rr['rr_m_blood09'],#45
			rr['rr_m_blood10'],#46
			rr['rr_m_blood11'],#47
			rr['rr_m_blood12'],#48
			rr['rr_m_blood13'],#49
			rr['rr_m_blood14'],#50
			rr['rr_m_feet1'],#51
			rr['rr_m_feet2'],#52
			rr['rr_m_feet3'],#53
			rr['rr_m_feet4'],#54
			rr['rr_h_prev_id1'],#55
			rr['rr_h_prev_id2'],#56
			rr['rr_h_prev_id3'],#57
			rr['rr_h_prev_id4'],#58
			rr['rr_a_deviation'],#59
			rr['rr_a_deviation3f'],#60
			rr['rr_a_race_count'],#61	
			rr['rr_r_err'],#62	
			rr['rr_h_sc_prev_id1'],#63
			rr['rr_h_sc_prev_id2'],#64
			rr['rr_h_sc_prev_id3'],#65
			rr['rr_h_sc_prev_id4'],#66
			rr['upd']#67

			)

		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )			 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
def update_hot(accessor, rr):

	try:
		#2019110203
		rr_r_id =rr['rr_r_id']
		y = rr_r_id[:4]
		
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		template = """
			select 
				count(*) 
			from {0}  
				where 
						rr_r_id ='{1}' 
					and 
						rr_r_race ='{2}'
					and 
						rr_r_horse_id='{3}'
		"""
		cmd = template.format(mdb, 
							rr['rr_r_id'],
							rr['rr_r_race'],
							rr['rr_r_horse_id'],
							)
		accessor.execute(cmd)
		count=0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to do...
		else:
			template = """
					update {0} 
					set 
						rr_r_weight='{4}',
						rr_r_gal_sign='{5}',
						rr_r_gal_val='{6}',
						rr_r_vote ='{7}',
						rr_r_odds='{8}'
					where 
						rr_r_id='{1}' 
						and 
						rr_r_race='{2}' 
						and 
						rr_r_horse_id='{3}' 
						"""	
		accessor.cur_close()
		cmd = template.format(
			mdb,#0
			rr['rr_r_id'], #1
			rr['rr_r_race'],#2
			rr['rr_r_horse_id'],#3
			rr['rr_r_weight'],#4
			rr['rr_r_gal_sign'],#5
			rr['rr_r_gal_val'],#6
			rr['rr_r_vote'],#7
			rr['rr_r_odds'],#8
			)

			 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert_comment(accessor, id, horse_name, comment):

	try:
		#2019110203
		rr_r_id =id
		y = int(rr_r_id/1000000)
	   
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)	   
		template = """
			update {0} 
			set 
				rr_r_comment='{3}'
			where 
				rr_r_id={1} 
			and 
				rr_r_horse_name='{2}'
		"""
		cmd = template.format(
			mdb,
			id,
			horse_name,
			comment
			)
	
		accessor.execute(cmd)
		accessor.commit()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

def upsert_prev_id(accessor, rr):

	try:
		#2019110203
		rr_r_id =rr['rr_r_id']
		y = rr_r_id[:4]
		if(1999 < int(y)):
			mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
			template = """
				select 
					count(*) 
				from {0}  
					where 
							rr_r_id ='{1}'
						and 
							rr_r_race='{2}'
						and 
							rr_r_horse_id='{3}'
			"""
			cmd = template.format(mdb, 
								rr['rr_r_id'],
								rr['rr_r_race'],
								rr['rr_r_horse_id']
								)
			accessor.execute(cmd)
						
			for c in accessor.cur.fetchall():
				count = int(c[0])
				break	  
			if 0 ==  count:  
			
				print("bat insert!",rr['rr_r_id'],
								rr['rr_r_race'],
								rr['rr_r_horse_id'])
			else:
				template = """
						update {0} 
						set 
					
							rr_h_prev_id1='{4}',
							rr_h_prev_id2='{5}',
							rr_h_prev_id3='{6}',
							rr_h_prev_id4='{7}',
							upd={8}
						where 
							rr_r_id='{1}' 
							and 
							rr_r_race='{2}' 
							and 
							rr_r_horse_id='{3}'
							"""
			accessor.cur_close()
			cmd = template.format(
				mdb,
				rr['rr_r_id'],
				rr['rr_r_race'],
				rr['rr_r_horse_id'],
				rr['rr_h_prev_id1'],
				rr['rr_h_prev_id2'],
				rr['rr_h_prev_id3'],
				rr['rr_h_prev_id4'],
				rr['upd']
				)

						
			accessor.execute(cmd)
			accessor.commit()
			accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	 


def update_deviations(accessor, rr):

	try:
		rr_r_id =rr['rr_r_id']
		y = rr_r_id[:4]
		
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		template = """
			select 
				count(*) 
			from {0}  
				where 
						rr_r_id ='{1}' 
					and 
						rr_r_race ='{2}'
					and 
						rr_r_horse_id='{3}'
		"""
		cmd = template.format(mdb, 
							rr['rr_r_id'],
							rr['rr_r_race'],
							rr['rr_r_horse_id'],
							)
		accessor.execute(cmd)
		count=0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to do...
		else:
			template = """
					update {0} 
					set 
						rr_a_deviation={4},
						rr_a_deviation3f={5},
      					upd={6}
					where 
						rr_r_id='{1}' 
						and 
						rr_r_race='{2}' 
						and 
						rr_r_horse_id='{3}' 
						"""	
		accessor.cur_close()
		cmd = template.format(
			mdb,#0
			rr['rr_r_id'], #1
			rr['rr_r_race'],#2
			rr['rr_r_horse_id'],#3
			rr['rr_a_deviation'],#4
			rr['rr_a_deviation3f'],#5
   			rr['upd'],#6
			)

			 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert_sc_prev_id(accessor, rr):

	try:
		#2019110203
		rr_r_id =rr['rr_r_id']
		y = rr_r_id[:4]
		if(1999 < int(y)):
			mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
			template = """
				select 
					count(*) 
				from {0}  
					where 
							rr_r_id ='{1}'
						and 
							rr_r_race='{2}'
						and 
							rr_r_horse_id='{3}'
			"""
			cmd = template.format(mdb, 
								rr['rr_r_id'],
								rr['rr_r_race'],
								rr['rr_r_horse_id']
								)
			accessor.execute(cmd)
						
			for c in accessor.cur.fetchall():
				count = int(c[0])
				break	  
			if 0 ==  count:  
			
				print("bat insert!",rr['rr_r_id'],
								rr['rr_r_race'],
								rr['rr_r_horse_id'])
			else:
				template = """
						update {0} 
						set 
							rr_h_sc_prev_id1='{4}',
							rr_h_sc_prev_id2='{5}',
							rr_h_sc_prev_id3='{6}',
							rr_h_sc_prev_id4='{7}',
							upd={8}
						where 
							rr_r_id='{1}' 
							and 
							rr_r_race='{2}' 
							and 
							rr_r_horse_id='{3}'
							"""
			accessor.cur_close()
			cmd = template.format(
				mdb,
				rr['rr_r_id'],
				rr['rr_r_race'],
				rr['rr_r_horse_id'],
				rr['rr_h_sc_prev_id1'],
				rr['rr_h_sc_prev_id2'],
				rr['rr_h_sc_prev_id3'],
				rr['rr_h_sc_prev_id4'],
				rr['upd']
				)

						
			accessor.execute(cmd)
			accessor.commit()
			accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	



def upsert_sc_prev_id_to_file(file, rr):

	try:
		#2019110203
		rr_r_id =rr['rr_r_id']
		y = rr_r_id[:4]
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)

		template = """
				update {0} 
				set 
					rr_h_sc_prev_id1='{4}',
					rr_h_sc_prev_id2='{5}',
					rr_h_sc_prev_id3='{6}',
					rr_h_sc_prev_id4='{7}',
					upd={8}
				where 
					rr_r_id='{1}' 
					and 
					rr_r_race='{2}' 
					and 
					rr_r_horse_id='{3}';
					"""
		cmd = template.format(
			mdb,
			rr['rr_r_id'],
			rr['rr_r_race'],
			rr['rr_r_horse_id'],
			rr['rr_h_sc_prev_id1'],
			rr['rr_h_sc_prev_id2'],
			rr['rr_h_sc_prev_id3'],
			rr['rr_h_sc_prev_id4'],
			rr['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		path = rf"C:\temp\{file}.txt"	
		with open(path,  mode='a') as f:
			f.write(f"{cmd}\n")

	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	 

def upsert_bloods(accessor, rr):

	try:
		#2019110203
		rr_r_id =rr['rr_r_id']
		y = rr_r_id[:4]
		
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		template = """
			select 
				count(*) 
			from {0}  
				where 
						rr_r_id ='{1}' 
					and 
						rr_r_race ='{2}'
					and 
						rr_r_horse_id='{3}'
		"""
		cmd = template.format(mdb, 
							rr['rr_r_id'],
							rr['rr_r_race'],
							rr['rr_r_horse_id'],
							)
		accessor.execute(cmd)
		count=0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			template = """
					insert into {0} 
					(  
						rr_r_id,
						rr_r_race,
						rr_r_horse_id,
						rr_m_blood01,
						rr_m_blood02,
						rr_m_blood03,
						rr_m_blood04,
						rr_m_blood05,
						rr_m_blood06,
						rr_m_blood07,
						rr_m_blood08,
						rr_m_blood09,
						rr_m_blood10,
						rr_m_blood11,
						rr_m_blood12,
						rr_m_blood13,
						rr_m_blood14,
						upd
						) values (
						'{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}',
						'{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}'
						)
						"""
		else:
			template = """
					update {0} 
					set 
						rr_m_blood01='{4}',
						rr_m_blood02='{5}',
						rr_m_blood03='{6}',
						rr_m_blood04='{7}',
						rr_m_blood05='{8}',
						rr_m_blood06='{9}',
						rr_m_blood07='{10}',
						rr_m_blood08='{11}',
						rr_m_blood09='{12}',
						rr_m_blood10='{13}',
						rr_m_blood11='{14}',
						rr_m_blood12='{15}',
						rr_m_blood13='{16}',
						rr_m_blood14='{17}',
						upd={18}

					where 
						rr_r_id='{1}' 
						and 
						rr_r_race='{2}' 
						and 
						rr_r_horse_id='{3}' 
						"""	
		accessor.cur_close()
		cmd = template.format(
			mdb,#0
			rr['rr_r_id'], #1
			rr['rr_r_race'],#2
			rr['rr_r_horse_id'],#3
			rr['rr_m_blood01'],#4
			rr['rr_m_blood02'],#5
			rr['rr_m_blood03'],#6
			rr['rr_m_blood04'],#7
			rr['rr_m_blood05'],#8
			rr['rr_m_blood06'],#9
			rr['rr_m_blood07'],#10
			rr['rr_m_blood08'],#11
			rr['rr_m_blood09'],#12
			rr['rr_m_blood10'],#13
			rr['rr_m_blood11'],#14
			rr['rr_m_blood12'],#15
			rr['rr_m_blood13'],#16
			rr['rr_m_blood14'],#17
			rr['upd']#18

			)

			 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert_bloods_id(accessor, y,  rr, is_direct =False):

	try:
		if(False == is_direct):
			mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		else:
			mdb = const.TBL_KJDB_RACE_RESULT
		
		template = """
				update {0} 
				set 
					rr_m_blood01='{2}',
					rr_m_blood02='{3}',
					rr_m_blood03='{4}',
					rr_m_blood04='{5}',
					rr_m_blood05='{6}',
					rr_m_blood06='{7}',
					rr_m_blood07='{8}',
					rr_m_blood08='{9}',
					rr_m_blood09='{10}',
					rr_m_blood10='{11}',
					rr_m_blood11='{12}',
					rr_m_blood12='{13}',
					rr_m_blood13='{14}',
					rr_m_blood14='{15}',
					upd=2
				where 
					rr_r_horse_id='{1}' 
					"""	
		cmd = template.format(
			mdb,#0
			rr['rr_r_horse_id'], #1
			rr['rr_m_blood01'],#4
			rr['rr_m_blood02'],#5
			rr['rr_m_blood03'],#6
			rr['rr_m_blood04'],#7
			rr['rr_m_blood05'],#8
			rr['rr_m_blood06'],#9
			rr['rr_m_blood07'],#10
			rr['rr_m_blood08'],#11
			rr['rr_m_blood09'],#12
			rr['rr_m_blood10'],#13
			rr['rr_m_blood11'],#14
			rr['rr_m_blood12'],#15
			rr['rr_m_blood13'],#16
			rr['rr_m_blood14'],#17

			)
		accessor.cur_close()
		
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )			 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

