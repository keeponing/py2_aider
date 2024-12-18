import os
import inspect

import model.conf.KJraConst as const

import pandas as pd
import time
def get_records_to_df(accessor):
	template = """
		select 
			* 
		from 
			{0} 
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_records_by_pid_to_df(accessor, program_id):
	y = program_id[:4]
	template = """
		select 
			* 
		from 
			{0} 
		where
			rr_r_id='{1}'
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		mdb,
		program_id
		)
	
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_records_by_pidr_to_df(accessor, program_id, race_no):
	y = program_id[:4]
	template = """
		select 
			* 
		from 
			{0} 
		where
			rr_r_id='{1}'
			and
			rr_r_race ='{2}'
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		mdb,
		program_id,
		race_no
		)
	
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_hid_by_pid_to_df(accessor, program_id):
	y = program_id[:4]
	template = """
		select 
			{0}.rr_r_horse_id 
		from 
			{0} 
		where
			rr_r_id='{1}'
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		mdb,
		program_id
		)
	
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

#データを取得
def get_records_y_to_df(accessor, y):
	template = """
		select
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
			(  
				{0}.ph_year='{3}'
			)
			order by 
				{0}.ph_id desc
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		mdb, 
		y
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret  


#データを取得
def get_records_y_to_df2(accessor, y):
	template = """
		select
			{0}.*
		from	   
			{0}
	
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		mdb
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_records_y_to_df3(accessor):
	template = """
		select
			{0}.*
		from	   
			{0}
	
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_RESULT
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret  
def get_zero_rank_by_ir_to_df(accessor, program_id, race_no):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template = """
		select 
			* 
		from 
			{0} 
		where
			rr_r_id='{1}'
			and
			rr_r_race ='{2}'
			and
			rr_r_rank='00'
		"""
	cmd = template.format(
		mdb,
		program_id,
		race_no
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  
#updが０のデータを取得
def get_non_upd_records_to_df(accessor, y):
	template = """
		select
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
			(  
				{0}.ph_year='{3}'
				and
				{2}.upd=0
			)
			order by 
				{0}.ph_id desc
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		mdb, 
		y
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_rank_by_jockey_id(accessor, jockey_id):
	
	template =  """
		select 
			{0}.rr_r_rank
		from {0}
		where  
			{0}.rr_r_j_id='{1}'
		order by 
 			{0}.rr_r_rank
	"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		jockey_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_rank_by_jockey_id2(accessor, y, jockey_id):
	if(1999 < int(y)):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)	
		template =  """
			select 
				CLng({0}.rr_r_rank) as rank
			from {0}
			where  
				{0}.rr_r_j_id='{1}'
			order by 
				{0}.rr_r_rank
		"""
		cmd = template.format(
			mdb, 
			jockey_id
			)
		
		ret = accessor.read_sql_to_df(cmd)   
	return ret
def get_rank_by_trainer_id(accessor, trainer_id):
	
	template =  """
		select 
			{0}.rr_r_rank
		from {0}
		where  
			{0}.rr_r_t_id='{1}'
		order by 
 			{0}.rr_r_rank
	"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		trainer_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_rank_by_trainer_id2(accessor, y, trainer_id):
	if(1999 < int(y)):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)	
		template =  """
			select 
				CLng({0}.rr_r_rank) as rank
			from {0}
			where  
				{0}.rr_r_t_id='{1}'
			order by 
				{0}.rr_r_rank
		"""
		cmd = template.format(
			mdb, 
			trainer_id
			)
		
		ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_rank_by_sire_id(accessor, sire_id):
	
	template =  """
		select 
			{0}.rr_r_rank
		from 
		({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race)
	
		where  
			{0}.rr_r_j_id='{1}'
		order by 
 			{0}.rr_r_rank
	"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		sire_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

#yearまでのデータを取得
def get_still_records_to_df(accessor, y):
	template = """
		select
			{0}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
			(
				int( {0}.ph_year) <= {3}
			)
			order by 
				{0}.ph_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		y
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret  


def is_existed(accessor,  program_id, horse_id):
	ret = False	
	y=program_id[:4]
	if(1999 < int(y)):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		template = """
			select 
				count(*) 
			from 
				{0} 
			where 
				rr_r_id='{1}'
			and 
				rr_r_horse_id='{2}'
			"""
		cmd = template.format(
			mdb,
			program_id,
			horse_id
			)
		accessor.execute(cmd)
		
		for c in accessor.cur.fetchall():
			ret = int(c[0])
			if(0 != ret):
				ret = True
			break
		accessor.cur_close()

	return ret

