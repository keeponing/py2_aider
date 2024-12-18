import sys
import os
import inspect
sys.path.append(r"C:\Dev\py2")
import numpy as np
from model.features.format.base.FeatureBaseFormatter import FeatureBaseFormatter
from model.features.format.base.FeatureBaseFormatter import FormatType
#
# 無変換フォーマット
#
class SimpleFormatter(FeatureBaseFormatter):
	def __init__(self, prefix, options=None):
		super().__init__(prefix, FormatType.NoConv, options)


	def doit(self):
		ret ={}
		try:
			#print(f'SimpleFormatter do it. {self._prefix} {self._val}')
			ret[f'{self._prefix}'] = self._val
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret