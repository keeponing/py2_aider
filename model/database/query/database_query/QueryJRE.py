import pyodbc
import model.conf.KJraConst as const
import pandas as pd
import time
import datetime

#指定IDの馬を返す
def get_race_evidence_one_by_ih_to_df(accessor, program_id, horse_id):
	year = program_id[:4]
	ret = pd.DataFrame()
	if(0!= year):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(year)
		template =  """
			select 
				{0}.*, {1}.*, {2}.*
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			( 
					{2}.rr_r_id='{3}'
				and
					{2}.rr_r_horse_id = '{4}'
			)
			order by 
				{0}.ph_id desc
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			program_id,
			horse_id
			)
		
		ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_race_evidence_one_by_h_to_df(accessor, horse_id, is_active =False):
	today1 = datetime.datetime.now()
	year = today1.year   
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,1999, -1):	
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
					{2}.rr_r_horse_id ='{3}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			horse_id
			)
		
		df_temp = accessor.read_sql_to_df(cmd) 
		temp_list.append(df_temp)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)

	if (len(ret)):
		ret = ret.sort_values('ph_id')
	return ret

def get_race_evidence_greater_than(accessor, oldest_year):
	   
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_rank <> '00'
			and 
				'{3}' <= {0}.ph_year
		)
		order by 
 			{0}.ph_id
	"""

	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		oldest_year
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_race_evidence_one_by_h_to_df2(accessor, horse_id, is_active =False):
	today1 = datetime.datetime.now()
	year = today1.year   
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,1999, -1):

		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)	   
		template =  """
			select 
				{0}.ph_id, {0}.ph_year, {1}.rh_race, {1}.rh_te_c2_code, {2}.rr_r_horse_id, {2}.rr_r_rank, CLng({2}.rr_r_rank) as rank
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					{2}.rr_r_horse_id ='{3}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			horse_id
			)
		
		df_temp = accessor.read_sql_to_df(cmd) 
		temp_list.append(df_temp)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)
	if (len(ret)):
		ret = ret.sort_values('ph_id')
	return ret


def get_race_evidence_one_by_h_to_df3(accessor, horse_id):
	today1 = datetime.datetime.now()
	year = today1.year   
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,1999, -1):

		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
		template =  """
			select 
				{0}.*,{1}.*,{2}.*
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					{2}.rr_r_horse_id ='{3}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			horse_id
			)
		
		df_temp = accessor.read_sql_to_df(cmd) 
		temp_list.append(df_temp)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)
	if (len(ret)):
		ret = ret.sort_values('ph_id')
	return ret

#指定IDの馬を返す
def get_latest_horse_result_to_sr(accessor, horse_id):
	ret = pd.DataFrame()

	template =  """
		select 
			top 1 {0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		( 
			{2}.rr_r_horse_id = '{3}'
		)
		order by 
			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		horse_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	if(0 != len(ret)):
		ret = ret.iloc[0]	
	return ret

def get_result_by_y(accessor, year):
	ret = pd.DataFrame()
	if(0!= year):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(year)
		template =  """
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
				{0}.ph_id
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			year
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )			
		ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_result_by_p(accessor, place):
	today1 = datetime.datetime.now()
	year = today1.year   
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,1999, -1):		
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
					{0}.ph_place='{3}'
			)
			order by 
				{0}.ph_id desc
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			place
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )			
		df_temp = accessor.read_sql_to_df(cmd)  
		temp_list.append(df_temp)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True) 
	return ret


def get_result_by_hi_to_df(accessor, horse_id):
	   
	template =  """
		select 
			{0}.ph_year, {0}.ph_monthday, {0}.ph_place, {1}.rh_race, {1}.rh_te_bpds_code, CLng({0}.ph_year) as y, CLng({0}.ph_monthday) as md, CLng({2}.rr_r_rank) as rank
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_horse_id ='{3}'
			and
				{2}.rr_r_rank <> '00'
		)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		horse_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_result_by_hi_to_df2(accessor, horse_id):
	   
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_horse_id ='{3}'
		)
		order by 
 			{0}.ph_id desc
	"""

	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		horse_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_result_by_hi_to_df_asc(accessor, horse_id):
	   
	template =  """
		select 
			{0}.ph_year, {0}.ph_monthday, {0}.ph_place, {1}.rh_race, {1}.rh_te_bpds_code, CLng({0}.ph_year) as y, CLng({0}.ph_monthday) as md, CLng({2}.rr_r_rank) as rank
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_horse_id ='{3}'
			and
				{2}.rr_r_rank <> '00'
		)
		order by 
 			{0}.ph_id
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		horse_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_result_over_y_to_df(accessor, y):
	   
	template =  """
		select 
			{0}.ph_year, {0}.ph_monthday, {0}.ph_place, {1}.rh_race, {1}.rh_te_bpds_code, {2}.rr_r_horse_id, 
			CLng({0}.ph_year) as y, CLng({0}.ph_monthday) as md, CLng({2}.rr_r_rank) as rank
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{3} < CLng({0}.ph_year)
				and 
				{3}+12 > CLng({0}.ph_year)
				and
				{2}.rr_r_rank <> '00'
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


