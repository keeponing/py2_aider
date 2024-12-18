# 調教師スコア
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, ts):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}
			where	
					ts_id ='{1}' 
				and
					ts_year = '{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_TRAINER_SCORE,
			ts['ts_id'],
			ts['ts_year']
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
						ts_id,
						ts_year,
						ts_win_score,
						ts_mul_score,
						ts_race_count,
						ts_win_count,
						ts_mul_count
					) values (
							'{1}','{2}',{3},{4},{5}, {6} ,{7}
					)
					"""
		else:
			template = """
					update {0} 
					set
						ts_win_score={3},
						ts_mul_score={4},
						ts_race_count={5},
						ts_win_count={6},
						ts_mul_count={7}		
					where 
							ts_id ='{1}'
						and
							ts_year ='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_TRAINER_SCORE, 
			ts['ts_id'],
			ts['ts_year'],
			ts['ts_win_score'],
			ts['ts_mul_score'],
			ts['ts_race_count'],
			ts['ts_win_count'],
			ts['ts_mul_count']
			)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

