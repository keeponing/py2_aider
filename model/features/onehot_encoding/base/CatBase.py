import sys
sys.path.append(r"C:\Dev\py2")

import numpy as np
import pandas as pd
import os
import inspect

class CatBase:
		def __init__(self):
			self.foo = 0 

		@staticmethod
		def to_onehot(sr_value, keylist, keys_code, key_format):
			try:
				zeros = np.zeros(len(keylist))
				series2 = pd.Series(data= zeros, index=keylist, dtype=int)
				index = int(sr_value[keys_code])
				if(0 != index):
					key = key_format.format(index)
					series2[key]=1
				return series2
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
    
		# @staticmethod
		# def to_onehot_m1(sr_value, keylist, keys_code, key_format):
		# 	try:
		# 		zeros = np.zeros(len(keylist))
		# 		series2 = pd.Series(data= zeros, index=keylist, dtype=int)
		# 		index = int(sr_value[keys_code])
		# 		index = index-1
		# 		if(0 < index):	
		# 			key = key_format.format(index)
		# 			series2[key]=1
		# 		return series2
		# 	except Exception as e:
		# 		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')		
    
		@staticmethod
		def create_zeros(keylist):
			try:
				zeros = np.zeros(len(keylist))
				return pd.Series(data= zeros, index=keylist, dtype=int)
			except Exception as e:
				print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
