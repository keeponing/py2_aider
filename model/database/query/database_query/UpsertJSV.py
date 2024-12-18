# 主牡馬スコア
import os
import inspect
import model.conf.KJraConst as const


def upsert(accessor, sv):

	template = """
		select 
			count(*) 
		from 
			{0}  
		where 
			sv_program_id='{1}'
			and
			sv_horse_id ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
		sv['sv_program_id'],
		sv['sv_horse_id']
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
					sv_program_id,
					sv_horse_id,
					sv_feet_pb1,
					sv_feet_pb2,
					sv_feet_pb3,
					sv_feet_pb4,
					sv_burdern,
					sv_odds,
					sv_weight,
					sv_timediff,
					sv_deviation,
					sv_deviation3f,
					sv_win_ratio,
					sv_mul_ratio,
					sv_arg_dev,
					sv_arg_3fd,
					sv_straight_dev,
					sv_l_corner_dev,
					sv_r_corner_dev,
					sv_turf_dev,
					sv_dirt_dev,
					sv_sire_win_score,
					sv_sire_mul_score,
					sv_tr_score,
					sv_jk_score,
					sv_speed_exp,
					sv_speed_3f_exp,
					sv_speed_exp_l4,
					sv_vote,
					sv_win_score_wa,
					sv_mul_score_wa,
					upd
				) values (
					'{1}' ,'{2}' , {3}  , {4}  , {5}  , {6}  , {7}  , {8}  , {9}  , {10} ,
						{11} , {12} , {13} , {14} , {15} , {16} , {17} , {18} , {19} , {20} ,
						{21} , {22} , {23} , {24} , {25} , {26} , {17} , {28} , {29} , {30} ,
						{31} , {32} 
				)
				"""
	else:
		template = """
				update 
					{0} 
				set
					sv_feet_pb1 ={3},
					sv_feet_pb2 ={4},
					sv_feet_pb3 ={5},
					sv_feet_pb4 ={6},
					sv_burdern ={7},
					sv_odds ={8},
					sv_weight ={9},
					sv_timediff ={10},
					sv_deviation ={11},
					sv_deviation3f ={12},
					sv_win_ratio ={13},
					sv_mul_ratio ={14},
					sv_arg_dev={15},
					sv_arg_3fd={16},
					sv_straight_dev={17},
					sv_l_corner_dev={18},
					sv_r_corner_dev={19},
					sv_turf_dev={20},
					sv_dirt_dev={21},
					sv_sire_win_score={22},
					sv_sire_mul_score={23},
					sv_tr_score={24},
					sv_jk_score={25},
					sv_speed_exp={26},
					sv_speed_3f_exp={27},
					sv_speed_exp_l4={28},
					sv_vote={29},
					sv_win_score_wa={30},
					sv_mul_score_wa={31},
					upd={32}
				where 
					sv_program_id='{1}'
					and
					sv_horse_id ='{2}'
				"""
	accessor.cur_close()
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
		sv['sv_program_id'],
		sv['sv_horse_id'],
		sv['sv_feet_pb1'],
		sv['sv_feet_pb2'],
		sv['sv_feet_pb3'],
		sv['sv_feet_pb4'],
		sv['sv_burdern'],
		sv['sv_odds'],
		sv['sv_weight'],
		sv['sv_timediff'],
		sv['sv_deviation'],
		sv['sv_deviation3f'],
		sv['sv_win_ratio'],
		sv['sv_mul_ratio'],
		sv['sv_arg_dev'],
		sv['sv_arg_3fd'],
		sv['sv_straight_dev'],
		sv['sv_l_corner_dev'],
		sv['sv_r_corner_dev'],
		sv['sv_turf_dev'],
		sv['sv_dirt_dev'],
		sv['sv_sire_win_score'],
		sv['sv_sire_mul_score'],
		sv['sv_tr_score'],
		sv['sv_jk_score'],
		sv['sv_speed_exp'],
		sv['sv_speed_3f_exp'],
		sv['sv_speed_exp_l4'],	
		sv['sv_vote'],	
		sv['sv_win_score_wa'],	
		sv['sv_mul_score_wa'],	
		sv['upd']
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )						 
	accessor.execute(cmd)
	accessor.commit()
	accessor.cur_close()

  	
