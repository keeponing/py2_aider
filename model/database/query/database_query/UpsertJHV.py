# 主牡馬スコア
import os
import inspect
import model.conf.KJraConst as const


def upsert(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				key_program_id='{1}'
				and
				key_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_HV_CACHE_VALIABLE,
			sv['key_program_id'],
			sv['key_horse_id']
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
						key_program_id,
						key_horse_id,
						desc_race_no,
						his_l4_p1,
						his_l4_p2,
						his_l4_p3,
						his_l4_p4,
						his_sc_l4_p1,
						his_sc_l4_p2,
						his_sc_l4_p3,
						his_sc_l4_p4,
						upd
					) values (
						'{1}' ,'{2}' , {3}  , {4}  , {5}  , {6}  , {7}  , {8} , {9}  , {10}  , {11}  , {12} 
					)
					"""
		else:
			template = """
					update 
						{0} 
					set
						desc_race_no ={3},
						his_l4_p1 ={4},
						his_l4_p2 ={5},
						his_l4_p3 ={6},
						his_l4_p4 ={7},
						his_sc_l4_p1 ={8},
						his_sc_l4_p2 ={9},
						his_sc_l4_p3 ={10},
						his_sc_l4_p4 ={11},
						upd ={12}
					where 
						key_program_id='{1}'
						and
						key_horse_id ='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_HV_CACHE_VALIABLE, 
			sv['key_program_id'],
			sv['key_horse_id'],
			sv['desc_race_no'],
			sv['his_l4_p1'],
			sv['his_l4_p2'],
			sv['his_l4_p3'],
			sv['his_l4_p4'],	
			sv['his_sc_l4_p1'],
			sv['his_sc_l4_p2'],
			sv['his_sc_l4_p3'],
			sv['his_sc_l4_p4'],	
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
		# y = sv['sv_program_id'][:4]
		# with  open(r'c:\temp\sv_{0}.sql'.format(y), 'a') as f:
		# 	f.write(cmd+';\n')		
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def upsert_sc(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				key_program_id='{1}'
				and
				key_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_HV_CACHE_VALIABLE,
			sv['key_program_id'],
			sv['key_horse_id']
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
						key_program_id,
						key_horse_id,
						desc_race_no,
						his_sc_l4_p1,
						his_sc_l4_p2,
						his_sc_l4_p3,
						his_sc_l4_p4,
						upd
					) values (
						'{1}' ,'{2}' , {3}  , {4}  , {5}  , {6}  , {7}  , {8} 
					)
					"""
		else:
			template = """
					update 
						{0} 
					set
						desc_race_no ={3},
						his_sc_l4_p1 ={4},
						his_sc_l4_p2 ={5},
						his_sc_l4_p3 ={6},
						his_sc_l4_p4 ={7},
						upd ={8}
					where 
						key_program_id='{1}'
						and
						key_horse_id ='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_HV_CACHE_VALIABLE, 
			sv['key_program_id'],
			sv['key_horse_id'],
			sv['desc_race_no'],
			sv['his_sc_l4_p1'],
			sv['his_sc_l4_p2'],
			sv['his_sc_l4_p3'],
			sv['his_sc_l4_p4'],	
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
		# y = sv['sv_program_id'][:4]
		# with  open(r'c:\temp\sv_{0}.sql'.format(y), 'a') as f:
		# 	f.write(cmd+';\n')		
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
