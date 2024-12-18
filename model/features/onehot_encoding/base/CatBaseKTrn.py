import sys
sys.path.append(r"C:\Dev\py2")

import model.database.query.database_query.QueryJMT as qjmt
from .CatBase import CatBase
import os
import inspect

#調教師符号化
class CatBaseKTrn(CatBase):
	TRAINER_MAP ={}

	def __init__(self):
		self.foo = 0 

	#調教師データ化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#調教師符号化
	@staticmethod
	def to_cats(input):
		ret ="00000"
		try:
			#ret = CatBaseKTrn.TRAINER_MAP[input]
			ret = input
		except Exception as e:
			#print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			ret ="00000"
		return ret 
		
	#調教師リスト作成
	@staticmethod
	def prepare(accessor):
		CatBaseKTrn.TRAINER_MAP={}
		df_list = qjmt.get_master_trainer_list_to_df(accessor)
		CatBaseKTrn.TRAINER_MAP['00000'] = 0
		for _, df in df_list.iterrows():
			CatBaseKTrn.TRAINER_MAP[df['mt_id']] = df['mt_cluster']