def get_result_by_ite_still_id_to_df(accessor, program_id, horse_id, ad_year=2000):
	year = int(program_id[:4])  
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,ad_year-1, -1):
		#print(f'{y} start')
		if(1999 < y):
			mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)
			template =  """
				select 
					*, CLng({2}.rr_r_rank) as rank, {1}.rh_te_bpd_code, {1}.rh_te_bd_code, {1}.rh_te_c_code, {1}.rh_te_bpds_code
				from	   
					(({1} inner join
					{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
					{0} on {2}.rr_r_id = {0}.ph_id)
				where  
				(  
						CLng({0}.ph_year+{0}.ph_monthday) < {3}
					and
						{2}.rr_r_horse_id ='{4}'
					and
						{2}.rr_r_rank <> '00'
				)
			
			"""
				# order by 
				# 	{0}.ph_id desc
			cmd = template.format(
				const.TBL_KJDB_PROGRAM_HEADER, 
				const.TBL_KJDB_RACE_HEADER, 
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
		ret = ret.sort_values('ph_id', ascending=False)
	return ret



# def get_result_by_ite_still_id_to_df2(accessor, program_id, horse_id, is_active =False):
	   
# 	template =  """
# 		select 
# 			*, CLng({2}.rr_r_rank) as rank
# 		from	   
# 			(({1} inner join
# 			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
# 			{0} on {2}.rr_r_id = {0}.ph_id)
# 		where  
# 		(  
# 				CLng({0}.ph_year+{0}.ph_monthday) < {3}
# 			and
# 				{2}.rr_r_horse_id ='{4}'
# 			and
# 				{2}.rr_r_rank <> '00'
# 		)
# 		order by 
#  			{0}.ph_id desc
# 	"""
# 	view = const.VIEW_KJDB_RACE_RESULT_ACTIVE if(True == is_active) else const.VIEW_KJDB_RACE_RESULT
# 	cmd = template.format(
# 		const.TBL_KJDB_PROGRAM_HEADER, 
# 		const.TBL_KJDB_RACE_HEADER, 
# 		view,
# 		program_id[:8],
# 		horse_id
# 		)
# 	cmd = cmd.replace( '\n' , ' ' )
# 	cmd = cmd.replace( '\t' , ' ' )	
# 	ret = accessor.read_sql_to_df(cmd)   
# 	return ret


def get_result_by_ite_still_id_to_df3(accessor, program_id, horse_id, oldest_year=""):
	   
	template =  """
		select 
			*, CLng({2}.rr_r_rank) as rank, {1}.rh_te_bpd_code, {1}.rh_te_bd_code, {1}.rh_te_c_code, {1}.rh_te_bpds_code
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				CLng({0}.ph_year+{0}.ph_monthday) < {3}
			and
				{2}.rr_r_horse_id ='{4}'
			and
				{2}.rr_r_rank <> '00'
			and
				'{5}' <= {0}.ph_year
		)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id[:8],
		horse_id,
		oldest_year

		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_rank_and_distance_still_ih_to_df(accessor, program_id, horse_id, ad_year =2000):
	today1 = datetime.datetime.now()
	year = today1.year   
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,ad_year-1, -1):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y) 
		template =  """
			select 
				{0}.ph_id, {2}.rr_r_rank, {1}.rh_distance
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					CLng({0}.ph_year+{0}.ph_monthday) < {3}
				and
					{2}.rr_r_horse_id ='{4}'
				and
					{2}.rr_r_rank <> '00'
			)

		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			program_id[:8],
			horse_id
			)
		df_temp = accessor.read_sql_to_df(cmd) 
		temp_list.append(df_temp)
		time.sleep(0.2)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)

	if (len(ret)):
		ret = ret.sort_values('ph_id', ascending=False)
	return ret
	
def get_rank_and_distance_still_id_to_df2(accessor, program_id, horse_id, oldest_year ='2000'):
 
	template =  """
		select 
			 {2}.rr_r_rank, {1}.rh_distance
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				CLng({0}.ph_year+{0}.ph_monthday) < {3}
			and
				{2}.rr_r_horse_id ='{4}'
			and
				{2}.rr_r_rank <> '00'
			and
				'{5}' <= {0}.ph_year
		)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id[:8],
		horse_id,
		oldest_year
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_rank_mean_by_bpd_still_id(accessor, program_id, horse_id, te_code):
	   
	template =  """
		select 
			 CLng({1}.rr_r_rank) as rank
		from	   
			{0} inner join
			{1} on {0}.rh_id = {1}.rr_r_id and {0}.rh_race = {1}.rr_r_race
		where  
		(  
				CLng(Mid({0}.rh_id,1,8)) < {2}
			and
				{1}.rr_r_horse_id ='{3}'
			and
				{0}.rh_te_bpd_code ='{4}'
			and
				{1}.rr_r_rank <> '00'
		)
		order by 
 			{0}.rh_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id[:8],
		horse_id,
  		te_code
		)
	
	df_temp = accessor.read_sql_to_df(cmd)  
	ret =.0 
	if(len(df_temp)):
		max_count =const.MAX_HORSE_COUNT 
		temp = df_temp['rank'].mean()
		temp = temp if(temp!=0) else max_count
		ret = (max_count - temp) /max_count
	return ret


