import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.target_encoding.base.TgtBase import TgtBase


#24-コーナーターゲットエンコーディング
class Tgt008C2(TgtBase):
	_columns_list =[
			'te_C2_00',
			'te_C2_01',
			'te_C2_02',
			'te_C2_03',
			'te_C2_04',
			'te_C2_05',
			'te_C2_06'
	]
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0


	@staticmethod
	def create_zeros(output):
		df_temp =Tgt008C2.create_zeros_series()
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():
		return TgtBase.create_zeros(Tgt008C2._columns_list)

	@staticmethod
	def create_zeros2(output):		
		return Tgt008C2.create_zeros(output)

	@staticmethod
	def create_zeros_series2():
		return Tgt008C2.create_zeros_series()