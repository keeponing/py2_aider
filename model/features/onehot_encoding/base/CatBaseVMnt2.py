import sys
sys.path.append(r"C:\Dev\py2")
import pandas as pd
from .CatBase import CatBase
import os
import inspect
#開催月符号化
class CatBaseVMnt2(CatBase):
	KEY_COS="cat_mnt_cos"
	KEY_SIN="cat_mnt_sin"

	CAT_LIST = []
	def __init__(self):
		self.foo = 0 

	#開催月符号化
	@staticmethod
	def to_onehot(series, key_list,  keys_code):
		try:

			mon = int(series[keys_code])
			dt = {}
			dt[CatBaseVMnt2.KEY_SIN]=.0
			dt[CatBaseVMnt2.KEY_COS]=.0
			if(1==mon):
				dt[CatBaseVMnt2.KEY_SIN]=.0
				dt[CatBaseVMnt2.KEY_COS]=1.0
			elif(2==mon):
				dt[CatBaseVMnt2.KEY_SIN]=0.5
				dt[CatBaseVMnt2.KEY_COS]=0.866025404
			elif(3==mon):
				dt[CatBaseVMnt2.KEY_SIN]=0.866025404
				dt[CatBaseVMnt2.KEY_COS]=0.5
			elif(4==mon):
				dt[CatBaseVMnt2.KEY_SIN]=1.0
				dt[CatBaseVMnt2.KEY_COS]=.0
			elif(5==mon):
				dt[CatBaseVMnt2.KEY_SIN]=0.866025404
				dt[CatBaseVMnt2.KEY_COS]=-0.5
			elif(6==mon):
				dt[CatBaseVMnt2.KEY_SIN]=0.5
				dt[CatBaseVMnt2.KEY_COS]=-0.866025404
			elif(7==mon):
				dt[CatBaseVMnt2.KEY_SIN]=.0
				dt[CatBaseVMnt2.KEY_COS]=-1.0
			elif(8==mon):
				dt[CatBaseVMnt2.KEY_SIN]=-0.5	
				dt[CatBaseVMnt2.KEY_COS]=-0.866025404
			elif(9==mon):
				dt[CatBaseVMnt2.KEY_SIN]=-0.866025404	
				dt[CatBaseVMnt2.KEY_COS]=-0.5
			elif(10==mon):
				dt[CatBaseVMnt2.KEY_SIN]=-1.0	
				dt[CatBaseVMnt2.KEY_COS]=.0
			elif(11==mon):
				dt[CatBaseVMnt2.KEY_SIN]=-0.866025404	
				dt[CatBaseVMnt2.KEY_COS]=0.5
			elif(12==mon):
				dt[CatBaseVMnt2.KEY_SIN]=-0.5	
				dt[CatBaseVMnt2.KEY_COS]=0.866025404
			ret = pd.Series(data= dt, index=key_list, dtype=float)
			return ret
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	#開催月符号化
	@staticmethod
	def to_cats(input):
		ret =0
		try:
			for i in range(len(CatBaseVMnt2.CAT_LIST)):
				if(CatBaseVMnt2.CAT_LIST[i] == input):
					ret=i
					break
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	



		return ret

	@staticmethod
	def prepare():
		try:
			CatBaseVMnt2.CAT_LIST =[]
			month = range(1, 13)
			for m in month:
				temp = f'{m:02}'
				CatBaseVMnt2.CAT_LIST.append(temp)

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