def update_hot(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			sv['sv_program_id'],
			sv['sv_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to dos
		else:
			template = """
					update 
						{0} 
					set
						sv_burdern ={3},
						sv_odds ={4},
						sv_vote ={5},
						upd={6}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			sv['sv_program_id'],
			sv['sv_horse_id'],
			sv['sv_burdern'],
			sv['sv_odds'],
			sv['sv_vote'],
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


  	
def update_speed_exponent(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			sv['sv_program_id'],
			sv['sv_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to dos
		else:
			template = """
					update 
						{0} 
					set
						sv_speed_exp ={3},
						upd={4}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			sv['sv_program_id'],
			sv['sv_horse_id'],
			sv['sv_speed_exp'],
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	
  

def update_speed_3f_exponent(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			sv['sv_program_id'],
			sv['sv_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to dos
		else:
			template = """
					update 
						{0} 
					set
						sv_speed_3f_exp ={3},
						upd={4}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			sv['sv_program_id'],
			sv['sv_horse_id'],
			sv['sv_speed_3f_exp'],
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

  

def update_speed_exp_l4(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			sv['sv_program_id'],
			sv['sv_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to dos
		else:
			template = """
					update 
						{0} 
					set
						sv_speed_exp_l4 ={3},
						upd={4}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			sv['sv_program_id'],
			sv['sv_horse_id'],
			sv['sv_speed_exp_l4'],
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	
  
  
def update_odds(accessor, program_id, horse_id, odds):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			program_id, 
			horse_id
			)
		accessor.execute(cmd)

		count = 0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to dos
		else:
			template = """
					update 
						{0} 
					set
						sv_odds ={3},
						upd={4}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			program_id, 
			horse_id, 
			odds,
			8
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

  
def update_timediff(accessor, program_id, horse_id, timediff):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			program_id, 
			horse_id
			)
		accessor.execute(cmd)

		count = 0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to dos
		else:
			template = """
					update 
						{0} 
					set
						sv_timediff ={3},
						upd={4}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			program_id, 
			horse_id, 
			timediff,
			9
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

  
  
def update_vote(accessor, program_id, horse_id, vote):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			program_id, 
			horse_id
			)
		accessor.execute(cmd)

		count = 0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
			#Nothing to dos
		else:
			template = """
					update 
						{0} 
					set
						sv_vote ={3},
						upd={4}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			program_id, 
			horse_id, 
			vote,
			9
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

  
    	

def upsert_sire_score(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			sv['sv_program_id'],
			sv['sv_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
		else:
			template = """
					update 
						{0} 
					set					
						sv_sire_win_score={3},
						sv_sire_mul_score={4},
						upd={5}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			sv['sv_program_id'],
			sv['sv_horse_id'],
			sv['sv_sire_win_score'],
			sv['sv_sire_mul_score'],
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()	
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	
  	

def upsert_jk_tr_score(accessor, sv):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				sv_program_id='{1}'
				and
				sv_horse_id ='{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			sv['sv_program_id'],
			sv['sv_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			i=0
		else:
			template = """
					update 
						{0} 
					set					
						sv_jk_score={3},
						sv_tr_score={4},
						sv_sire_win_score={5},
						sv_sire_mul_score={6},
						upd={7}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_STATISTICS_CACHE_VALIABLE, 
			sv['sv_program_id'],
			sv['sv_horse_id'],
			sv['sv_jk_score'],
			sv['sv_tr_score'],
			sv['sv_sire_win_score'],
			sv['sv_sire_mul_score'],
			sv['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()	
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	



def upsert_wa_score(accessor, sv):
	try:
		program_id = sv['sv_program_id']
		y = program_id[:4]
		if('0000'!= y):
	
			mdb = const.TBL_KJDB_STATISTICS_CACHE_VALIABLE_AT.format(y)

			# template = """
			# 	select 
			# 		count(*) 
			# 	from 
			# 		{0}  
			# 	where 
			# 		sv_program_id='{1}'
			# 		and
			# 		sv_horse_id ='{2}'
			# 	"""
			# cmd = template.format(
			# 	const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
			# 	sv['sv_program_id'],
			# 	sv['sv_horse_id']
			# 	)
			# accessor.execute(cmd)

			# count =0
			# for c in accessor.cur.fetchall():
			# 	count = int(c[0])
			# 	break	  
			# if 0 ==  count:  
			# 	i=0
			# else:
			template = """
					update 
						{0} 
					set			
						sv_win_ratio={3},
						sv_mul_ratio={4},		
						sv_win_score_wa={5},
						sv_mul_score_wa={6},
						upd={7}
					where 
						sv_program_id='{1}'
						and
						sv_horse_id ='{2}'
					"""
			accessor.cur_close()
			cmd = template.format(
				mdb, 
				sv['sv_program_id'],
				sv['sv_horse_id'],
				sv['sv_win_ratio'],
				sv['sv_mul_ratio'],
				sv['sv_win_score_wa'],
				sv['sv_mul_score_wa'],
				sv['upd']
				)
			cmd = cmd.replace( '\n' , ' ' )
			cmd = cmd.replace( '\t' , ' ' )						 
			accessor.execute(cmd)
			accessor.commit()
			accessor.cur_close()	
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
