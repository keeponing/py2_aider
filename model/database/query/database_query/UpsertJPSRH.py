#Jra S レースヘッダ
import os
import inspect

import model.conf.KJraConst as const


def upsert(accessor, rh):

	try:
		template = """
			select count(*) 
			from {0}  
			where 
			rh_id ='{1}'
			and 
			rh_race='{2}' 
			"""
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
							rh['rh_id'],
							rh['rh_race']
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
						rh_id,
						rh_race,
						rh_race_hm,
						rh_weather,
						rh_track,
						rh_turf_condition,
						rh_dirt_condition,
						rh_race_name,
						rh_category,
						rh_class2,
						rh_class3,
						rh_class4,
						rh_class5over,
						rh_classYoung,
						rh_rule,
						rh_weight,
						rh_distance,
						rh_corner,
						rh_horse_count,
						rh_grade
					) values (
							'{1}',  '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}',
							'{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}'
					)
					"""
		else:
			template = """
					update {0} 
					set 
						rh_race_hm ='{3}',
						rh_weather ='{4}',
						rh_track ='{5}',
						rh_turf_condition ='{6}',
						rh_dirt_condition ='{7}',
						rh_race_name ='{8}',
						rh_category ='{9}',
						rh_class2 ='{10}',
						rh_class3 ='{11}',
						rh_class4 ='{12}',
						rh_class5over ='{13}',
						rh_classYoung ='{14}',
						rh_rule ='{15}',
						rh_weight ='{16}',
						rh_distance ='{17}',
						rh_corner ='{18}',
						rh_horse_count ='{19}',
						rh_grade ='{20}'
					where 
						rh_id='{1}'
					and 
						rh_race='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(const.TBL_KJDB_RACE_HEADER, 
			rh['rh_id'],
			rh['rh_race'],
			rh['rh_race_hm'],
			rh['rh_weather'],
			rh['rh_track'],
			rh['rh_turf_condition'],
			rh['rh_dirt_condition'],
			rh['rh_race_name'],
			rh['rh_category'],
			rh['rh_class2'],
			rh['rh_class3'],
			rh['rh_class4'],
			rh['rh_class5over'],
			rh['rh_classYoung'],
			rh['rh_rule'],
			rh['rh_weight'],
			rh['rh_distance'],
			rh['rh_corner'],
			rh['rh_horse_count'],
			rh['rh_grade']
		)
					 
		accessor.execute(cmd)
		accessor.commit()
		accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

