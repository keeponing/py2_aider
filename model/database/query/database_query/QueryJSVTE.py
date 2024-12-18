import pyodbc
import model.conf.KJraConst as const
import pandas as pd
#統計情報値

def get_record_at_to_df(accessor, program_id, horse_id):
	template = """
		SELECT {0}.*, {1}.*
		FROM 
  			{0} INNER JOIN {1} ON 
     			({0}.sv_horse_id = {1}.te_horse_id) 
        	AND 
         		({0}.sv_program_id = {1}.te_id)
		WHERE
			{0}.sv_program_id ='{2}'
			AND
			{0}.sv_horse_id ='{3}'
		"""
	cmd = template.format(
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE,
  		const.TBL_KJDB_TE_CACHE_VALIABLE,
		program_id, 
		horse_id
		)
	df_temp = accessor.read_sql_to_df(cmd)
	ret = pd.Series()
	if(0!=len(df_temp)):
		ret = df_temp.iloc[0]
	return ret
