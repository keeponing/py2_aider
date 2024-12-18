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
				mj_id ='{1}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_MASTER_JOCKEY,
			id
			)
		cmd = cmd.replace( '\n' , '' )
		cmd = cmd.replace( '\t' , '' )		
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count:  
			template = """
					insert into {0} 
					( 
						mj_id,
						mj_name,
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
						mj_name ='{2}',
						upd=1
					where 
						mj_id ='{1}'
					   
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_MASTER_JOCKEY, 
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
# 				mj_id ='{1}' 
# 			"""
# 		cmd = template.format(
# 			const.TBL_KJDB_MASTER_JOCKEY,
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
# 						mj_id,
# 						mj_cluster,
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
# 						mj_cluster ={2},
# 						upd=1
# 					where 
# 						mj_id ='{1}'
					   
# 					"""

# 		accessor.cur_close()
# 		cmd = template.format(
# 			const.TBL_KJDB_MASTER_JOCKEY, 
# 			id,
# 			cluster
# 			)
					 
# 		accessor.execute(cmd)
# 		accessor.commit()
# 		accessor.cur_close()
# 	except Exception as e:
# 		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
