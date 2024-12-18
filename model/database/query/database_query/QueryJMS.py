import pyodbc
import model.conf.KJraConst as const


def get_master_sire_list_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_SIRE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_master_sire_id_list(accessor):
	# template = """
	#	 select 
	#		 StrConv(ms_name,4) as ms_name2
	#	 from 
	#		 {0} 
	#	 order by ms_id
	#	 """
	template = """
		select 
			ms_id
		from 
			{0} 
		order by ms_id
		"""
	cmd = template.format(
		const.TBL_KJDB_MASTER_SIRE
		)
	temp = accessor.read_sql_to_df(cmd)
	series = temp.iloc[:,0]
	ret = series.tolist()
	# ret = []
	# for temp3 in temp2:
	#	 ret.append(temp3.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})))
	return ret