
import sys
sys.path.append(r"C:\Dev\py2")
import model.conf.KJraConfig as conf
from model.database.drivers.mdb_driver.MdbAccessor import MdbAccessor
from model.database.drivers.sqlserver_driver.SqlSvrAccessor  import SqlSvrAccessor
import os
import inspect
#データベースファクトリ
class DatabaseFactory:
	ACC_ACCESSOR = "acc_accessor"
	MST_ACCESSOR = "mst_accessor"
	SQL_ACCESSOR = "sql_accessor"
	SCR_ACCESSOR = "scr_accessor"
	PV_ACCESSOR2 = "pv_accessors2"
	CMT_ACCESSOR = "cmt_accessor"
	PRD_ACCESSOR = "prd_accessor"
	LAC_ACCESSOR = "lac_accessor"
	LAP_ACCESSOR = "lap_accessor"
	_instance = None
	_acc_accessor = None
	_mst_accessor = None
	_sql_accessor = None
	_scr_accessor = None
	_cmt_accessor = None
	_pv_accessors2 = {}
	_prd_accessor = None
	_lac_accessor = None
	_lap_accessor = None
	def __new__(cls, *args, **kwargs):
		if cls._instance is None:
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance	

	def close(self):
		try:
			DatabaseFactory._acc_accessor.close()
			DatabaseFactory._mst_accessor.close()
			DatabaseFactory._sql_accessor.close()
			DatabaseFactory._scr_accessor.close()
			DatabaseFactory._cmt_accessor.close()
			DatabaseFactory._prd_accessor.close()
			DatabaseFactory._lac_accessor.close()
			DatabaseFactory._lap_accessor.close()
			#_pv_accessors
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')

	def get(self, keyword, arg=None):
		ret = None
		try:
			if(DatabaseFactory.ACC_ACCESSOR==keyword):
				if(DatabaseFactory._acc_accessor is None):
					DatabaseFactory._acc_accessor = MdbAccessor()
					DatabaseFactory._acc_accessor.open(conf.KJDB_MDB_FILE)
				
				ret = DatabaseFactory._acc_accessor
			elif(DatabaseFactory.MST_ACCESSOR==keyword):
				if(DatabaseFactory._mst_accessor is None):
					DatabaseFactory._mst_accessor = MdbAccessor()
					DatabaseFactory._mst_accessor.open(conf.KJDB_MASTER_MDB_FILE)
				ret = DatabaseFactory._mst_accessor
			elif(DatabaseFactory.SQL_ACCESSOR==keyword):
				if(DatabaseFactory._sql_accessor is None):
					DatabaseFactory._sql_accessor = SqlSvrAccessor()
					DatabaseFactory._sql_accessor.open()
				ret = DatabaseFactory._sql_accessor
			elif(DatabaseFactory.SCR_ACCESSOR==keyword):
				if(DatabaseFactory._scr_accessor is None):
					DatabaseFactory._scr_accessor = MdbAccessor()
					DatabaseFactory._scr_accessor.open(conf.KJDB_SCORE_MDB_FILE)
				ret = DatabaseFactory._scr_accessor
			elif(DatabaseFactory.PV_ACCESSOR2==keyword):
				ret = DatabaseFactory.get_pv_at(arg)
			elif(DatabaseFactory.CMT_ACCESSOR==keyword):
				if(DatabaseFactory._cmt_accessor is None):
					DatabaseFactory._cmt_accessor = MdbAccessor()
					DatabaseFactory._cmt_accessor.open(conf.KJDB_COMMENT_FILE)
				ret = DatabaseFactory._cmt_accessor
			elif(DatabaseFactory.PRD_ACCESSOR==keyword):
				if(DatabaseFactory._prd_accessor is None):
					DatabaseFactory._prd_accessor = MdbAccessor()
					DatabaseFactory._prd_accessor.open(conf.KJDB_PREDICT_SCORE_MDB_FILE)
				ret = DatabaseFactory._prd_accessor
			elif(DatabaseFactory.LAC_ACCESSOR==keyword):
				if(DatabaseFactory._lac_accessor is None):
					DatabaseFactory._lac_accessor = MdbAccessor()
					DatabaseFactory._lac_accessor.open(conf.KJDB_LINEAGE_COUPLE_MDB_FILE)
				ret = DatabaseFactory._lac_accessor
			elif(DatabaseFactory.LAP_ACCESSOR==keyword):
				if(DatabaseFactory._lap_accessor is None):
					DatabaseFactory._lap_accessor = MdbAccessor()
					DatabaseFactory._lap_accessor.open(conf.KJDB_LINEAGE_PAC_MDB_FILE)
				ret = DatabaseFactory._lap_accessor
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
	
	@staticmethod
	def get_pv_at(y):
		ret=None
		try:
			if(y in DatabaseFactory._pv_accessors2):
				ret = DatabaseFactory._pv_accessors2[y] 
			else:
				accessor = MdbAccessor()
				mdb = conf.KJDB_PREDICT_CAHCE_MDB_FILE.format(y)
				accessor.open(mdb)
				DatabaseFactory._pv_accessors2[y] = accessor
				ret = DatabaseFactory._pv_accessors2[y]
		except Exception as e: 
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret