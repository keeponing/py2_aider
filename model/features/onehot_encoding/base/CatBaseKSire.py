import sys
sys.path.append(r"C:\Dev\py2")

import model.database.query.database_query.QueryJMS as qjms
from .CatBase import CatBase
import os
import inspect
#種牡馬符号化
class CatBaseKSire(CatBase):
	SIRE_MAP = {}
 
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def to_onehot(series, keylist, keys_code, key_format):
		try:
			return CatBase.to_onehot(series, keylist, keys_code, key_format)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	

	#種牡馬符号化
	@staticmethod
	def to_cats(input):
		ret ="0000000000"
		try:
			#ret = CatBaseKSire.SIRE_MAP[input]
			ret =input
		except Exception as e:
			#print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
			ret ="0000000000"
		return ret 
	#種牡馬リスト作成
	@staticmethod
	def prepare(accessor):
		CatBaseKSire.SIRE_MAP={}
		df_list = qjms.get_master_sire_list_to_df(accessor)
		CatBaseKSire.SIRE_MAP['0000000000'] = 0
		for _, df in df_list.iterrows():
			CatBaseKSire.SIRE_MAP[df['ms_id']] = df['ms_cluster']