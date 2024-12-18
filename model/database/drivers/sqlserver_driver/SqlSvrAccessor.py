#pymssqlアクセッサ
import sys
sys.path.append(r"C:\Dev\py2")
import pymssql
import pandas as pd
import warnings
warnings.simplefilter('ignore')
from tenacity import retry, stop_after_attempt, wait_fixed, RetryError

class SqlSvrAccessor:
	def __init__(self):
		
		self.conn = None
		self.cur = None

	#mdbのオープン
	@retry(stop=stop_after_attempt(4), wait=wait_fixed(1))
	def open(self, server_name="192.168.1.3"):
	#def open(self, server_name="staging-vm2"):
	#def open(self, server_name="staging-vm2"):
	#def open(self, server_name="acer-pc"):
		self.conn = pymssql.connect(
			server=server_name, 
			user='kjvan_user', 
			password='kiichi1', 
			database='Kjvan')
		self.cur = self.conn.cursor()
		

	def cur_close(self):
		if(None != self.cur):
			self.cur.close()
			self.cur=None
	#mdbのクローズ
	def close(self):
		self.conn.close()
		self.conn=None
			

	#コマンドの実行
	def execute(self, cmd):
		self.cur = self.conn.cursor()
		self.cur.execute(cmd)
		#self.cur.fetchone() 

	#コマンドの実行
	def commit(self):

		#row = self.cur.fetchall()
		self.conn.commit()
	
	# dfに格納
	@retry(stop=stop_after_attempt(3), wait=wait_fixed(3))
	def read_sql_to_df(self,cmd):
		return pd.read_sql_query(cmd, self.conn)

	def upsert(self, df, table):
		df.to_sql(table, self.conn, if_exists='replace')

	def read_sql_with_outlier(self,cmd):
		df = self.read_sql_to_df(cmd)
		return df
   