def get_rank_mean_by_bd_still_id(accessor, program_id, horse_id, te_code):
	   
	template =  """
		select 
			 CLng({1}.rr_r_rank) as rank
		from	   
			{0} inner join
			{1} on {0}.rh_id = {1}.rr_r_id and {0}.rh_race = {1}.rr_r_race
		where  
		(  
				CLng(Mid({0}.rh_id,1,8)) < {2}
			and
				{1}.rr_r_horse_id ='{3}'
			and
				{0}.rh_te_bd_code ='{4}'
			and
				{1}.rr_r_rank <> '00'
		)
		order by 
 			{0}.rh_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id[:8],
		horse_id,
  		te_code
		)
	
	df_temp = accessor.read_sql_to_df(cmd)  
	ret =.0 
	if(len(df_temp)):
		max_count =const.MAX_HORSE_COUNT 
		temp = df_temp['rank'].mean()
		temp = temp if(temp!=0) else max_count
		ret = (max_count - temp) /max_count
	return ret

def get_rank_mean_by_c_still_id(accessor, program_id, horse_id, te_code):
	   
	template =  """
		select 
			 CLng({1}.rr_r_rank) as rank
		from	   
			{0} inner join
			{1} on {0}.rh_id = {1}.rr_r_id and {0}.rh_race = {1}.rr_r_race
		where  
		(  
				CLng(Mid({0}.rh_id,1,8)) < {2}
			and
				{1}.rr_r_horse_id ='{3}'
			and
				{0}.rh_te_c_code ='{4}'
			and
				{1}.rr_r_rank <> '00'
		)
		order by 
 			{0}.rh_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id[:8],
		horse_id,
  		te_code
		)
	
	df_temp = accessor.read_sql_to_df(cmd)  
	ret =.0 
	if(len(df_temp)):
		max_count =const.MAX_HORSE_COUNT 
		temp = df_temp['rank'].mean()
		temp = temp if(temp!=0) else max_count
		ret = (max_count - temp) /max_count
	return ret

#指定idの前レース成績を返す。
def get_prev_race_results_by_ihi_to_df(accessor, program_id, horse_id, ad_year=2000):
	today1 = datetime.datetime.now()
	year = today1.year   
	ret = pd.DataFrame()
	temp_list=[]
	for y in range(year,ad_year-1, -1):
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
					{2}.rr_r_horse_id = '{4}' 
				and 
					CLng({0}.ph_year+{0}.ph_monthday) < {3}
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
			horse_id
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		df_temp = accessor.read_sql_to_df(cmd)
		temp_list.append(df_temp)
		time.sleep(0.2)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)

	if (len(ret)):
		ret = ret.sort_values('ph_id', ascending=False)
	return ret


