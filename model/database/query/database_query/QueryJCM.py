
import model.conf.KJraConst as const
import pandas as pd

def get_comment_by_ihi_to_sr(accessor, proram_id, horse_id):
	ret = pd.Series()
	template = """
		select 
			*
		from 
			{0} 
		where
			cm_id ='{1}'
			and
			cm_horse_id ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_COMMENT,
		proram_id,
		horse_id
		)
	df_temp = accessor.read_sql_to_df(cmd)
	if(len(df_temp)):
		ret = df_temp.iloc[0]
	return ret
