import model.conf.KJraConst as const
import pyodbc


# #特徴量データ

#IDと一致するレコードを取得する。
def get_record_all_to_df(accessor):
	template = """
		select
			{0}.* ,{1}.* ,{2}.* 
		from 
			(
				(
				{1} inner join
					{2} on 
     					{1}.te_id = {2}.sv_program_id 
          				and 
              			{1}.te_horse_id = {2}.sv_horse_id
				) 
      		inner join 
				{0} on 
    				{2}.sv_program_id = {0}.key_program_id 
        			and 
           			{2}.sv_horse_id = {0}.key_horse_id
   			)
		order by 
			{0}.key_program_id
		"""
	cmd = template.format(
		const.TBL_KJDB_PREDICT_CACHE_VALIABLE,
		const.TBL_KJDB_TE_CACHE_VALIABLE,
		const.TBL_KJDB_STATISTICS_CACHE_VALIABLE
		)
	ret = accessor.read_sql_with_outlier(cmd)
	return ret  