def get_all_result_to_df(accessor):
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_all_result_to_df2(accessor):
	template =  """
		select 
			{0}.ph_id, {0}.ph_year, {1}.rh_te_c2_code, {1}.rh_race, {2}.rr_r_horse_id, {2}.rr_r_rank
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_all_result_to_df3(accessor): 
	template =  """
		select 
			top 100 {0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_all_result_to_df4(accessor): 
	template =  """
		select 
			top 100 
			{0}.ph_id, {0}.ph_year,{0}.ph_monthday,{0}.ph_place,
			{1}.rh_race, 
			{2}.rr_r_horse_id, {2}.rr_r_horse_no,  {2}.rr_r_burden, {2}.rr_r_time_diff
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		order by 
 			{0}.ph_id
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_result_still_id_to_df(accessor, program_id, horse_id):
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where
			{2}.rr_r_horse_id ='{4}'
			and
			{2}.rr_r_id <'{3}'
			and
			{2}.rr_r_rank <> '00'
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_deviations_still_id_to_df(accessor, program_id, horse_id):
	template =  """
		select 
			{0}.*, {1}.rh_corner, {2}.rr_a_deviation, {2}.rr_a_deviation3f
		from
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where
			{2}.rr_r_horse_id ='{4}'
			and
			{2}.rr_r_id <'{3}'
			and
			{2}.rr_r_rank <> '00'
		order by 
 			{2}.rr_r_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_deviations_still_id_to_df2(accessor, program_id, horse_id, oldest_year):
	template =  """
		select 
			{0}.*, {1}.rh_corner, {2}.rr_a_deviation, {2}.rr_a_deviation3f
		from
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where
			{2}.rr_r_horse_id ='{4}'
			and
			{2}.rr_r_id <'{3}'
			and
			{2}.rr_r_rank <> '00'
			and
			'{5}' <= {0}.ph_year
		order by 
 			 {2}.rr_r_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id,
		oldest_year
		)
	
	ret = accessor.read_sql_to_df(cmd)
	return ret



def get_horse_by_id_to_df(accessor, program_id):
	   
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
		)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_horse_by_ir_to_df(accessor, program_id, race_no, ad_year=2000):
	ret = pd.DataFrame()
	y = int(program_id[:4])
	if(ad_year <= y):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)	   
		template =  """
			select 
				{0}.*, {1}.*, {2}.*
			from	   
				(({0} 
				INNER JOIN {1} 
					ON {0}.ph_id = {1}.rh_id) 
				INNER JOIN {2} 
					ON {1}.rh_id = {2}.rr_r_id
					AND {1}.rh_race = {2}.rr_r_race)
			where  
			(  
				{0}.ph_id='{3}'
				and
				{1}.rh_race='{4}'
			)
			order by 
				{0}.ph_id desc
		"""
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



def get_all_horses_active_duty_by_y_to_df(accessor, y, ad_year=2000):
	ret = pd.DataFrame()
	today1 = datetime.datetime.now()
	year = today1.year  
	temp_list=[]
	for y in range(year,ad_year-1, -1):	
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)	   
		template =  """
			select 
				{0}.*, {1}.*, {2}.*
			from	   
				(({0} 
				INNER JOIN {1} 
					ON {0}.ph_id = {1}.rh_id) 
				INNER JOIN {2} 
					ON {1}.rh_id = {2}.rr_r_id
					AND {1}.rh_race = {2}.rr_r_race)
			order by 
				{0}.ph_id desc
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		df_temp = accessor.read_sql_to_df(cmd)   
		temp_list.append(df_temp)
	if(len(temp_list)):
		ret = pd.concat(temp_list, ignore_index=True)

	if (len(ret)):
		ret = ret.sort_values('ph_id')
	return ret

def get_horse_by_ｙ_to_df(accessor, y):
	ret = pd.DataFrame()
	if(1999 < y):	 
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)  
		template =  """
			select 
				{0}.*, {1}.*, {2}.*
			from	   
				(({0} 
				INNER JOIN {1} 
					ON {0}.ph_id = {1}.rh_id) 
				INNER JOIN {2} 
					ON {1}.rh_id = {2}.rr_r_id
					AND {1}.rh_race = {2}.rr_r_race)
			where  
			(  
				{0}.ph_year='{3}'
			)
			order by 
				{0}.ph_id desc
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			y
			)
		cmd = cmd.replace( '\n' , ' ' )
		cmd = cmd.replace( '\t' , ' ' )	
		ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_horse_by_place_to_df(accessor, place):
	   
	template =  """
		select 
			 {0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_place='{3}'
		)
		order by 
 			{0}.ph_id  desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		place
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_prev_id_by_place_year_to_df(accessor, place, year):
	ret = pd.DataFrame()
	if(1999 < year):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(year)   
		template =  """
			select 
				{0}.*, {1}.*, {2}.*
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
				{0}.ph_place='{3}' 
				and 
				{0}.ph_year='{4}'
				and
				{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id 
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			place,
			year
			)
		
		ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_prev_id_by_year_to_df(accessor, year):
	   
	template =  """
		select 
			{0}.ph_id, 
			{2}.rr_r_horse_id, 
			{2}.rr_h_prev_id1, 
			{2}.rr_h_prev_id2, 
			{2}.rr_h_prev_id3, 
			{2}.rr_h_prev_id4
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_year='{3}'
			and
			{2}.rr_r_rank <> '00'
		)
		order by 
 			{0}.ph_id 
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		year
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret
def get_prev_id_by_place_class_year_to_df(accessor, place, year, cls_code):
	
	cc='000'
	if('01'==cls_code):
		cc='701'
	elif('02'==cls_code):
		cc='703'
	elif('03'==cls_code):
		cc='005'
	elif('04'==cls_code):
		cc='010'
	elif('05'==cls_code):
		cc='016'
	elif('06'==cls_code):
		cc='999'
		
	template =  """
		select 
			{0}.ph_id, 
			{1}.rh_race, 
			{2}.rr_r_horse_id, 
			{2}.rr_h_prev_id1, 
			{2}.rr_h_prev_id2, 
			{2}.rr_h_prev_id3, 
			{2}.rr_h_prev_id4, 
			{2}.rr_h_sc_prev_id1, 
			{2}.rr_h_sc_prev_id2, 
			{2}.rr_h_sc_prev_id3, 
			{2}.rr_h_sc_prev_id4,
			{2}.rr_r_rank
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_place='{3}' 
			and 
			{0}.ph_year='{4}'
			and
			(
					{1}.rh_class2='{5}'
				or
					{1}.rh_class3='{5}'
				or
					{1}.rh_class4='{5}'
				or
					{1}.rh_class5over='{5}'
				or
					{1}.rh_classYoung='{5}'
			)
			and
			{2}.rr_r_rank <> '00'
		)
		order by 
 			{0}.ph_id 
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		place,
		year,
		cc
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )		
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_prev_id_by_distance_class_year_to_df(accessor, dist, year, track_code):
	

	template =  """
		select 
			{0}.ph_id, 
			{1}.rh_race, 
			{2}.rr_r_horse_id, 
			{2}.rr_h_prev_id1, 
			{2}.rr_h_prev_id2, 
			{2}.rr_h_prev_id3, 
			{2}.rr_h_prev_id4, 
			{2}.rr_h_sc_prev_id1, 
			{2}.rr_h_sc_prev_id2, 
			{2}.rr_h_sc_prev_id3, 
			{2}.rr_h_sc_prev_id4,
			{2}.rr_r_rank
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{1}.rh_distance='{3}' 
			and 
			{0}.ph_year='{4}'
			and
			{1}.rh_track='{5}'
			and
			{2}.rr_r_rank <> '00'
		)
		order by 
 			{0}.ph_id 
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		dist,
		year,
		track_code
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )		
	ret = accessor.read_sql_to_df(cmd)   
	return ret
#指定idの前レース成績を返す。
def get_prev_race_evidence_by_ih_to_df(accessor, program_id, horse_id):
	
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
				{2}.rr_r_horse_id = '{3}'
			and
				{0}.ph_id < '{4}'
			and 
				{2}.rr_r_rank <> '00'
		order by 
			{0}.ph_id desc		 
	"""	
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		horse_id,
		program_id
		)

	df = accessor.read_sql_to_df(cmd)

  
	ret=[]
	ret.append(None)
	ret.append(None)
	ret.append(None)
	ret.append(None)
	cnt = 0
	for index2, r in df.iterrows():  
		if(cnt < len(ret)):
			ret[cnt]= r
			cnt =cnt+1
		else:
			break
	accessor.cur_close()

	return ret[0], ret[1], ret[2], ret[3]


def get_horse_by_id(accessor, program_id):
	   
	template =  """
		select 
			{0}.*, {1}.*, {2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_id={3}
		)
		order by 
 			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_horse_by_ir(accessor, program_id, race):
	
	
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
 			{2}.rr_r_horse_no
	"""
	year = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(year)   
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		mdb,
		program_id,
		race
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_horse_by_ir2(accessor, program_id, race):
	
	
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
			and
			{2}.rr_r_rank<>'00'
		)
		order by 
 			{2}.rr_r_horse_no
	"""
	year = program_id[:4]
	mdb = const.TBL_KJDB_RACE_RESULT_AT.format(year)   
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		mdb,
		program_id,
		race
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