def is_existed2(accessor, program_id, horse_id):
	template = """
		select 
			count(*) 
		from 
			{0} 
		where 
			rr_r_id='{1}'
		and 
			rr_r_horse_id='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	accessor.execute(cmd)
	ret = False
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		if(0 != ret):
			ret = True
		break
	accessor.cur_close()

	return ret

def get_rank_list_by_id(accessor, horse_id):
	template ="""
		select 
			{0}.rr_r_rank
		from 
			{0} 
		where 
			rr_r_horse_id='{1}'
		"""
	cmd = template.format(
			const.VIEW_KJDB_RACE_RESULT, 
			horse_id)
	accessor.execute(cmd)

	# ret=[]
	# for c in accessor.cur.fetchall():
	# 	rank =c.rr_r_rank
	# 	ret.append(rank)
	# return ret
	ret = accessor.read_sql_to_df(cmd)
	return ret 

def get_record_list_by_hid(accessor, horse_id):
	template ="""
		select 
			{0}.*
		from 
			{0} 
		where 
			rr_r_horse_id='{1}'
		"""
	cmd = template.format(
			const.VIEW_KJDB_RACE_RESULT, 
			horse_id)
	accessor.execute(cmd)

	# ret=[]
	# for c in accessor.cur.fetchall():
	# 	rank =c.rr_r_rank
	# 	ret.append(rank)
	# return ret
	ret = accessor.read_sql_to_df(cmd)
	return ret 
#指定年のデータを返す。
def get_race_by_y(accessor, y):
	   
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_year={3}
		)
		order by 
 			{0}.ph_id desc
	"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		mdb, 
		y
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret


#指定年のレース成績を返す。
def get_race_result_by_ir(accessor, program_id, race):
	y = program_id[:4]
	template ="""
		select 
			* 
		from 
			{0} 
		where 
				rr_r_id='{1}' 
			and 
				rr_r_race='{2}'
			and 
				rr_r_horse_no<>'00'
		order by 
			rr_r_vote
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
			mdb, 
			program_id, 
			race)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#指定年のレース成績を返す。
def get_race_result_by_ir2(accessor, program_id, race):
	y = program_id[:4]
	template ="""
		select 
			* 
		from 
			{0} 
		where 
				rr_r_id='{1}' 
			and 
				rr_r_race='{2}'
			and
				rr_r_rank<>'00' 
		order by 
			rr_r_vote
		"""
			# order by 
			# rr_r_vote
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
			mdb, 
			program_id, 
			race)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#指定年のレース成績を返す。
def get_race_result_by_ir3(accessor, program_id, race):
	y = program_id[:4]
	template ="""
		select 
			* 
		from 
			{0} 
		where 
				rr_r_id='{1}' 
			and 
				rr_r_race='{2}'
			and
				rr_r_rank<>'00' 
		order by 
			rr_r_vote
		"""
			# order by 
			# rr_r_vote
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
			mdb, 
			program_id, 
			race)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_result_by_phid_to_sr(accessor, program_id, horse_id, is_direct=False):
	ret = pd.Series()
	y = program_id[:4]
	if(False == is_direct):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	else:
		mdb = const.TBL_KJDB_RACE_RESULT
	template = """
				select 
					* 
				from {0} 
				where 
					rr_r_id = '{1}'
				and 
					rr_r_horse_id = '{2}'
				"""
	cmd = template.format(
		mdb, 
		program_id,
		horse_id
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret


#最新の馬IDを返す
def get_latest_horse_id_by_name(accessor, horse_name):
	template = """
		select 
			{0}.rr_r_horse_id 
		from 
			{0} 
		where 
			{0}.rr_r_horse_name='{1}'
		order by {0}.rr_r_id desc
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		horse_name)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret =c.rr_r_horse_id
		break
	accessor.cur_close()  
	return ret

#指定馬の出走回数を返す
def get_race_ran_count_by_ii_union(accessor, id, horse_id):
	template = """
				select 
					count(*) 
				from {0} 
				where 
					rr_r_horse_id = {2}
				and 
					rr_r_id < {1}
				"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		id,
		horse_id
		)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret = int(c[0])
	accessor.cur_close()
	return ret
   
