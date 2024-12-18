# 主牡馬スコア
import os
import inspect

import model.conf.KJraConst as const



def upsert(accessor, td):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}
			where 
					td_id ='{1}' 
			"""
		cmd = template.format(
			const.TBL_KJDB_TIME_DESCRIBES,
			td['td_id']
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
						td_id,
						td_place,
						td_distance,
						td_class2,
						td_class3,
						td_class4,
						td_class5over,
						td_classYoung,
						td_category,
						td_track,
						td_weather,
						td_turf_condition,
						td_dirt_condition,
						td_count,
						td_mean,
						td_std,
						td_mean_3f,
						td_std_3f
					) values (
							 '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}','{10}',
							'{11}','{12}','{13}',  {14},  {15},  {16},  {17},  {18}
					)
					"""

		else:
			template = """
					update {0} 
					set
						td_place ='{2}',
						td_distance ='{3}',
						td_class2 ='{4}',
						td_class3 ='{5}',
						td_class4 ='{6}',
						td_class5over ='{7}',
						td_classYoung ='{8}',
						td_category ='{9}',
						td_track ='{10}',
						td_weather ='{11}',
						td_turf_condition ='{12}',
						td_dirt_condition ='{13}',
						td_count={14},
						td_mean ={15},
						td_std ={16},
						td_mean_3f ={17},
						td_std_3f ={18}
					where 
						td_id ='{1}'
					"""

		accessor.cur_close()
		cmd = template.format(
			const.TBL_KJDB_TIME_DESCRIBES, 
			td["td_id"],
			td["td_place"],
			td["td_distance"],
			td["td_class2"],
			td["td_class3"],
			td["td_class4"],
			td["td_class5over"],
			td["td_classYoung"],
			td["td_category"],
			td["td_track_cd"],
			td["td_weather"],
			td["td_turf_condition"],
			td["td_dirt_condition"],
			td["td_count"] ,
			td["td_mean"] ,
			td["td_std"],
			td["td_mean_3f"],
			td["td_std_3f"]
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )			 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

