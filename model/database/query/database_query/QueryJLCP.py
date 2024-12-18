

import model.conf.KJraConst as const
import pandas as pd


def get_record_at_to_sr(accessor, parent_id):
	ret = pd.Series()
	template = """
		select	
			* 
		from 
			{0} 
		where 
			{0}.parent_id='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_LA_COUNT,
		parent_id)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret

#指定年のプログラムヘッダを返す。
def get_ids_to_df(accessor):
	template = """
		select	
			{0}.parent_id
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_LA_COUNT)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_zero_data_to_sr(accessor):

	template = """
		select	
			top 1 * 
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_LA_COUNT)
	#df_temp = accessor.read_sql_to_df(cmd)
	accessor.execute(cmd)

	columns = [column[0] for column in accessor.cur.description]

	ret = pd.Series(0, index=columns)

	return ret

def is_existed(accessor, parent_id):

	template = """
		select 
			count(*) 
		from 
			{0} 
		where 
			parent_id='{1}'
		"""
	cmd = template.format(
		const.TBL_KJDB_LA_COUNT,
		parent_id
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

