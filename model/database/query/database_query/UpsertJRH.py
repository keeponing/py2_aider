#Jra S レースヘッダ
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, rh):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							rh['rh_id'],
							rh['rh_race']
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			template = """
					insert into {0} 
					( 
						rh_id,
						rh_race,
						rh_race_hm,
						rh_weather,
						rh_track,
						rh_turf_condition,
						rh_dirt_condition,
						rh_race_name,
						rh_category,
						rh_class2,
						rh_class3,
						rh_class4,
						rh_class5over,
						rh_classYoung,
						rh_rule,
						rh_weight,
						rh_distance,
						rh_corner,
						rh_horse_count,
						rh_grade,
						rh_te_bpd_code,
						rh_te_bd_code,
						rh_te_c_code,
						rh_te_bpds_code,
						rh_sp_code,
						rh_te_c2_code,
						rh_avg_time,
						rh_avg_3f_time,
						rh_cnd_hash256,
						rh_ready
					) values (
							'{1}',  '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}',
							'{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}',
							'{21}','{22}','{23}','{24}','{25}','{26}', {27} , {28} ,'{29}', {30}
					)
					"""
		else:
			template = """
					update {0} 
					set 
						rh_race_hm ='{3}',
						rh_weather ='{4}',
						rh_track ='{5}',
						rh_turf_condition ='{6}',
						rh_dirt_condition ='{7}',
						rh_race_name ='{8}',
						rh_category ='{9}',
						rh_class2 ='{10}',
						rh_class3 ='{11}',
						rh_class4 ='{12}',
						rh_class5over ='{13}',
						rh_classYoung ='{14}',
						rh_rule ='{15}',
						rh_weight ='{16}',
						rh_distance ='{17}',
						rh_corner ='{18}',
						rh_horse_count ='{19}',
						rh_grade ='{20}',
						rh_te_bpd_code ='{21}',
						rh_te_bd_code ='{22}',
						rh_te_c_code ='{23}',
						rh_te_bpds_code ='{24}',
						rh_sp_code ='{25}',
						rh_te_c2_code='{26}',
						rh_avg_time={27},
						rh_avg_3f_time={28},
						rh_cnd_hash256='{29}',
						rh_ready ={30}
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
			rh['rh_id'],
			rh['rh_race'],
			rh['rh_race_hm'],
			rh['rh_weather'],
			rh['rh_track'],
			rh['rh_turf_condition'],
			rh['rh_dirt_condition'],
			rh['rh_race_name'],
			rh['rh_category'],
			rh['rh_class2'],
			rh['rh_class3'],
			rh['rh_class4'],
			rh['rh_class5over'],
			rh['rh_classYoung'],
			rh['rh_rule'],
			rh['rh_weight'],
			rh['rh_distance'],
			rh['rh_corner'],
			rh['rh_horse_count'],
			rh['rh_grade'],
			rh['rh_te_bpd_code'],
			rh['rh_te_bd_code'],
			rh['rh_te_c_code'],
			rh['rh_te_bpds_code'],
			rh['rh_sp_code'],
			rh['rh_te_c2_code'],
			rh['rh_avg_time'],
			rh['rh_avg_3f_time'],
			rh['rh_cnd_hash256'],
			rh['rh_ready']
		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		


def update_hot(accessor, rh):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							rh['rh_id'],
							rh['rh_race']
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			# Nothing to do...
		else:
			template = """
					update {0} 
					set 
						rh_weather ='{3}',
						rh_turf_condition ='{4}',
						rh_dirt_condition ='{5}'
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
			rh['rh_id'],
			rh['rh_race'],
			rh['rh_weather'],
			rh['rh_turf_condition'],
			rh['rh_dirt_condition']
		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert_bpd_tecode(accessor, program_id, race, te_code):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							program_id,
							race
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i =0 
		
		else:
			template = """
					update {0} 
					set 
						rh_te_bpd_code ='{3}'	
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
				program_id,
				race,
				te_code

		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert_bd_tecode(accessor, program_id, race, te_code):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							program_id,
							race
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i =0 
		
		else:
			template = """
					update {0} 
					set 
						rh_te_bd_code ='{3}'	
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
				program_id,
				race,
				te_code

		)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )				 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert_c_tecode(accessor, program_id, race, te_code):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							program_id,
							race
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i =0 
		
		else:
			template = """
					update {0} 
					set 
						rh_te_c_code ='{3}'	
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
				program_id,
				race,
				te_code

		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		

def upsert_c_tecode2(accessor, program_id, race, te_code, te_code2):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							program_id,
							race
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i =0 
		
		else:
			template = """
					update {0} 
					set 
						rh_te_c_code ='{3}'	,
						rh_te_c2_code='{4}'
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
				program_id,
				race,
				te_code,
				te_code2

		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		


def upsert_bpds_tecode(accessor, program_id, race, te_code):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							program_id,
							race
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i =0 
		
		else:
			template = """
					update {0} 
					set 
						rh_te_bpds_code ='{3}'	
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
				program_id,
				race,
				te_code

		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		


def upsert_average_time(accessor, rh):
	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							rh['rh_id'],
							rh['rh_race']
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i =0 
		
		else:
			template = """
					update {0} 
					set 
						rh_avg_time ={3},
						rh_avg_3f_time={4},
						rh_upd={5}
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
				rh['rh_id'],
				rh['rh_race'],
				rh['rh_avg_time'],
				rh['rh_avg_3f_time'],
				rh['upd']

		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		



def upsert_sh256(accessor, rh):
	try:
		
		template = """
					update {0} 
					set 
						rh_cnd_hash256 ='{3}',
						rh_upd={4}
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
				rh['rh_id'],
				rh['rh_race'],
				rh['rh_cnd_hash256'],
				rh['upd']

		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
