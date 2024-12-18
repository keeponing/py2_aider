# 基準タイム
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, bt):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}
			where	
					bt_year = '{1}'
				and 
					bt_place ='{2}'
				and
					bt_distance = '{3}'
				and 
					bt_track_cd ='{4}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_BASE_TIME,
			bt['bt_year'],
			bt['bt_place'],
			bt['bt_distance'],
			bt['bt_track_cd']
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
						bt_year,
						bt_place,
						bt_distance,
						bt_track_cd,
						bt_count,
						bt_base_time,
						bt_base_time_std,
						bt_3f_time,
						bt_3f_time_std,
						bt_dist_exponet,
						upd
					) values (
							'{1}','{2}','{3}','{4}',{5},{6},{7},{8},{9},{10},{11}
					)
					"""
		else:
			template = """
					update {0} 
					set
						bt_count ='{5}',
						bt_base_time={6},
						bt_base_time_std={7},
						bt_3f_time={8},
						bt_3f_time_std={9},
						bt_dist_exponet={10},
						upd={11}	
					where 
							bt_year ='{1}'
						and
							bt_place ='{2}'
						and
							bt_distance='{3}'
						and	 
							bt_track_cd='{4}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_BASE_TIME,
			bt['bt_year'],
			bt['bt_place'],
			bt['bt_distance'],
			bt['bt_track_cd'],
			bt['bt_count'],
			bt['bt_base_time'],
			bt['bt_base_time_std'],
			bt['bt_3f_time'],
			bt['bt_3f_time_std'],
			bt['bt_dist_exponet'],
			bt['upd']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
