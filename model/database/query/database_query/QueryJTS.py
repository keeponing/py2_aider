import pyodbc
import model.conf.KJraConst as const


def get_score_by_id_to_df(accessor, y, trainer_id):
	template = """
		select 
			*
		from 
			{0} 
		where
			ts_year = '{1}'
			and
			ts_id ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_TRAINER_SCORE,
		y,
		trainer_id
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret
