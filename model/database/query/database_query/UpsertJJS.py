# 調教師スコア
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, js):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}
			where	
					js_id ='{1}' 
				and
					js_year = '{2}'
			"""
		cmd = template.format(
			const.TBL_KJDB_JOCKEY_SCORE,
			js['js_id'],
			js['js_year']
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
						js_id,
						js_year,
						js_win_score,
						js_mul_score,
						js_race_count,
						js_win_count,
						js_mul_count
					) values (
							'{1}','{2}',{3},{4},{5}, {6} ,{7}
					)
					"""
		else:
			template = """
					update {0} 
					set
						js_win_score={3},
						js_mul_score={4},
						js_race_count={5},
						js_win_count={6},
						js_mul_count={7}		
					where 
							js_id ='{1}'
						and
							js_year ='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_JOCKEY_SCORE, 
			js['js_id'],
			js['js_year'],
			js['js_win_score'],
			js['js_mul_score'],
			js['js_race_count'],
			js['js_win_count'],
			js['js_mul_count']
			)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
