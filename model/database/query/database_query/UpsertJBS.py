# 主牡馬スコア
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, bs):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}
			where	
					bs_id ='{1}' 
				and
					bs_year = '{2}'
				and 
					bs_place ='{3}'
				and
					bs_distance = '{4}'
				and 
					bs_track ='{5}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_BLOOD_SCORE,
			bs['bs_id'],
			bs['bs_year'],
			bs['bs_place'],
			bs['bs_distance'],
			bs['bs_track']
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
						bs_id,
						bs_year,
						bs_place,	 
						bs_distance,  
						bs_track,
						bs_name,
						bs_win_score,
						bs_mul_score,
						bs_race_count,
						bs_win_count,
						bs_mul_count
					) values (
							'{1}','{2}','{3}','{4}','{5}','{6}',{7},{8},{9},{10},{11}
					)
					"""
		else:
			template = """
					update {0} 
					set
						bs_name ='{6}',
						bs_win_score={7},
						bs_mul_score={8},
						bs_race_count={9},
						bs_win_count={10},
						bs_mul_count={11}		
					where 
							bs_id ='{1}'
						and
							bs_year ='{2}'
						and
							bs_place='{3}'
						and	 
							bs_distance='{4}'
						and  
							bs_track='{5}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_BLOOD_SCORE, 
			bs['bs_id'],
			bs['bs_year'],
			bs['bs_place'],
			bs['bs_distance'],
			bs['bs_track'],
			bs['bs_name'],
			bs['bs_win_score'],
			bs['bs_mul_score'],
			bs['bs_race_count'],
			bs['bs_win_count'],
			bs['bs_mul_count']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		



def update_name(accessor, bs):

	try:
		template = """
				update {0} 
				set
					bs_name ='{2}'
				where 
					bs_id ='{1}'
				"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_BLOOD_SCORE, 
			bs['bs_id'],
			bs['bs_name'],
			)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