#指定馬の勝鞍を返す
def get_win_count_by_ii(accessor, id, horse_id):
 
	template = """
				select 
					count(*) 
				from {0} 
				where 
					{0}.rr_r_horse_id = {2}
				and 
					{0}.rr_r_id < {1}
				and 
					{0}.rr_r_rank=1
				"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		id,
		horse_id
		)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret = int(c[0])
	accessor.cur_close()
	return ret


#指定馬の複勝を返す
def get_mul_count_by_ii(accessor, id, horse_id):

	template = """
			select 
				count(*) 
			from {0} 
			where 
				{0}.rr_r_horse_id = {2}
			and 
				{0}.rr_r_id < {1}
			and 
				(
					{0}.rr_r_rank=1
				or 
					{0}.rr_r_rank=2
				or 
					{0}.rr_r_rank=3
				)
	"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		id,
		horse_id
		)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret = int(c[0])
	accessor.cur_close()
	return ret

#指定馬の出走回数を返す
def get_race_ran_count_by_ir2(accessor, id, horse_name, horse_id):
   
	template = """
				select 
					count(*) 
				from {0} 
				where 
					rr_r_horse_name = '{2}' 
				and 
					rr_r_horse_id = {3}
				and 
					rr_r_id < {1}
				and 
					rr_r_race_count <> 0
				"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT, 
		id,
		horse_name, 
		horse_id
		)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret = int(c[0])
	accessor.cur_close()
	return ret



def is_exist_with_upd_zero(accessor, program_id, race_no, horse_id):

	y = int(program_id/1000000)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template = """
		select 
			count(*) 
		from 
			{0} 
		where 
			rr_r_id={1} 
		and
			rr_r_race={2} 
		and 
			rr_r_horse_id={3} 
		and 
			upd=0
		"""
	cmd = template.format(
		mdb,
		program_id, 
		race_no, 
		horse_id
		)
	accessor.execute(cmd)
	ret = False
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		if(0 != ret):
			ret = True
		break
	accessor.cur_close()

	return ret

#統計用データを返す
def get_statistics_data(accessor):
   
	template = """
			   select 
					rr_r_deviation,
					rr_r_deviation3f,
					rr_r_win_ratio,
					rr_r_mul_ratio,
					rr_r_arg_dev,
					rr_r_arg_3fd,
					rr_r_tr_score,
					rr_r_jk_score,
					rr_r_sire_win_score,
					rr_r_sire_mul_score,
					rr_r_straight_dev,
					rr_r_l_corner_dev,
					rr_r_corner_dev,
					rr_r_turf_dev,
					rr_r_dirt_dev,
					rr_r_avg_time_diff
				from 
				 {0}
				"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	#read_sql にしない
	ret = accessor.read_sql_to_df(cmd)
	return ret



#外れ値データ取得
def get_outer_records(accessor, y):
	template = """
		select
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
			(  
			{2}.rr_r_deviation <= -100  or  100 <=  {2}.rr_r_deviation
			or
			{2}.rr_r_deviation3f <= -100  or  100 <= {2}.rr_r_deviation3f
			or
			{2}.rr_r_arg_dev <= -100  or  100 <= {2}.rr_r_arg_dev
			or
			{2}.rr_r_arg_3fd <= -100  or  100 <=  {2}.rr_r_arg_3fd
			or
			{2}.rr_r_straight_dev <= -100  or  100 <= {2}.rr_r_straight_dev
			or
			{2}.rr_r_l_corner_dev <= -100  or  100 <= {2}.rr_r_l_corner_dev
			or
			{2}.rr_r_r_corner_dev <= -100  or  100 <= {2}.rr_r_r_corner_dev
			or
			{2}.rr_r_turf_dev <= -100  or  100 <= {2}.rr_r_turf_dev
			or
			{2}.rr_r_dirt_dev <= -100  or  100 <= {2}.rr_r_dirt_dev	  
			)
			order by 
				{0}.ph_id desc
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		mdb
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret  


def get_jockey_list_to_df(accessor):
	template = """
		select 
			distinct(rr_r_jockey) 
		from 
			{0} 
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_jocky_and_id_to_df(accessor):
	template = """
		select 
			rr_r_id,
			rr_r_horse_id,
			rr_r_j_id

		from 
			{0} 
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  
	 


#レース成績の着順を返す。
def get_rank_by_ir(accessor, id, race):
	y = id[:4]
	template ="""
		select 
			rr_r_horse_id, rr_r_rank
		from 
			{0} 
		where 
				rr_r_id='{1}' 
			and 
				rr_r_race='{2}'
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
			mdb, 
			id, 
			race
			)
	ret = accessor.read_sql_to_df(cmd)
	return ret



