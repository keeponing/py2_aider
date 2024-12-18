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
				cm_id ='{1}' 
				and
				cm_horse_name='{2}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_COMMENT,
			js['cm_id'],
			js['cm_horse_name'],
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
						cm_id,
						cm_horse_id,
						cm_horse_name,
						cm_comment
					) values (
							'{1}','{2}','{3}','{4}'
					)
					"""
		else:
			template = """
					update {0} 
					set
						cm_horse_name='{3}',
						cm_comment='{4}'		
					where 
							cm_id ='{1}'
						and
							cm_horse_id ='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_COMMENT, 
			js['cm_id'],
			js['cm_horse_id'],
			js['cm_horse_name'],
			js['cm_comment']
			)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
	