#指定馬の出走平均距離を求める
def get_average_distance_by_ih(accessor, program_id, horse_id):
   
	template =  """
		select 
			avg({0}.rh_distance) as dist_avg
		from	   
			({0} inner join {1} on {0}.rh_id = {1}.rr_r_id and {0}.rh_race = {1}.rr_r_race)
		where  
			({1}.rr_r_horse_id = {3} and {1}.rr_r_id <= {2}) 
	"""   
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,  
		program_id,
		horse_id
		)

	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():	 
		ret = c.dist_avg
		break

	accessor.cur_close()
	return ret


#右周り偏差値
def get_right_corner_deviation(accessor, horse_id, program_id):
   
	template =  """
		select 
			avg({2}.rr_r_deviation)
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_horse_id = {4} 
			and 
			(
					int({2}.rr_r_id mod 100)=1 
				or 
					int({2}.rr_r_id mod 100)=2 
				or 
					int({2}.rr_r_id mod 100)=3 
				or 
					int({2}.rr_r_id mod 100)=6 
				or 
					int({2}.rr_r_id mod 100)=8 
				or 
					int({2}.rr_r_id mod 100)=9 
				or 
					int({2}.rr_r_id mod 100)=10
			)
			and 
				{2}.rr_r_id < {3}
		)
	   
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	
	accessor.execute(cmd)
	ret = .0
	for c in accessor.cur.fetchall():
		if(c[0] is not None):
			ret = float(c[0])
		break
	accessor.cur_close()
	
	return ret



#左周り偏差値
def get_left_corner_deviation(accessor, horse_id, program_id):
   
	template =  """
		 select 
			avg({2}.rr_r_deviation)
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_horse_id = {4} 
			and 
			(
					(int({2}.rr_r_id mod 100)=4 and {1}.rh_distance <> 1000) 
				or 
					int(rr_r_id mod 100)=5 
				or 
					int(rr_r_id mod 100)=7 
			)
			and 
				{2}.rr_r_id < {3}
		)
	   
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	
	accessor.execute(cmd)
	ret = .0
	for c in accessor.cur.fetchall():
		if(c[0] is not None):
			ret = float(c[0])
		break
	accessor.cur_close()
	
	return ret


#直線偏差値
def get_straight_deviation(accessor, horse_id, program_id):
   
	template =  """
		select 
			avg({2}.rr_r_deviation) 
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				rr_r_horse_id = {4} 
			and 
			(
					int({2}.rr_r_id mod 100)=4 
				and 
					{1}.rh_distance = 1000
			)
			and 
				{2}.rr_r_id < {3}
		)
	   
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	
	accessor.execute(cmd)
	ret = .0
	for c in accessor.cur.fetchall():
		if(c[0] is not None):
			ret = float(c[0])
		break
	accessor.cur_close()
	
	return ret


#ダート偏差値
def get_arg_deviation(accessor, horse_id, program_id):
   
	template =  """
		select 
			avg({2}.rr_r_deviation)
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_horse_id = {4} 
			and 
				{2}.rr_r_id <= {3}
		)
	   
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	
	accessor.execute(cmd)
	ret = .0
	for c in accessor.cur.fetchall():
		if(c[0] is not None):
			ret = float(c[0])
		break
	accessor.cur_close()
	
	return ret


#上がり3F平均偏差値
def get_arg_3fdeviation(accessor, horse_id, program_id):
   
	template =  """
		select 
			avg({2}.rr_r_deviation3f)
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{2}.rr_r_horse_id = {4} 
			and 
				{2}.rr_r_id <= {3}
		)
	   
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		program_id,
		horse_id
		)
	
	accessor.execute(cmd)
	ret = .0
	for c in accessor.cur.fetchall():
		if(c[0] is not None):
			ret = float(c[0])
		break
	accessor.cur_close()
	
	return ret

#指定IDの馬を返す
def get_prev_id_by_ihi_to_df(accessor, program_id, horse_id):
	year = program_id[:4]
	ret = pd.DataFrame()
	if(0!= year):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(year)
		template =  """
			select 
				Top 1 {0}.*, {1}.*, {2}.*
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			( 
					{2}.rr_r_id <'{3}'
				and
					{2}.rr_r_horse_id ='{4}'
			)
			order by 
				{0}.ph_id desc
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			const.VIEW_KJDB_RACE_RESULT,
			#mdb,
			program_id,
			horse_id
			)
		
		ret = accessor.read_sql_to_df(cmd)   
	return ret


#指定IDの馬を返す
def get_prev_id_by_ihi_to_df2(accessor, year, program_id, horse_id):
	ret = pd.DataFrame()
	if(0!= year):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(year)
		template =  """
			select 
				Top 1 {0}.*, {1}.*, {2}.*
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			( 
					{2}.rr_r_id <'{3}'
				and
					{2}.rr_r_horse_id ='{4}'
			)
			order by 
				{0}.ph_id desc
		"""
		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			#const.VIEW_KJDB_RACE_RESULT,
			mdb,
			program_id,
			horse_id
			)
		
		ret = accessor.read_sql_to_df(cmd)   
	return ret