def is_upd2(accessor, program_id, horse_id):
	try:
		rr_r_id =program_id
		y = int(rr_r_id[:4])
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		template = """
			select 
				count(*) 
			from 
				{0} 
			where 
				{0}.rr_r_id='{1}'
				and 
				{0}.rr_r_horse_id='{2}'
				and
				{0}.upd=0
			"""
		cmd = template.format(
			mdb, 
			program_id,
			horse_id)
		accessor.execute(cmd)
		ret = False
		for c in accessor.cur.fetchall():
			ret = int(c[0])
			if(0 != ret):
				ret = True
			break
		accessor.cur_close()
	except Exception as e: 
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret


#指定レースの馬情報が存在するかを返す
def get_race_horse_count(accessor, program_id, race):
	y = program_id[:4]
	template ="""
		select 
			count(*)
		from 
			{0} 
		where 
				rr_r_id='{1}' 
			and 
				rr_r_race='{2}'
		"""
	ret = 0
	if(2000 <= int(y)):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		cmd = template.format(
				mdb, 
				program_id, 
				race
				)
		accessor.execute(cmd)
		
		for c in accessor.cur.fetchall():
			ret = int(c[0])
			
			break
		accessor.cur_close()
	return ret


#指定レースの馬情報が存在するかを返す
def get_rank_zero_count(accessor, y):
	template ="""
		select 
			count(*)
		from 
			{0} 
		where 
				rr_r_rank='00' 
		"""
	ret = 0
	if(2000 <= int(y)):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		cmd = template.format(
				mdb
				)
		accessor.execute(cmd)
		
		for c in accessor.cur.fetchall():
			ret = int(c[0])
			if(0 != ret):
				ret = True
			break
		accessor.cur_close()
	return ret


#指定年のレース成績を返す。
def get_horse_id_result_by_ir(accessor, program_id, race):
	y = program_id[:4]
	template ="""
		select 
			rr_r_horse_id, rr_r_rank
		from 
			{0} 
		where 
				rr_r_id='{1}' 
			and 
				rr_r_race='{2}'
			and 
				rr_r_rank<>'00'
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
			mdb, 
			program_id, 
			race)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_horse_id_result_by_ir2(accessor, program_id, race):
	y = program_id[:4]
	template ="""
		select 
			rr_r_horse_id, rr_r_rank
		from 
			{0} 
		where 
				rr_r_id='{1}' 
			and 
				rr_r_race='{2}'
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
			mdb, 
			program_id, 
			race)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_sire_result_by_iste_still_id_to_df(accessor, program_id, sire_id, bpd_code):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	ret = pd.DataFrame()
	if(1999 < y2):
		template =  """
			select 
				CLng({2}.rr_r_rank) as rank
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					CLng({0}.ph_year+{0}.ph_monthday) < {3}
				and
					{1}.rh_te_bpd_code ='{4}'
				and
					{2}.rr_m_blood01 ='{5}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id desc
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			program_id[:8],
			bpd_code,
			sire_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_sire_result_by_iste_all_to_df(accessor, program_id, sire_id, bpd_code):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(int(y)-1)
	ret = pd.DataFrame()
	if(2000 < y2):
		template =  """
			select 
				CLng({2}.rr_r_rank) as rank
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					{1}.rh_te_bpd_code ='{3}'
				and
					{2}.rr_m_blood01 ='{4}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id desc
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			bpd_code,
			sire_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		ret = accessor.read_sql_to_df(cmd)   
	return ret

	
