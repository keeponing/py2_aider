# 基準タイム
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, at):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}
			where	
					at_year = '{1}'
				and 
					at_place ='{2}'
				and
					at_distance = '{3}'
				and 
					at_track_cd ='{4}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_AVERAGE_TIME_MAIDEN_RACE,
			at['at_year'],
			at['at_place'],
			at['at_distance'],
			at['at_track_cd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )		
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			template = """
					insert into {0} 
					( 
						at_year,
						at_place,
						at_distance,
						at_track_cd,
						at_count,
						at_base_time,
						at_base_time_std,
						at_3f_time,
						at_3f_time_std,
						upd
					) values (
							'{1}','{2}','{3}','{4}',{5},{6},{7},{8},{9},{10}
					)
					"""
		else:
			template = """
					update {0} 
					set
						at_count ={5},
						at_base_time={6},
						at_base_time_std={7},
						at_3f_time={8},
						at_3f_time_std={9},
						upd={10}	
					where 
							at_year ='{1}'
						and
							at_place ='{2}'
						and
							at_distance='{3}'
						and	 
							at_track_cd='{4}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_AVERAGE_TIME_MAIDEN_RACE,
			at['at_year'],
			at['at_place'],
			at['at_distance'],
			at['at_track_cd'],
			at['at_count'],
			at['at_base_time'],
			at['at_base_time_std'],
			at['at_3f_time'],
			at['at_3f_time_std'],
			at['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