def get_prev_id_by_cp_year_to_df(accessor, place, group, year ):
	   
	template =  """
		select 
			{0}.ph_id, 
			{2}.rr_r_horse_id, 
			{2}.rr_h_prev_id1, 
			{2}.rr_h_prev_id2, 
			{2}.rr_h_prev_id3, 
			{2}.rr_h_prev_id4
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
				{0}.ph_place='{3}' 
			and 
				{0}.ph_year='{4}'
			and 
				(
					{1}.rh_class2 ='{5}'
					or
					{1}.rh_class3 ='{5}'
					or
					{1}.rh_class4 ='{5}'
					or
					{1}.rh_class5over ='{5}'
					or
					{1}.rh_classYoung ='{5}'
				)
				
		)
		order by 
 			{0}.ph_id 
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		place,
		year,
		group
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

	

def get_all_program_id_and_horse_id_to_df(accessor):
	template ="""
		select
			 {0}.rr_r_id, 
			 {0}.rr_r_horse_id 
		from {0} 
		"""
	cmd = template.format(
			const.VIEW_KJDB_RACE_RESULT)
	accessor.execute(cmd)

	ret = accessor.read_sql_to_df(cmd)
	return ret 

def get_horse_id_by_upd(accessor, upd):
	   
	template =  """
		select 
			{0}.rr_r_horse_id
		from	   
			{0}
		where
			upd={1}
	"""
	cmd = template.format(
		const.VIEW_KJDB_RACE_RESULT,
		upd
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret

def get_race_condition_by_hi_id(accessor, horse_id):
	template =  """
		SELECT 
			{0}.rh_id, 
			{0}.rh_track, 
			{0}.rh_turf_condition, 
			{0}.rh_dirt_condition, 
			{0}.rh_distance, 
			{1}.rr_r_horse_id
		FROM 
			{1} 
			INNER JOIN {0} ON (
				{1}.rr_r_race = {0}.rh_race
			) 
			AND 
			(
				{1}.rr_r_id = {0}.rh_id
			)
		WHERE {1}.rr_r_horse_id='{2}'
		ORDER BY {0}.rh_id DESC
	"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		const.VIEW_KJDB_RACE_RESULT,
		horse_id
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_race_condition_to_df(accessor):
	template =  """
		SELECT 
			{0}.rh_id, 
			{0}.rh_track, 
			{0}.rh_turf_condition, 
			{0}.rh_dirt_condition, 
			{0}.rh_distance, 
			{1}.rr_r_horse_id
		FROM 
			{1} 
			INNER JOIN {0} ON (
				{1}.rr_r_race = {0}.rh_race
			) 
			AND 
			(
				{1}.rr_r_id = {0}.rh_id
			)
		ORDER BY {0}.rh_id DESC
	"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		const.VIEW_KJDB_RACE_RESULT
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret




def get_race_te_by_horse_id_to_df(accessor, horse_id_list, tecode_list):
	horse_id_where =''
	te_where =''
	for horse_id in horse_id_list:
		if(len(horse_id_where)):
			horse_id_where += f" OR {const.VIEW_KJDB_RACE_RESULT}.rr_r_horse_id = '{horse_id}' "
		else:
			horse_id_where = f" {const.VIEW_KJDB_RACE_RESULT}.rr_r_horse_id = '{horse_id}' "

	for te_code in tecode_list:
		if(len(te_where)):
			te_where += f" OR {const.TBL_KJDB_RACE_HEADER}.rh_te_bpd_code = '{te_code}' "
		else:
			te_where = f" {const.TBL_KJDB_RACE_HEADER}.rh_te_bpd_code = '{te_code}' "
	template =  """
		SELECT
			{1}.rr_r_rank
		FROM
		{1} 
		INNER JOIN {0} 
			ON {0}.rh_id = {1}.rr_r_id 
			AND {0}.rh_race = {1}.rr_r_race 
		WHERE
		(
			{2}
		)
		and
		(
			{3}
		)
		
	"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		const.VIEW_KJDB_RACE_RESULT,
		horse_id_where,
		te_where
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_child_record_by_horse_id_list_to_df(accessor, horse_id_list):
	horse_id_where =''
	for horse_id in horse_id_list:
		if(len(horse_id_where)):
			horse_id_where += f" OR rr_r_horse_id = '{horse_id}' "
		else:
			horse_id_where = f" rr_r_horse_id = '{horse_id}' "

	template =  """
		SELECT
			CInt(rr_r_rank) as rank  ,rh_te_bpd_code
		FROM
		{1} 
		INNER JOIN {0} 
			ON {0}.rh_id = {1}.rr_r_id 
			AND {0}.rh_race = {1}.rr_r_race 
		WHERE
		(
			{2}
		)
	"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		const.VIEW_KJDB_RACE_RESULT,
		horse_id_where
		)
	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_horses_by_smid_to_df(accessor, sire_id, mare_id):
	template = """
		select 
			CInt({1}.rr_r_rank) as rank  ,{0}.rh_te_bpd_code
		FROM
		{1} 
		INNER JOIN {0} 
			ON {0}.rh_id = {1}.rr_r_id 
			AND {0}.rh_race = {1}.rr_r_race 
		WHERE
		(
			(
				{1}.rr_m_blood01 = '{2}'
				AND
				{1}.rr_m_blood02 = '{3}'
			)
			OR
			(
				{1}.rr_m_blood03 = '{2}'
				AND
				{1}.rr_m_blood04 = '{3}'
			)
			OR
			(
				{1}.rr_m_blood05 = '{2}'
				AND
				{1}.rr_m_blood06 = '{3}'
			)
			OR
			(
				{1}.rr_m_blood07 = '{2}'
				AND
				{1}.rr_m_blood08 = '{3}'
			)
			OR
			(
				{1}.rr_m_blood09 = '{2}'
				AND
				{1}.rr_m_blood10 = '{3}'
			)
			OR
			(
				{1}.rr_m_blood11 = '{2}'
				AND
				{1}.rr_m_blood12 = '{3}'
			)
			OR
			(
				{1}.rr_m_blood13 = '{2}'
				AND
				{1}.rr_m_blood14 = '{3}'
			)
		)
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		const.VIEW_KJDB_RACE_RESULT,
		sire_id, 
		mare_id
		)
	# cmd = cmd.replace( '\n' , ' ' )
	# cmd = cmd.replace( '\t' , ' ' )			
	ret = accessor.read_sql_to_df(cmd)
	return ret  


