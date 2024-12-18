# 特徴量フォーマット

from model.features.format.concrete.DescConvFormatter import DescConvFormatter
from collections import OrderedDict
import pandas as pd
import os
import inspect
class FeatureFormatter(OrderedDict):
  
	def __init__(self):
		pass

	def doit(self):
		temp_list = []
		try:
			for index, formatter in self.items():
				temp_list.append(formatter.doit())
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')

		mearge_dict = {}
		for element in temp_list:
			mearge_dict.update(element)
		ret = pd.Series(mearge_dict)
		return ret
		
		
	def clear_val(self):
		for key, formatter in self.items():
			formatter.clear_val()