def get_jocky_result_by_iste_still_id_to_df(accessor, program_id, jocky_id, bpd_code):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	ret = pd.DataFrame()
	if(1999 < y2):
		template =  """
			select 
				CLng({2}.rr_r_rank) as rank
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					CLng({0}.ph_year+{0}.ph_monthday) < {3}
				and
					{1}.rh_te_bpd_code ='{4}'
				and
					{2}.rr_r_j_id ='{5}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id desc
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			program_id[:8],
			bpd_code,
			jocky_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_jocky_result_by_iste_all_to_df(accessor, program_id, jocky_id, bpd_code):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(int(y)-1)
	ret = pd.DataFrame()
	if(2000 < y2):
		template =  """
			select 
				CLng({2}.rr_r_rank) as rank
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					{1}.rh_te_bpd_code ='{3}'
				and
					{2}.rr_r_j_id ='{4}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id desc
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			bpd_code,
			jocky_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		ret = accessor.read_sql_to_df(cmd)   
	return ret


	
def get_trainer_result_by_iste_still_id_to_df(accessor, program_id, jocky_id, bpd_code):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	ret = pd.DataFrame()
	if(1999 < y2):
		template =  """
			select 
				CLng({2}.rr_r_rank) as rank
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					CLng({0}.ph_year+{0}.ph_monthday) < {3}
				and
					{1}.rh_te_bpd_code ='{4}'
				and
					{2}.rr_r_t_id ='{5}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id desc
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			program_id[:8],
			bpd_code,
			jocky_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_trainer_result_by_iste_all_to_df(accessor, program_id, jocky_id, bpd_code):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(int(y)-1)
	ret = pd.DataFrame()
	if(2000 < y2):
		template =  """
			select 
				CLng({2}.rr_r_rank) as rank
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					{1}.rh_te_bpd_code ='{3}'
				and
					{2}.rr_r_t_id ='{4}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id desc
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			bpd_code,
			jocky_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_race_result_by_hni_with_wild_card(accessor, program_id, horse_name):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	ret = pd.DataFrame()
	if(1999 < y2):	
		template =  """
			select 
				{0}.rr_r_id, {0}.rr_r_horse_id, {0}.rr_r_horse_name
			from {0}
			where  
				{0}.rr_r_id like '{1}__'
				and
				{0}.rr_r_horse_name='{2}'
		"""
		cmd = template.format(
			mdb, 
			program_id,
			horse_name
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )			
		ret = accessor.read_sql_to_df(cmd)   
		return ret



def get_feets_to_sr(accessor, program_id, horse_id):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template ="""
		select 
			{0}.rr_m_feet1, {0}.rr_m_feet2, {0}.rr_m_feet3, {0}.rr_m_feet4
		from 
			{0} 
		where
			{0}.rr_r_id = '{1}'
			and 
			{0}.rr_r_horse_id='{2}'
		"""
	cmd = template.format(
			mdb,
			program_id, 
			horse_id)
	accessor.execute(cmd)
	ret = None
	temp = accessor.read_sql_to_df(cmd)
	if(0 != len(temp)):
		ret = temp.iloc[0]
	return ret 


def get_burden_to_sr(accessor, program_id, horse_id):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template ="""
		select 
			{0}.rr_r_burden
		from 
			{0} 
		where
			{0}.rr_r_id = '{1}'
			and 
			{0}.rr_r_horse_id='{2}'
		"""
	cmd = template.format(
			mdb,
			program_id, 
			horse_id)
	accessor.execute(cmd)
	ret = None
	temp = accessor.read_sql_to_df(cmd)
	if(0 != len(temp)):
		ret = temp.iloc[0]
	return ret 


def get_odds_to_sr(accessor, program_id, horse_id):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template ="""
		select 
			{0}.rr_r_odds
		from 
			{0} 
		where
			{0}.rr_r_id = '{1}'
			and 
			{0}.rr_r_horse_id='{2}'
		"""
	cmd = template.format(
			mdb,
			program_id, 
			horse_id)
	accessor.execute(cmd)
	ret = None
	temp = accessor.read_sql_to_df(cmd)
	if(0 != len(temp)):
		ret = temp.iloc[0]
	return ret 


#指定IDの馬を返す
def get_latest_program_id(accessor, y, horse_id):
	ret = ''
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template =  """
		select 
			top 1 {0}.rr_r_id
		from	   
			{0}
		where  
			{0}.rr_r_horse_id = '{1}'
		order by 
			{0}.rr_r_id desc
	"""
	cmd = template.format(
		mdb,
		horse_id
		)
	
	df_temp = accessor.read_sql_to_df(cmd)   
	if(0 != len(df_temp)):
		ret = str(df_temp.iloc[0]['rr_r_id'])	
	return ret



