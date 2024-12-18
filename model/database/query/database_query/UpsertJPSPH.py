#Jra S プログラムヘッダ
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, ph):

	try:
		template = "select count(*) from {0}  where ph_id ='{1}' "
		cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER, 
							ph['ph_id']
							)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			template = """
				insert into 
					{0} 
					( 
						ph_id,
						ph_year,
						ph_monthday,
						ph_count,
						ph_place,
						ph_place_count		
					) 
					values (
						'{1}','{2}','{3}','{4}','{5}','{6}'
					)
				"""
		else:
			template = """
				update 
					{0} 
				set  
					ph_year ='{2}',
					ph_monthday ='{3}',
					ph_count ='{4}',
					ph_place ='{5}',
					ph_place_count ='{6}'
				where 
					ph_id='{1}'
				"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_PROGRAM_HEADER, 
				ph['ph_id'],
				ph['ph_year'],
				ph['ph_monthday'],
				ph['ph_count'],
				ph['ph_place'],
				ph['ph_place_count']
				)
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
