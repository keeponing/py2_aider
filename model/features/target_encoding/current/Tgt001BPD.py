import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
import pandas as pd
from model.features.target_encoding.base.TgtBase import TgtBase
import os
import inspect
#24-馬場-会場-距離ターゲットエンコーディング
class Tgt001BPD(TgtBase):
	_columns_list =[
			"te_09T1823",
			"te_07D2330",
			"te_07T1418",
			"te_05T1418",
			"te_06T1418",
			"te_99D1418",
			"te_06D2330",
			"te_99T1418",
			"te_08T1823",
			"te_02T2330",
			"te_02D2330",
			"te_10D1418",
			"te_09T0714",
			"te_03D1418",
			"te_99T1823",
			"te_10T30OV",
			"te_05T1823",
			"te_09D0714",
			"te_09T2330",
			"te_01D0714",
			"te_10D2330",
			"te_05D1418",
			"te_05D1823",
			"te_10D0714",
			"te_03T2330",
			"te_08D0714",
			"te_06T2330",
			"te_03T1418",
			"te_99T0714",
			"te_08T0714",
			"te_05T0714",
			"te_99T30OV",
			"te_02T1823",
			"te_01T1823",
			"te_07T0714",
			"te_02T0714",
			"te_09D1418",
			"te_06T30OV",
			"te_08T2330",
			"te_09D1823",
			"te_99D2330",
			"te_10T2330",
			"te_06T1823",
			"te_09T1418",
			"te_03T0714",
			"te_03D2330",
			"te_06D0714",
			"te_99D0714",
			"te_07D1418",
			"te_03D0714",
			"te_07T2330",
			"te_99D30OV",
			"te_04D2330",
			"te_07T30OV",
			"te_06T0714",
			"te_08D1823",
			"te_04T30OV",
			"te_06D1418",
			"te_07D0714",
			"te_01D2330",
			"te_02D1418",
			"te_04D1418",
			"te_01T1418",
			"te_03T1823",
			"te_08D1418",
			"te_01D1418",
			"te_04T1823",
			"te_10T1418",
			"te_01T2330",
			"te_05D0714",
			"te_07T1823",
			"te_04T2330",
			"te_99D1823",
			"te_02D0714",
			"te_10T0714",
			"te_04D0714",
			"te_08T30OV",
			"te_04T1418",
			"te_02T1418",
			"te_03T30OV",
			"te_08T1418",
			"te_07D1823",
			"te_99T2330",
			"te_04T0714",
			"te_09T30OV",
			"te_01T0714",
			"te_10T1823",
			"te_05T30OV",
			"te_05T2330",
			"te_05D2330",

		]
	def __init__(self):
		self.foo = 0 

	@staticmethod
	def prepare():
		i=0

	@staticmethod
	def create_zeros(output):
		
		df_temp =TgtBase.create_zeros(Tgt001BPD._columns_list)
		return pd.concat([output, df_temp])

	@staticmethod
	def create_zeros_series():	
		return TgtBase.create_zeros(Tgt001BPD._columns_list)

	@staticmethod
	def create_zeros2(output):
		return Tgt001BPD.create_zeros_series()

	@staticmethod
	def create_zeros_series2():
		return Tgt001BPD.create_zeros_series()