def get_horse_result_by_hid(accessor, program_id, horse_id):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template ="""
		select 
			{0}.*
		from 
			{0} 
		where
			{0}.rr_r_id = '{1}'
			and 
			{0}.rr_r_horse_id='{2}'
		"""
	cmd = template.format(
			mdb,
			program_id, 
			horse_id)
	accessor.execute(cmd)
	ret = None
	temp = accessor.read_sql_to_df(cmd)
	if(0 != len(temp)):
		ret = temp.iloc[0]
	return ret 


def get_horse_by_yir_to_df(accessor, program_id, race_no):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)	   
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_id='{3}'
			and
			{1}.rh_race='{4}'

		)
		order by 
 			{0}.ph_id desc
	"""
 			# and
			# {2}.rr_r_rank='00'
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		mdb,
		program_id,
		race_no
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_time_diff_to_sr(accessor, program_id, horse_id):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template ="""
		select 
			{0}.rr_r_time_diff
		from 
			{0} 
		where
			{0}.rr_r_id = '{1}'
			and 
			{0}.rr_r_horse_id='{2}'
		"""
	cmd = template.format(
			mdb,
			program_id, 
			horse_id)
	accessor.execute(cmd)
	ret = None
	temp = accessor.read_sql_to_df(cmd)
	if(0 != len(temp)):
		ret = temp.iloc[0]
	return ret 

	
def get_weight_to_sr(accessor, program_id, horse_id):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template ="""
		select 
			{0}.rr_r_weight
		from 
			{0} 
		where
			{0}.rr_r_id = '{1}'
			and 
			{0}.rr_r_horse_id='{2}'
		"""
	cmd = template.format(
			mdb,
			program_id, 
			horse_id)
	accessor.execute(cmd)
	ret = None
	temp = accessor.read_sql_to_df(cmd)
	if(0 != len(temp)):
		ret = temp.iloc[0]
	return ret 

def get_odds_to_df(accessor):
	template = """
		select 
			{0}.rr_r_id, {0}.rr_r_horse_id, {0}.rr_r_odds 
		from 
			{0} 
		order by rr_r_id desc
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  
	
def get_timediff_to_df(accessor):
	template = """
		select
			{0}.rr_r_id, {0}.rr_r_horse_id, {0}.rr_r_time_diff
		from 
			{0} 
		order by rr_r_id desc
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def get_odds_to_df2(accessor, program_id, horse_id):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	template = """
		select 
			 {0}.rr_r_odds 
		from 
			{0} 
		where 
			{0}.rr_r_id='{1}'
			and
			{0}.rr_r_horse_id='{2}'
		order by rr_r_id desc
		"""
	cmd = template.format(
		mdb,
		program_id,
		horse_id
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  
	
	
def get_vote_to_df(accessor):
	template = """
		select 
			{0}.rr_r_id, {0}.rr_r_horse_id, {0}.rr_r_vote
		from 
			{0} 
		order by rr_r_id desc
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def is_upd(accessor, program_id, race_no):
	y = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	ret = False
	template = """
		select 
			count(*)
		from 
			{0} 
		where 
				{0}.rh_id='{1}'
			and 
				{0}.rh_race ='{2}'
			and
				{0}.rh_upd=5
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		program_id,
		race_no
		)
	accessor.execute(cmd)
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		if(0 != ret):
			ret = True
		break
	accessor.cur_close()
	return ret

	
def get_records_upd_not_5_to_df(accessor):
	template = """
		select 
		    rr_r_id,
			rr_r_horse_id
		from 
			{0} 
		where
			upd<>5
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  



def get_records_pid_hid_to_df(accessor):
	template = """
		select
		    rr_r_id,
			rr_r_horse_id
		from 
			{0} 
		"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT
		)
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

def is_blood01_null(accessor, program_id, horse_id):
	y = program_id[:4]
	y2 = int(y)
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	ret = pd.DataFrame()
	if(1999 < y2):
		template =  """
			select 
				count(*)
			from {0}	   

			where  
			(  
					{0}.rr_r_id='{1}'
				and
					{0}.rr_r_horse_id ='{2}'

				and 
					{0}.rr_m_blood01 is null
			)
		"""

		cmd = template.format(
			mdb,
			program_id,
			horse_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		accessor.execute(cmd)
		ret = False
		for c in accessor.cur.fetchall():
			ret = int(c[0])
			if(0 != ret):
				ret = True
			break
		accessor.cur_close()

	return ret

def get_records_null_horse_name_to_df(accessor, y):
	template = """
		select 
			* 
		from 
			{0} 
		where
			{0}.rr_r_horse_name is null
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		mdb
		)
	
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  

#データを取得
def get_horse_id_y_to_list(accessor, y):
	ret = []
	template = """
		select
			distinct({0}.rr_r_horse_id) as horse_id
		from	   
			{0}
		where
			{0}.rr_r_horse_id<>'0000000000'
		"""
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
	cmd = template.format(
		mdb
		)
	
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp['horse_id'].to_list()
	return ret  

def get_bloods_to_sr(accessor, y, horse_id):

	ret = pd.Series()
	if(1999 < y):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		template =  """
			select 
				{0}.rr_r_id,
				{0}.rr_r_horse_id,
				{0}.rr_m_blood01,
				{0}.rr_m_blood02,
				{0}.rr_m_blood03,
				{0}.rr_m_blood04,
				{0}.rr_m_blood05,
				{0}.rr_m_blood06,
				{0}.rr_m_blood07,
				{0}.rr_m_blood08,
				{0}.rr_m_blood09,
				{0}.rr_m_blood10,
				{0}.rr_m_blood11,
				{0}.rr_m_blood12,
				{0}.rr_m_blood13,
				{0}.rr_m_blood14
			from {0}	   
			where  
				{0}.rr_r_horse_id='{1}'

		"""

		cmd = template.format(
			mdb,
			horse_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		df_temp = accessor.read_sql_to_df(cmd)
		if(len(df_temp)):
			ret = df_temp.iloc[0]
	return ret


def get_horse_rank_still_by_ph(accessor, program_id, horse_id, ad_year=2000):
	year = int(program_id[:4])  
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,ad_year-1, -1):
		#print(f'{y} start')
		if(1999 < y):
			mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
			template =  """
				select 
					rr_r_id, rr_r_rank
				from	   
					{0}
				where  
				(  
						CLng(Left({0}.rr_r_id, 8)) < {1}
					and
						{0}.rr_r_horse_id ='{2}'
					and
						{0}.rr_r_rank <> '00'
				)
			
			"""
				# order by 
				# 	{0}.ph_id desc
			cmd = template.format(
				mdb,
				program_id[:8],
				horse_id
				)
			cmd = cmd.replace( '\n' , ' ' )
			cmd = cmd.replace( '\t' , ' ' )	 
			df_temp = accessor.read_sql_to_df(cmd) 
			if(len(df_temp)):
				temp_list.append(df_temp)
			time.sleep(0.2)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)

	if (len(ret)):
		ret = ret.sort_values('rr_r_id', ascending=False)
	return ret


def get_horse_full_rank_by_ph(accessor, program_id, horse_id, ad_year=2000):
	year = int(program_id[:4])  
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(2024,ad_year, -1):
		#print(f'{y} start')
		if(1999 < y):
			mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
			template =  """
				select 
					rr_r_id, rr_r_rank
				from	   
					{0}
				where  
				(  
						CLng(Left({0}.rr_r_id, 4)) <= {1}
					and
						{0}.rr_r_horse_id ='{2}'
					and
						{0}.rr_r_rank <> '00'
				)
				order by rr_r_id
			"""
				# order by 
				# 	{0}.ph_id desc
			cmd = template.format(
				mdb,
				program_id[:4],
				horse_id
				)
			cmd = cmd.replace( '\n' , ' ' )
			cmd = cmd.replace( '\t' , ' ' )	 
			df_temp = accessor.read_sql_to_df(cmd) 
			if(len(df_temp)):
				temp_list.append(df_temp)
			time.sleep(0.2)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)

	if (len(ret)):
		ret = ret.sort_values('rr_r_id', ascending=False)
	return ret


