# 主牡馬スコア
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, md):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
				md_id ='{1}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_MASTER_DEPARTMENT,
			md['horse_id']
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
						md_id,
						md_sire_id1,
						md_sire_id2,
						md_sire_id3,
						md_sire_id4,
						md_sire_id5,
						md_sire_id6,
						md_sire_id7,
						md_sire_id8,
						md_sire_id9,
						md_sire_id10,
						md_sire_id11,
						md_sire_id12,
						md_sire_id13,
						md_sire_id14,
						upd
					) values (
						'{1}' , '{2}', '{3}', '{4}', '{5}','{6}','{7}','{8}','{9}','{10}',
						'{11}','{12}','{13}','{14}','{15}',1
					)
					"""
		else:
			template = """
					update 
						{0} 
					set
						md_sire_id1 ='{2}',
						md_sire_id2 ='{3}',
						md_sire_id3 ='{4}',
						md_sire_id4 ='{5}',
						md_sire_id5 ='{6}',
						md_sire_id6 ='{7}',
						md_sire_id7 ='{8}',
						md_sire_id8 ='{9}',
						md_sire_id9 ='{10}',
						md_sire_id10 ='{11}',
						md_sire_id11 ='{12}',
						md_sire_id12 ='{13}',
						md_sire_id13 ='{14}',
						md_sire_id14 ='{15}',
						upd=1
					where 
						md_id ='{1}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_MASTER_DEPARTMENT, 
			md['horse_id'],
			md['sire_id1'],
			md['sire_id2'],
			md['sire_id3'],
			md['sire_id4'],
			md['sire_id5'],
			md['sire_id6'],
			md['sire_id7'],
			md['sire_id8'],
			md['sire_id9'],
			md['sire_id10'],
			md['sire_id11'],
			md['sire_id12'],
			md['sire_id13'],
			md['sire_id14']
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )						 
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
# 				md_id ='{1}' 
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
# 						md_id,
# 						md_cluster,
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
# 						md_cluster ='{2}',
# 						upd=1
# 					where 
# 						md_id ='{1}'
					   
# 					"""

# 		accessor.cur_close()
# 		cmd = template.format(
# 			const.TBL_KJDB_MASTER_TRAINER, 
# 			id,
# 			cluster
# 			)
					 
# 		accessor.execute(cmd)
# 		accessor.commit()
# 		accessor.cur_close()
# 	except Exception as e:
# 		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

