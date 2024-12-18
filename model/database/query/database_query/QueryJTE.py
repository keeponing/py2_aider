from numpy import empty
import pandas as pd
import model.conf.KJraConst as const
#統計情報値
def get_record_all_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		"""
	cmd = template.format(
		const.TBL_KJDB_TE_CACHE_VALIABLE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret

def get_te_to_sr(accessor, program_id, horse_id, is_direct=False):
	y = program_id[:4]
	if(False == is_direct):
		mdb = const.TBL_KJDB_TE_CACHE_VALIABLE_AT.format(y)
	else:
		mdb = const.TBL_KJDB_TE_CACHE_VALIABLE
	template = """
		select 
			*
		from 
			{0} 
		where
			te_id='{1}'
			and
			te_horse_id ='{2}'

		"""
	cmd = template.format(
		mdb,
		program_id,
		horse_id
		)
	dt_temp = accessor.read_sql_to_df(cmd)
	ret = pd.Series()
	if(len(dt_temp)):
		ret = dt_temp.iloc[0]
	return ret

def get_te_by_h_to_df(accessor, horse_id):
	template = """
		select 
			*
		from 
			{0} 
		where
			te_horse_id ='{1}'
		order by
			te_id
		"""
	cmd = template.format(
		const.TBL_KJDB_TE_CACHE_VALIABLE,
		horse_id
		)
	cmd = cmd.replace( '\n' , ' ' )
	cmd = cmd.replace( '\t' , ' ' )	
	ret = accessor.read_sql_to_df(cmd)
	return ret

def is_existed(accessor,  program_id, horse_id):
	template = """
		select 
			count(*) 
		from 
			{0}
		where	
			te_id='{1}'
			and
			te_horse_id ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_TE_CACHE_VALIABLE,
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

def get_upd(accessor,  program_id, horse_id):
	template = """
		select 
			upd
		from 
			{0}
		where	
			te_id='{1}'
			and
			te_horse_id ='{2}'
		"""
	cmd = template.format(
		const.TBL_KJDB_TE_CACHE_VALIABLE,
		program_id,
		horse_id
		)
	accessor.execute(cmd)
	ret = 0
	for c in accessor.cur.fetchall():
		ret = int(c[0])
		break
	accessor.cur_close()
	return ret

def get_record_non_upd2_to_df(accessor):
	template = """
		select 
			*
		from 
			{0} 
		where 
			upd<>2
		order by te_id desc
		"""
	cmd = template.format(
		const.TBL_KJDB_TE_CACHE_VALIABLE
		)
	ret = accessor.read_sql_to_df(cmd)
	return ret


def get_record_to_sr2(accessor, program_id, horse_id, is_direct=False):
	ret = pd.Series()
	y = program_id[:4]
	if(1999< int(y)):
	
		if(False == is_direct):
			mdb = const.TBL_KJDB_TE_CACHE_VALIABLE_AT.format(y)
		else:
			mdb = const.TBL_KJDB_TE_CACHE_VALIABLE
		cmd = f"""
			SELECT 
				{mdb}.*
			FROM 
				{mdb}
			WHERE
				te_id = '{program_id}'
				AND 
				te_horse_id='{horse_id}'
			"""
		
		df_temp = accessor.read_sql_to_df(cmd)
		if(len(df_temp)):
			ret = df_temp.iloc[0]
	return ret


def get_te_col():
	ret = [
	'te_09T1823',
	'te_07D2330',
	'te_07T1418',
	'te_05T1418',
	'te_06T1418',
	'te_99D1418',
	'te_06D2330',
	'te_99T1418',
	'te_08T1823',
	'te_02T2330',
	'te_02D2330',
	'te_10D1418',
	'te_09T0714',
	'te_03D1418',
	'te_99T1823',
	'te_10T30OV',
	'te_05T1823',
	'te_09D0714',
	'te_09T2330',
	'te_01D0714',
	'te_10D2330',
	'te_05D1418',
	'te_05D1823',
	'te_10D0714',
	'te_03T2330',
	'te_08D0714',
	'te_06T2330',
	'te_03T1418',
	'te_99T0714',
	'te_08T0714',
	'te_05T0714',
	'te_99T30OV',
	'te_02T1823',
	'te_01T1823',
	'te_07T0714',
	'te_02T0714',
	'te_09D1418',
	'te_06T30OV',
	'te_08T2330',
	'te_09D1823',
	'te_99D2330',
	'te_10T2330',
	'te_06T1823',
	'te_09T1418',
	'te_03T0714',
	'te_03D2330',
	'te_06D0714',
	'te_99D0714',
	'te_07D1418',
	'te_03D0714',
	'te_07T2330',
	'te_99D30OV',
	'te_04D2330',
	'te_07T30OV',
	'te_06T0714',
	'te_08D1823',
	'te_04T30OV',
	'te_06D1418',
	'te_07D0714',
	'te_01D2330',
	'te_02D1418',
	'te_04D1418',
	'te_01T1418',
	'te_03T1823',
	'te_08D1418',
	'te_01D1418',
	'te_04T1823',
	'te_10T1418',
	'te_01T2330',
	'te_05D0714',
	'te_07T1823',
	'te_04T2330',
	'te_99D1823',
	'te_02D0714',
	'te_10T0714',
	'te_04D0714',
	'te_08T30OV',
	'te_04T1418',
	'te_02T1418',
	'te_03T30OV',
	'te_08T1418',
	'te_07D1823',
	'te_99T2330',
	'te_04T0714',
	'te_09T30OV',
	'te_01T0714',
	'te_10T1823',
	'te_05T30OV',
	'te_05T2330',
	'te_05D2330',	
	]
	#ret = [x for x in ret if not x.startswith('te_99')]
	return ret