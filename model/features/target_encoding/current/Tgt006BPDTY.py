import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.target_encoding.base.TgtBase import TgtBase
import os
import inspect
#24-馬場-会場-距離ターゲットエンコーディング
class Tgt006BPDTY(TgtBase):
	_columns_list =[
			'te_bpdty',
		]
	VALUE_NAME ='te_value'
	VALUE_NEW_NAME ='te_value_ty'
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def create_zeros(output):
		key_list =[
			Tgt006BPDTY.VALUE_NEW_NAME
		]
		df_temp =TgtBase.create_zeros(key_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		key_list =[
			Tgt006BPDTY.VALUE_NEW_NAME
		]
		return TgtBase.create_zeros(key_list)


	@staticmethod
	def create_zeros2(output):
		df_temp =TgtBase.create_zeros(Tgt006BPDTY._columns_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series2():
		return TgtBase.create_zeros(Tgt006BPDTY._columns_list)