import sys
sys.path.append(r"C:\Dev\py2")

import model.database.query.database_query.QueryJMJ as qjmj
from .CatBase import CatBase
import os
import inspect

#ジョッキー符号化
class CatBaseKJcy(CatBase):
	JOCKEY_MAP ={}

	def __init__(self):
		self.foo = 0 

	#ジョッキーデータ化
	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#ジョッキー符号化
	@staticmethod
	def to_cats(input):
		ret ="00000"
		try:
			#ret = CatBaseKJcy.JOCKEY_MAP[input]
			ret = input
		except Exception as e:
			#print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
			ret ="00000"
		return ret 
		
	#ジョッキーリスト作成
	@staticmethod
	def prepare(accessor):
		CatBaseKJcy.JOCKEY_MAP={}
		df_list = qjmj.get_master_jockey_list_to_df(accessor)
		CatBaseKJcy.JOCKEY_MAP['00000'] = 0
		for _, df in df_list.iterrows():
			CatBaseKJcy.JOCKEY_MAP[df['mj_id']] = df['mj_cluster']