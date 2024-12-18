import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd


#統計量データ基本
class SvBase():

	def __init__(self):
		self.foo = 0 

	@staticmethod
	def create_zeros(keylist):
		try:
			zeros = np.zeros(len(keylist))
			return pd.Series(data= zeros, index=keylist, dtype=int)
		except Exception as e:
			print('SvBase:create_zeros:{}'.format(e) )  