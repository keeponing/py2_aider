#mdbアクセッサ
import sys
sys.path.append(r"C:\Dev\py2")
import model.conf.KJraConfig as conf
import pyodbc
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_fixed, RetryError

class MdbAccessor:
    def __init__(self):
       
        self.conn = None
        self.cur = None

    #mdbのオープン
    #@retry(stop=stop_after_attempt(4), wait=wait_fixed(1))
    def open(self, con_str=conf.KJDB_MDB_FILE):
        template = 'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};'
        # template = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=\"{0}\";"
        self.conn = pyodbc.connect(template.format(con_str))
        

    def cur_close(self):
        if(None != self.cur):
            self.cur.close()
            self.cur=None
    #mdbのクローズ
    def close(self):
        self.conn.close()
        self.conn=None
            

    #コマンドの実行
    #@retry(stop=stop_after_attempt(4), wait=wait_fixed(1))
    def execute(self, cmd):
        self.cur = self.conn.cursor()
        self.cur.execute(cmd)
    
    def execute_no_retry(self, cmd):
        self.cur = self.conn.cursor()
        self.cur.execute(cmd)
    #コマンドの実行
    def commit(self):
        self.cur.commit()
    
    # dfに格納
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(1))
    def read_sql_to_df(self,cmd):
        return pd.read_sql_query(cmd, self.conn)

    def upsert(self, df, table):
        df.to_sql(table, self.conn, if_exists='replace')

    def read_sql_with_outlier(self,cmd):
        df = self.read_sql_to_df(cmd)
        return df
   