def get_horses_rank_lineage_to_df(accessor):
	template = """
		select 
			CInt({1}.rr_r_rank) as rank  ,{0}.rh_te_bpd_code, 
			{1}.rr_r_horse_id,
			{1}.rr_m_blood01,
			{1}.rr_m_blood02,
			{1}.rr_m_blood03,
			{1}.rr_m_blood04,
			{1}.rr_m_blood05,
			{1}.rr_m_blood06,
			{1}.rr_m_blood07,
			{1}.rr_m_blood08,
			{1}.rr_m_blood09,
			{1}.rr_m_blood10,
			{1}.rr_m_blood11,
			{1}.rr_m_blood12,
			{1}.rr_m_blood13,
			{1}.rr_m_blood14
		FROM
		{1} 
		INNER JOIN {0} 
			ON {0}.rh_id = {1}.rr_r_id 
			AND {0}.rh_race = {1}.rr_r_race 
		"""
	cmd = template.format(
		const.TBL_KJDB_RACE_HEADER,
		const.VIEW_KJDB_RACE_RESULT
		)
	# cmd = cmd.replace( '\n' , ' ' )
	# cmd = cmd.replace( '\t' , ' ' )			
	ret = accessor.read_sql_to_df(cmd)
	return ret  


def get_rantime_by_ypdtc_to_df(accessor, y, p, d, t, c):
	   
	template =  """
		select 
			{2}.rr_r_time
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_year='{3}'
			and
			{0}.ph_place='{4}'
			and
			{1}.rh_distance='{5}'
			and
			{1}.rh_track='{6}'
			and
			{1}.rh_te_c2_code='{7}'
			and
			{2}.rr_r_time<>'0000'
			
		)
		order by 
			{0}.ph_place,
			{1}.rh_te_c2_code,
			{1}.rh_distance,
			{1}.rh_track
			 
	"""
	view = const.VIEW_KJDB_RACE_RESULT
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		y,
		p,
		d,
		t,
		c
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)   
	return ret


def get_conditions_by_y(accessor, y):
	template = """
		select 
			distinct {0}.ph_place, {1}.rh_te_c2_code, {1}.rh_distance, {1}.rh_track
		from	   
			{0} inner join {1} 
			on 
			    {0}.ph_id = {1}.rh_id 
		WHERE 
			{0}.ph_year ='{2}'
		ORDER BY
			{0}.ph_place,
			{1}.rh_distance, 
			{1}.rh_track,
			{1}.rh_te_c2_code 
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER,
		y)
	ret = accessor.read_sql_to_df(cmd)
	return ret

#レースヘッダ一覧を返す
def get_condition_headers_by_y(accessor, y):
	template = """
		select  
			{0}.*,{1}.*
		from	   
			{0} inner join {1} 
			on 
			    {0}.ph_id = {1}.rh_id 
		where rh_id like '{2}%'
		"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER,
		y)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_rantime_by_y_to_df(accessor, y):
	   
	template =  """
		select 
			{2}.rr_r_time,
			{0}.ph_place,
			{1}.rh_distance,
			{1}.rh_track,
			{1}.rh_te_c2_code
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_year='{3}'	
		)
		order by 
			{0}.ph_place,
			{1}.rh_te_c2_code,
			{1}.rh_distance,
			{1}.rh_track
			 
	"""
	view = const.VIEW_KJDB_RACE_RESULT
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		const.VIEW_KJDB_RACE_RESULT,
		y
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)   
	return ret



def get_horse_by_pdt_to_df(accessor, p, d, t):
	   
	template =  """
		select 
			{0}.*,{1}.*,{2}.*
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_place='{3}'
			and
			{1}.rh_distance='{4}'
			and
			{1}.rh_track='{5}'
			
		)
		order by 
			{0}.ph_place,
			{1}.rh_distance,
			{1}.rh_track
			 
	"""
	view = const.VIEW_KJDB_RACE_RESULT
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		view,
		p,
		d,
		t
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)   
	return ret



def get_program_race_to_df(accessor):
	ret = pd.DataFrame()
	
	template =  """
		select 
			{0}.*, {1}.*
		from
			{0} 
			INNER JOIN {1} 
				ON {0}.ph_id = {1}.rh_id
		order by 
			{0}.ph_id desc
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )			
	ret = accessor.read_sql_to_df(cmd)   
	return ret


#指定年のレースヘッダを返す。
def get_race_header_by_ptd_to_df(accessor, p, t, d):  
	template = """
		select {1}.* 
		from 
			{0} 
			INNER JOIN {1} 
				ON {0}.ph_id = {1}.rh_id
		where 
			ph_place = '{2}' 
			and
			rh_track = '{3}' 
			and
			rh_distance = '{4}'
			
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER,	
		p, t, d)
	ret = accessor.read_sql_to_df(cmd)
	return ret


#指定年のレースヘッダを返す。
def get_race_header_by_ptdc_to_df(accessor, p, t, d, c):  
	template = """
		select {1}.* 
		from 
			{0} 
			INNER JOIN {1} 
				ON {0}.ph_id = {1}.rh_id
		where 
			ph_place = '{2}' 
			and
			rh_track = '{3}' 
			and
			rh_distance = '{4}'
			and
			rh_te_c2_code = '{5}'
			
	"""
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER,	
		p, t, d, c)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_sire_score_info_by_ysid_to_df(accessor,  y, sire_id, ad_year=2000): 
	ret = pd.DataFrame()
	if(ad_year <= y):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)   
		template =  """
			select 
				{0}.ph_id, {1}.rh_te_bpd_code, CLng({2}.rr_r_rank) as rank 
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					{2}.rr_m_blood01 ='{3}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			sire_id
			)
		
		ret = accessor.read_sql_to_df(cmd) 
	return ret

def get_sire_score_info_by_ysid_to_df(accessor,  y, sire_id, ad_year=2000): 
	ret = pd.DataFrame()
	if(ad_year <= y):
		mdb = const.TBL_KJDB_RACE_RESULT_AT.format(y)   
		template =  """
			select 
				{0}.ph_id, {1}.rh_te_bpd_code, CLng({2}.rr_r_rank) as rank 
			from	   
				(({1} inner join
				{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
				{0} on {2}.rr_r_id = {0}.ph_id)
			where  
			(  
					{2}.rr_m_blood01 ='{3}'
				and
					{2}.rr_r_rank <> '00'
			)
			order by 
				{0}.ph_id
		"""

		cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			mdb,
			sire_id
			)
		
		ret = accessor.read_sql_to_df(cmd) 
	return ret


def get_avg_mul_score_by_cls(accessor, cls_code): 
		
	template = """
		SELECT
			AVG(rank) AS average_rank
		FROM
			(
				SELECT
					AVG(IIf({2}.rr_r_rank IN ('01', '02', '03'), 1, 0)) AS rank
				FROM
					(({1}
					INNER JOIN {2} ON {1}.rh_id = {2}.rr_r_id AND {1}.rh_race = {2}.rr_r_race)
					INNER JOIN {0} ON {2}.rr_r_id = {0}.ph_id)
				WHERE 
					{1}.rh_te_c2_code='{3}'
					AND
					{2}.rr_a_race_count > 4

				GROUP BY
					{2}.rr_r_id
			) AS subquery
		WHERE
			rank > 0
		"""

	cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			const.TBL_KJDB_RACE_RESULT,
			cls_code
			)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )				
	accessor.execute(cmd) 
	ret =.0
	for c in accessor.cur.fetchall():
		if(c[0] is None):
			pass
		else:
			ret = float(c[0])
		break	 
	return ret

def get_avg_win_score_by_cls(accessor, cls_code): 
		
	template = """
		SELECT
			AVG(rank) AS average_rank
		FROM
			(
				SELECT
					AVG(IIf({2}.rr_r_rank IN ('01'), 1, 0)) AS rank
				FROM
					(({1}
					INNER JOIN {2} ON {1}.rh_id = {2}.rr_r_id AND {1}.rh_race = {2}.rr_r_race)
					INNER JOIN {0} ON {2}.rr_r_id = {0}.ph_id)
				WHERE 
					{1}.rh_te_c2_code='{3}'
					AND
					{2}.rr_a_race_count > 4

				GROUP BY
					{2}.rr_r_id
			) AS subquery
		WHERE
			rank > 0
		"""

	cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			const.TBL_KJDB_RACE_RESULT,
			cls_code
			)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )				
	accessor.execute(cmd) 
	ret =.0
	for c in accessor.cur.fetchall():
		if(c[0] is None):
			pass
		else:
			ret = float(c[0])
		break	 
	return ret

def get_avg_mul_score_by_sire_id(accessor, sire_id): 
		
	template = """
		SELECT
			AVG(rank) AS average_rank
		FROM
			(
				SELECT
					AVG(IIf({2}.rr_r_rank IN ('01', '02', '03'), 1, 0)) AS rank
				FROM
					(({1}
					INNER JOIN {2} ON {1}.rh_id = {2}.rr_r_id AND {1}.rh_race = {2}.rr_r_race)
					INNER JOIN {0} ON {2}.rr_r_id = {0}.ph_id)
				WHERE 
					{2}.rr_m_blood01='{3}'
					AND
					{2}.rr_a_race_count > 4

				GROUP BY
					{2}.rr_r_id
			) AS subquery
		WHERE
			rank > 0
		"""

	cmd = template.format(
			const.TBL_KJDB_PROGRAM_HEADER, 
			const.TBL_KJDB_RACE_HEADER, 
			const.TBL_KJDB_RACE_RESULT,
			sire_id
			)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )				
	accessor.execute(cmd) 
	for c in accessor.cur.fetchall():
		if(c[0] is None):
			pass
		else:
			ret = float(c[0])
		break	 
	return ret


def get_parent_score_by_pdt_to_df(accessor, p, d, t):
	   
	template =  """
		select 
			{0}.*, {1}.*, {2}.rr_m_blood01, {2}.rr_m_blood02, CInt({2}.rr_r_rank) as rank 
		from	   
			(({1} inner join
			{2} on {1}.rh_id = {2}.rr_r_id and {1}.rh_race = {2}.rr_r_race) inner join 
			{0} on {2}.rr_r_id = {0}.ph_id)
		where  
		(  
			{0}.ph_place='{3}'
			and
			{1}.rh_distance='{4}'
			and
			{1}.rh_track='{5}'
			and
   			{2}.rr_r_rank<>'00'
		)
		order by 
			{0}.ph_place,
			{1}.rh_distance,
			{1}.rh_track
			 
	"""
	view = const.VIEW_KJDB_RACE_RESULT
	cmd = template.format(
		const.TBL_KJDB_PROGRAM_HEADER, 
		const.TBL_KJDB_RACE_HEADER, 
		view,
		p,
		d,
		t
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)   
	return ret