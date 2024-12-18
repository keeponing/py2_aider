import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.target_encoding.base.TgtBase import TgtBase
import os
import inspect
#24-馬場-距離ターゲットエンコーディング
class Tgt002BD(TgtBase):
	_columns_list =[
			"te_D0714",
			"te_D1418",
			"te_D1823",
			"te_D2330",
			"te_D30OV",
			"te_T0714",
			"te_T1418",
			"te_T1823",
			"te_T2330",
			"te_T30OV",
	]
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	
	
	@staticmethod
	def create_zeros(output):
		
		df_temp =TgtBase.create_zeros(Tgt002BD._columns_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return TgtBase.create_zeros(Tgt002BD._columns_list)

	@staticmethod
	def create_zeros2(output):	
		return Tgt002BD.create_zeros(output)

	@staticmethod
	def create_zeros_series2():
		return Tgt002BD.create_zeros_series()