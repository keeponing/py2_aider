# 主牡馬スコア
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, id, name, racecount=0, win_count=0, mul_count=0):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				ms_id ='{1}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_MASTER_SIRE,
			id
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
						ms_id,
						ms_name,
						ms_race_count,
						ms_win_count,
						ms_mul_count,
						upd
					) values (
						'{1}','{2}',{3},{4},{5},1
					)
					"""
		else:
			template = """
					update 
						{0} 
					set
						ms_name ='{2}',
						ms_race_count={3},
						ms_win_count={4},
						ms_mul_count={5},
						upd=1
					where 
						ms_id ='{1}'
					"""

		accessor.cur_close()

		cmd = template.format(
			const.TBL_KJDB_MASTER_SIRE, 
			id,
			name,
			racecount, 
			win_count, 
			mul_count
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , '' )					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		


def upsert_score(accessor, id, racecount, win_count, mul_count):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				ms_id ='{1}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_MASTER_SIRE,
			id
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
						ms_id,
						ms_race_count,
						ms_win_count,
						ms_mul_count,
						upd
					) values (
						'{1}',{2},{3},{4},1
					)
					"""
		else:
			template = """
					update 
						{0} 
					set
						ms_race_count={2},
						ms_win_count={3},
						ms_mul_count={4},
						upd=1
					where 
						ms_id ='{1}'
					"""

		accessor.cur_close()

		cmd = template.format(
			const.TBL_KJDB_MASTER_SIRE, 
			id,
			racecount, 
			win_count, 
			mul_count
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , '' )					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


# def upsert_cluster(accessor, id, cluster):

# 	try:
# 		template = """
# 			select 
# 				count(*) 
# 			from 
# 				{0}  
# 			where 
# 				ms_id ='{1}' 
# 			"""
# 		cmd = template.format(
# 			const.TBL_KJDB_MASTER_SIRE,
# 			id
# 			)
# 		accessor.execute(cmd)

# 		count =0
# 		for c in accessor.cur.fetchall():
# 			count = int(c[0])
# 			break	  
# 		if 0 ==  count:  
# 			template = """
# 					insert into {0} 
# 					( 
# 						ms_id,
# 						ms_cluster,
# 						upd
# 					) values (
# 						'{1}',{2},1
# 					)
# 					"""
# 		else:
# 			template = """
# 					update 
# 						{0} 
# 					set
# 						ms_cluster ={2},
# 						upd=1
# 					where 
# 						ms_id ='{1}'
					   
# 					"""

# 		accessor.cur_close()
# 		cmd = template.format(
# 			const.TBL_KJDB_MASTER_SIRE, 
# 			id,
# 			cluster
# 			)
					 
# 		accessor.execute(cmd)
# 		accessor.commit()
# 		accessor.cur_close()
# 	except Exception as e:
# 		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
