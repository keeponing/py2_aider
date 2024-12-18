# 主牡馬スコア
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, id, name):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				mt_id ='{1}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_MASTER_TRAINER,
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
						mt_id,
						mt_name,
						upd
					) values (
						'{1}','{2}',1
					)
					"""
		else:
			template = """
					update 
						{0} 
					set
						mt_name ='{2}',
						upd=1
					where 
						mt_id ='{1}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_MASTER_TRAINER, 
			id,
			name
			)
					 
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
# 				mt_id ='{1}' 
# 			"""
# 		cmd = template.format(
# 			const.TBL_KJDB_MASTER_TRAINER,
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
# 						mt_id,
# 						mt_cluster,
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
# 						mt_cluster ='{2}',
# 						upd=1
# 					where 
# 						mt_id ='{1}'
					   
# 					"""

# 		accessor.cur_close()
# 		cmd = template.format(
# 			const.TBL_KJDB_MASTER_TRAINER, 
# 			id,
# 			cluster
# 			)
# 		cmd = cmd.replace( '\n' , ' ' )
# 		cmd = cmd.replace( '\t' , ' ' )		
# 		accessor.execute(cmd)
# 		accessor.commit()
# 		accessor.cur_close()
# 	except Exception as e:
# 		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		