def get_sire_mare_pair_to_df(accessor, layer):
	target_sire = ''
	target_mare = ''
	if(layer ==1):
		target_sire = 'rr_m_blood01'
		target_mare = 'rr_m_blood02'
	elif(layer ==2):
		target_sire = 'rr_m_blood03'
		target_mare = 'rr_m_blood04'		
	elif(layer ==3):
		target_sire = 'rr_m_blood05'
		target_mare = 'rr_m_blood06'	
	elif(layer ==4):
		target_sire = 'rr_m_blood07'
		target_mare = 'rr_m_blood08'	
	elif(layer ==5):
		target_sire = 'rr_m_blood09'
		target_mare = 'rr_m_blood10'	
	elif(layer ==6):
		target_sire = 'rr_m_blood11'
		target_mare = 'rr_m_blood12'	
	elif(layer ==7):
		target_sire = 'rr_m_blood13'
		target_mare = 'rr_m_blood14'	

	template = """
		select 
			distinct {0}.{1}, {0}.{2}
		from 
			{0}

		"""
	mdb = const.VIEW_KJDB_RACE_RESULT
	cmd = template.format(
		mdb,
		target_sire,
		target_mare
		)
	
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  



def get_parent_to_df(accessor, layer):
	target_parent = ''
	if(layer ==1):
		target_parent = 'rr_m_blood01'
	elif(layer ==2):
		target_parent = 'rr_m_blood02'	
	elif(layer ==3):
		target_parent = 'rr_m_blood03'
	elif(layer ==4):
		target_parent = 'rr_m_blood04'	
	elif(layer ==5):
		target_parent = 'rr_m_blood05'	
	elif(layer ==6):
		target_parent = 'rr_m_blood06'	
	elif(layer ==7):
		target_parent = 'rr_m_blood07'	
	elif(layer ==8):
		target_parent = 'rr_m_blood08'
	elif(layer ==9):
		target_parent = 'rr_m_blood09'		
	elif(layer ==10):
		target_parent = 'rr_m_blood10'	
	elif(layer ==11):
		target_parent = 'rr_m_blood11'	
	elif(layer ==12):
		target_parent = 'rr_m_blood12'	
	elif(layer ==13):
		target_parent = 'rr_m_blood13'	
	elif(layer ==14):
		target_parent = 'rr_m_blood14'
	template = """
		select 
			distinct {0}.{1}
		from 
			{0}

		"""
	mdb = const.VIEW_KJDB_RACE_RESULT
	cmd = template.format(
		mdb,
		target_parent,
		)
	
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  



def get_parent_child_to_df(accessor, layer):
	target_parent = ''
	target_child = ''
	if(layer ==1):
		target_parent ,target_child= 'rr_m_blood01','rr_r_horse_id'
	elif(layer ==2):
		target_parent ,target_child= 'rr_m_blood02','rr_r_horse_id'
	elif(layer ==3):
		target_parent ,target_child= 'rr_m_blood03','rr_m_blood01'
	elif(layer ==4):
		target_parent ,target_child= 'rr_m_blood04','rr_m_blood01'
	elif(layer ==5):
		target_parent ,target_child= 'rr_m_blood05','rr_m_blood02'
	elif(layer ==6):
		target_parent ,target_child= 'rr_m_blood06','rr_m_blood02'
	elif(layer ==7):
		target_parent ,target_child= 'rr_m_blood07','rr_m_blood03'
	elif(layer ==8):
		target_parent ,target_child= 'rr_m_blood08','rr_m_blood03'
	elif(layer ==9):
		target_parent ,target_child= 'rr_m_blood09','rr_m_blood04'
	elif(layer ==10):
		target_parent ,target_child= 'rr_m_blood10','rr_m_blood04'
	elif(layer ==11):
		target_parent ,target_child= 'rr_m_blood11','rr_m_blood05'
	elif(layer ==12):
		target_parent ,target_child= 'rr_m_blood12','rr_m_blood05'
	elif(layer ==13):
		target_parent ,target_child= 'rr_m_blood13','rr_m_blood06'
	elif(layer ==14):
		target_parent ,target_child= 'rr_m_blood14','rr_m_blood06'
	template = """
		select 
			distinct {1}, {2}
		from 
			{0}

		"""
	mdb = const.VIEW_KJDB_RACE_RESULT
	cmd = template.format(
		mdb,
		target_parent,
		target_child
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	 	
	accessor.execute(cmd)
	ret = accessor.read_sql_to_df(cmd)
	return ret  


