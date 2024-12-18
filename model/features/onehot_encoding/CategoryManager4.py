
from model.features.onehot_encoding.current.Cat219CDiff import Cat219CDiff
from model.features.onehot_encoding.current.Cat218CDiff import Cat218CDiff
import inspect
import os
from model.features.onehot_encoding.current.Cat268CErr import Cat268CErr
from model.features.onehot_encoding.current.Cat267VYD import Cat267VYD
from model.features.onehot_encoding.current.Cat262BRcnt import Cat262BRcnt
from model.features.onehot_encoding.current.Cat233CBlng import Cat233CBlng
from model.features.onehot_encoding.current.Cat232CVt import Cat232CVt
from model.features.onehot_encoding.current.Cat231CHsgn import Cat231CHsgn
from model.features.onehot_encoding.current.Cat230BCnr import Cat230BCnr
from model.features.onehot_encoding.current.Cat229BCnr import Cat229BCnr
from model.features.onehot_encoding.current.Cat228BCnr import Cat228BCnr
from model.features.onehot_encoding.current.Cat227BCnr import Cat227BCnr
from model.features.onehot_encoding.current.Cat226BVote import Cat226BVote
from model.features.onehot_encoding.current.Cat223BGal import Cat223BGal
from model.features.onehot_encoding.current.Cat222CPm import Cat222CPm
from model.features.onehot_encoding.current.Cat217CDiff import Cat217CDiff
from model.features.onehot_encoding.current.Cat215CJmrk import Cat215CJmrk
from model.features.onehot_encoding.current.Cat211CSex import Cat211CSex
from model.features.onehot_encoding.current.Cat210BOld import Cat210BOld
from model.features.onehot_encoding.current.Cat209CBlink import Cat209CBlink
from model.features.onehot_encoding.current.Cat207CFrm import Cat207CFrm
from model.features.onehot_encoding.current.Cat206BRnk import Cat206BRnk
from model.features.onehot_encoding.current.Cat205BHn import Cat205BHn
from model.features.onehot_encoding.current.Cat120CGrd import Cat120CGrd
from model.features.onehot_encoding.current.Cat119BHcnt import Cat119BHcnt
from model.features.onehot_encoding.current.Cat118CClsT import Cat118CClsT
from model.features.onehot_encoding.current.Cat117BDst import Cat117BDst
from model.features.onehot_encoding.current.Cat116CRcnd import Cat116CRcnd
from model.features.onehot_encoding.current.Cat115CRule import Cat115CRule
from model.features.onehot_encoding.current.Cat114CClsY import Cat114CClsY
from model.features.onehot_encoding.current.Cat113CCls5 import Cat113CCls5
from model.features.onehot_encoding.current.Cat112CCls4 import Cat112CCls4
from model.features.onehot_encoding.current.Cat111CCls3 import Cat111CCls3
from model.features.onehot_encoding.current.Cat110CCls2 import Cat110CCls2
from model.features.onehot_encoding.current.Cat109CCat import Cat109CCat
from model.features.onehot_encoding.current.Cat107CBcd import Cat107CBcd
from model.features.onehot_encoding.current.Cat106CBct import Cat106CBct
from model.features.onehot_encoding.current.Cat105CTrk2 import Cat105CTrk2
from model.features.onehot_encoding.current.Cat104CWtr import Cat104CWtr
from model.features.onehot_encoding.current.Cat006VRpc import Cat006VRpc
from model.features.onehot_encoding.current.Cat004VEvtd import Cat004VEvtd
from model.features.onehot_encoding.current.Cat003VMnt2 import Cat003VMnt2
from model.features.onehot_encoding.current.Cat002VYear import Cat002VYear
from model.features.onehot_encoding.current.Cat001CPlc import Cat001CPlc
import pandas as pd
import sys
import copy
from model.database.drivers.driver_factory.QueryFactory import QueryFactory
sys.path.append(r"C:\Dev\py2")


# カテゴリマネージャ


class CategoryManager4:
	_cat_current_list = [
			Cat001CPlc,  # 001-開催場符号化
			# Cat002VYear,#002-開催年符号化
			Cat003VMnt2,  # 003-開催月符号化
			# Cat004VEvtd, #004-開催日符号化
			# T Cat006VRpc, #006-開催回符号化
			Cat104CWtr,  # 104-天候符号化
			Cat105CTrk2,  # 105-コース周り
			Cat106CBct,  # 106-芝馬場符号化
			Cat107CBcd,  # 107-ダート馬場符号化
			# Cat109CCat, #109-カテゴリ符号化
			# Cat110CCls2, #110-競走条件コード 2歳条件符号化
			# Cat111CCls3, #111-競走条件コード 3歳条件符号化
			# Cat112CCls4, #112-競走条件コード 4歳条件符号化
			# Cat113CCls5, #113-競走条件コード 5歳以上条件
			# Cat114CClsY, #114-競走条件コード 最若年条件
			Cat116CRcnd,  # 116-負担重量条件符号化
			Cat117BDst,  # 117-出走距離符号化
			Cat118CClsT,  # 118-競走条件コード 最大条件
			Cat119BHcnt,  # 119-出走頭数符号化
			Cat120CGrd,  # 120-グレード
			Cat205BHn,  # 205-馬番符号化
			Cat207CFrm,  # 207-枠符号化
			Cat209CBlink,  # 209-ブリンカー符号化
			Cat210BOld,  # 210-年齢符号化
			Cat211CSex,  # 211-性別符号化
			Cat215CJmrk,  # 215-騎手見習コード
			# Cat217CDiff, #217-着差コード1
			# Cat218CDiff, #218-着差コード2
			# Cat219CDiff, #219-着差コード3
			Cat222CPm,  # 222-+-符号化
			Cat223BGal,  # 223-馬体重増減符号化
			#Cat226BVote,  # 226-人気符号化
			# Cat227BCnr, #227-第一コーナー符号化■
			# Cat228BCnr, #228-第二コーナー符号化■
			# Cat229BCnr, #229-第三コーナー符号化■
			# Cat230BCnr, #230-第四コーナー符号化■
			# Cat231CHsgn, #231-馬記号コード■
			# Cat232CVt, #232-品種コード■
			# T Cat233CBlng, #233-東西所属コード符号化■
			Cat262BRcnt,  # 262-出走数符号化
			# Cat267VYD, #267-経過年符号化
			# Cat268CErr, #268-異常区分コード
		]

	_cat_history_list = [
			# T Cat001CPlc,  #001-開催場符号化
			# Cat002VYear,  #002-開催年符号化
			# Cat003VMnt2, #003-開催月符号化
			# Cat004VEvtd, #004-開催日符号化
			# Cat006VRpc, #006-開催回符号化
			# Cat104CWtr, #104-天候符号化
			# T Cat105CTrk2, #105-コース周り
			# T Cat106CBct, #106-芝馬場符号化
			# T Cat107CBcd, #107-ダート馬場符号化
			# Cat109CCat, #109-カテゴリ符号化
			# Cat110CCls2, #110-競走条件コード 2歳条件符号化
			# Cat111CCls3, #111-競走条件コード 3歳条件符号化
			# Cat112CCls4, #112-競走条件コード 4歳条件符号化
			# Cat113CCls5, #113-競走条件コード 5歳以上条件
			# Cat114CClsY, #114-競走条件コード 最若年条件
			# T Cat116CRcnd, #116-負担重量条件符号化
			# T Cat117BDst, #117-出走距離符号化
			# T Cat118CClsT, #118-競走条件コード 最大条件
			# T Cat119BHcnt, #119-出走頭数符号化
			# T Cat120CGrd, #120-グレード
			# T Cat205BHn, #205-馬番符号化
			# T Cat206BRnk, #206-着順符号化
			# T Cat207CFrm, #207-枠符号化
			# Cat209CBlink, #209-ブリンカー符号化
			# T Cat210BOld, #210-年齢符号化
			# T Cat211CSex, #211-性別符号化
			# T Cat215CJmrk, #215-騎手見習コード
			# T Cat217CDiff, #217-着差コード1
			# Cat218CDiff, #218-着差コード2
			# Cat219CDiff, #219-着差コード3
			# T Cat222CPm, #222-+-符号化
			# T Cat223BGal, #223-馬体重増減符号化
			# T Cat226BVote,  #226-人気符号化
			# T Cat227BCnr, #227-第一コーナー符号化
			# T Cat228BCnr, #228-第二コーナー符号化
			# T Cat229BCnr, #229-第三コーナー符号化
			# T Cat230BCnr, #230-第四コーナー符号化
			# Cat231CHsgn, #231-馬記号コード
			# Cat232CVt, #232-品種コード■
			# T Cat233CBlng,  #233-東西所属コード符号化■
			#T Cat262BRcnt, #262-出走数符号化
			# T Cat267VYD, #267-経過年符号化
			# T Cat268CErr, #268-異常区分コード
		]

	_cat_hot_list = [
			Cat104CWtr,  # 104-天候符号化
			Cat106CBct,  # 106-芝馬場符号化
			Cat107CBcd,  # 107-ダート馬場符号化
			Cat222CPm,  # 222-+-符号化
			Cat223BGal,  # 223-馬体重増減符号化
			#Cat226BVote,  # 226-人気符号化

		]

	def __init__(self):
		self.foo = 0

	@staticmethod
	def prepare(df_code):
		try:

			Cat001CPlc.prepare(df_code)  # 001-開催場符号化 ■
			Cat002VYear.prepare()  # 002-開催年符号化 ■
			Cat003VMnt2.prepare()  # 003-開催月符 ■
			Cat004VEvtd.prepare(QueryFactory().get_max_count())  # 004-開催日符号化  ■
			Cat006VRpc.prepare(QueryFactory().get_max_place_count())  # 006-開催回符号化 ■

			Cat104CWtr.prepare(df_code)  # 104-天候符号化 ■
			Cat105CTrk2.prepare()  # 105-トラック・コース周り符号化 ■
			Cat106CBct.prepare(df_code)  # 106-芝馬場状態符号化 ■
			Cat107CBcd.prepare(df_code)  # 107-ダート馬場状態符号化 ■
			Cat109CCat.prepare(df_code)  # 109-カテゴリ符号化 ■
			# Cat110CCls2.prepare(df_code) #110-競走条件コード 2歳条件符号化 ■
			# Cat111CCls3.prepare(df_code) #111-競走条件コード 3歳条件符号化 ■
			# Cat112CCls4.prepare(df_code) #112-競走条件コード 4歳条件符号化 ■
			# Cat113CCls5.prepare(df_code) #113-競走条件コード 5歳以上条件 ■
			# Cat114CClsY.prepare(df_code) #114-競走条件コード 最若年条件 ■
			Cat115CRule.prepare(df_code)  # 115-競走記号コード ■
			Cat116CRcnd.prepare(df_code)  # 116-負担重量条件符号化 ■
			Cat117BDst.prepare()  # 117-出走距離符号化 ■
			Cat118CClsT.prepare(df_code)  # 118-競走条件コード 最大条件
			Cat119BHcnt.prepare()  # 119-出走頭数符号化 ■
			Cat120CGrd.prepare(df_code)  # 120-グレード■
			Cat205BHn.prepare()  # 205-馬番符号化 ■
			Cat206BRnk.prepare()  # 206-着順符号化 ■
			Cat207CFrm.prepare()  # 207-枠符号化 ■
			Cat209CBlink.prepare()  # 209-ブリンカー符号化 ■
			Cat210BOld.prepare()  # 210-年齢符号化 ■
			Cat211CSex.prepare(df_code)  # 211-性別符号化 ■
			Cat215CJmrk.prepare(df_code)  # 215-騎手見習コード■
			Cat217CDiff.prepare(df_code)  # 217-着差コード1■
			Cat218CDiff.prepare(df_code)  # 218-着差コード2■
			Cat219CDiff.prepare(df_code)  # 219-着差コード3■
			Cat222CPm.prepare()  # 222-馬体重+-符号化 ■
			Cat223BGal.prepare()  # 223-馬体重増減符号化 ■
			Cat226BVote.prepare()  # 226-人気符号化 ■
			Cat227BCnr.prepare()  # 227-第一コーナー符号化■
			Cat228BCnr.prepare()  # 228-第二コーナー符号化■
			Cat229BCnr.prepare()  # 229-第三コーナー符号化■
			Cat230BCnr.prepare()  # 230-第四コーナー符号化■
			Cat231CHsgn.prepare(df_code)  # 231-馬記号コード■
			Cat232CVt.prepare(df_code)  # 232-品種コード■
			Cat233CBlng.prepare(df_code)  # 233-東西所属コード符号化■
			Cat262BRcnt.prepare()  # 262-出走数符号化 ■
			Cat267VYD.prepare()  # 267-経過年符号化
			Cat268CErr.prepare(df_code)  # 268-異常区分コード
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')

	@staticmethod
	def to_onehot(input):
		ret = None
		try:
			output = pd.Series()

			for i in range(len(CategoryManager4._cat_current_list)):
				cat = CategoryManager4._cat_current_list[i]
				output = cat.to_onehot(input, output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_onehot_dedicated(input):
		ret = None
		try:
			output = pd.Series()
			cat_list = copy.deepcopy(CategoryManager4._cat_current_list)
			cat_list.remove(Cat001CPlc)
			cat_list.remove(Cat003VMnt2)		
			cat_list.remove(Cat105CTrk2)
			cat_list.remove(Cat117BDst)
			cat_list.remove(Cat118CClsT)
			cat_list.remove(Cat120CGrd)
			cat_list.remove(Cat215CJmrk)
	
			
			for i in range(len(cat_list)):
				cat = cat_list[i]
				output = cat.to_onehot(input, output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_cats_direct(input):
		ret = None
		try:
			ret = pd.Series()
			dic = {}
			for i in range(len(CategoryManager4._cat_current_list)):
				cat = CategoryManager4._cat_current_list[i]

				try:
					dic[cat.KEYS] = input[cat.KEYS]
				except Exception as e:
					dic[cat.KEYS] = 0
			ret = pd.Series(dic)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros():
		ret = None
		try:
			output = pd.Series()

			for i in range(len(CategoryManager4._cat_current_list)):
				cat = CategoryManager4._cat_current_list[i]
				output = cat.create_zeros(output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_onehot_of_history(input):
		ret = None
		try:

			output = pd.Series()
			for i in range(len(CategoryManager4._cat_history_list)):
				cat = CategoryManager4._cat_history_list[i]
				output = cat.to_onehot(input, output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_cats_direct_of_history(input):
		ret = None
		try:
			ret = pd.Series()
			dic = {}
			for i in range(len(CategoryManager4._cat_history_list)):
				cat = CategoryManager4._cat_history_list[i]
				try:
					dic[cat.KEYS] = input[cat.KEYS]
				except Exception as e:
					dic[cat.KEYS] = 0
			ret = pd.Series(dic)
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def create_zeros_of_history():
		ret = None
		try:
			output = pd.Series()

			for i in range(len(CategoryManager4._cat_history_list)):
				cat = CategoryManager4._cat_history_list[i]
				output = cat.create_zeros(output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
		return ret
	# 符号化

	@staticmethod
	def to_cats(input):
		ret = pd.Series()
		try:
			ret[Cat001CPlc.KEYS] = Cat001CPlc.to_cats(
				input[Cat001CPlc.KEYS])  # 001-開催場符号化
			ret[Cat002VYear.KEYS] = Cat002VYear.to_cats(
				input[Cat002VYear.KEYS])  # 002-開催年符号化
			ret[Cat003VMnt2.KEYS] = Cat003VMnt2.to_cats(
				input[Cat003VMnt2.KEYS])  # 003-開催月符号化
			ret[Cat004VEvtd.KEYS] = Cat004VEvtd.to_cats(
				input[Cat004VEvtd.KEYS])  # 004-開催日符号化
			ret[Cat006VRpc.KEYS] = Cat006VRpc.to_cats(
				input[Cat006VRpc.KEYS])  # 006-開催回符号化

			ret[Cat104CWtr.KEYS] = Cat104CWtr.to_cats(
				input[Cat104CWtr.KEYS])  # 104-天候符号化
			ret[Cat105CTrk2.KEYS] = Cat105CTrk2.to_cats(
				input[Cat105CTrk2.KEYS])  # 105-コース周り

			ret[Cat106CBct.KEYS] = Cat106CBct.to_cats(
				input[Cat106CBct.KEYS])  # 106-芝馬場符号化
			ret[Cat107CBcd.KEYS] = Cat107CBcd.to_cats(
				input[Cat107CBcd.KEYS])  # 107-ダート馬場符号化
			ret[Cat109CCat.KEYS] = Cat109CCat.to_cats(
				input[Cat109CCat.KEYS])  # 109-カテゴリ符号化
			ret[Cat110CCls2.KEYS] = Cat110CCls2.to_cats(
				input[Cat110CCls2.KEYS])  # 110-競走条件コード 2歳条件符号化
			ret[Cat111CCls3.KEYS] = Cat111CCls3.to_cats(
				input[Cat111CCls3.KEYS])  # 111-競走条件コード 3歳条件符号化
			ret[Cat112CCls4.KEYS] = Cat112CCls4.to_cats(
				input[Cat112CCls4.KEYS])  # 112-競走条件コード 4歳条件符号化
			ret[Cat113CCls5.KEYS] = Cat113CCls5.to_cats(
				input[Cat113CCls5.KEYS])  # 113-競走条件コード 5歳以上条件
			ret[Cat114CClsY.KEYS] = Cat114CClsY.to_cats(
				input[Cat114CClsY.KEYS])  # 114-競走条件コード 最若年条件
			ret[Cat115CRule.KEYS] = Cat115CRule.to_cats(
				input[Cat115CRule.KEYS])  # 115-競走記号コード
			ret[Cat116CRcnd.KEYS] = Cat116CRcnd.to_cats(
				input[Cat116CRcnd.KEYS])  # 116-負担重量条件符号化
			ret[Cat117BDst.KEYS] = Cat117BDst.to_cats(
				input[Cat117BDst.KEYS])  # 117-出走距離符号化
			# ret[Cat118CClsT.KEYS] = Cat118CClsT.to_cats(input[Cat118CClsT.KEYS])	#118-競走条件コード 最大条件
			ret[Cat119BHcnt.KEYS] = Cat119BHcnt.to_cats(
				input[Cat119BHcnt.KEYS])  # 119-出走頭数符号化
			ret[Cat120CGrd.KEYS] = Cat120CGrd.to_cats(
				input[Cat120CGrd.KEYS])  # 120-グレード

			ret[Cat205BHn.KEYS] = Cat205BHn.to_cats(input[Cat205BHn.KEYS])  # 205-馬番
			ret[Cat206BRnk.KEYS] = Cat206BRnk.to_cats(
				input[Cat206BRnk.KEYS])  # 206-着順符号化
			ret[Cat207CFrm.KEYS] = Cat207CFrm.to_cats(
				input[Cat207CFrm.KEYS])  # 207-枠符号化
			ret[Cat209CBlink.KEYS] = Cat209CBlink.to_cats(
				input[Cat209CBlink.KEYS])  # 209-ブリンカー
			ret[Cat210BOld.KEYS] = Cat210BOld.to_cats(
				input[Cat210BOld.KEYS])  # 210-年齢符号化
			ret[Cat211CSex.KEYS] = Cat211CSex.to_cats(
				input[Cat211CSex.KEYS])  # 211-性別符号化
			ret[Cat215CJmrk.KEYS] = Cat215CJmrk.to_cats(
				input[Cat215CJmrk.KEYS])  # 215-ジョッキー符号化
			ret[Cat217CDiff.KEYS] = Cat217CDiff.to_cats(
				input[Cat217CDiff.KEYS])  # 217-着差コード1
			ret[Cat218CDiff.KEYS] = Cat218CDiff.to_cats(
				input[Cat218CDiff.KEYS])  # 218-着差コード2
			ret[Cat219CDiff.KEYS] = Cat219CDiff.to_cats(
				input[Cat219CDiff.KEYS])  # 219-着差コード3
			ret[Cat222CPm.KEYS] = Cat222CPm.to_cats(input[Cat222CPm.KEYS])  # 222-+-符号化
			ret[Cat223BGal.KEYS] = Cat223BGal.to_cats(
				input[Cat223BGal.KEYS])  # 223-馬体重増減符号化
			ret[Cat226BVote.KEYS] = Cat226BVote.to_cats(
				input[Cat226BVote.KEYS])  # 226-人気符号化
			ret[Cat227BCnr.KEYS] = Cat227BCnr.to_cats(
				input[Cat227BCnr.KEYS])  # 227-第一コーナー符号化
			ret[Cat228BCnr.KEYS] = Cat228BCnr.to_cats(
				input[Cat228BCnr.KEYS])  # 228-第二コーナー符号化
			ret[Cat229BCnr.KEYS] = Cat229BCnr.to_cats(
				input[Cat229BCnr.KEYS])  # 229-第三コーナー符号化
			ret[Cat230BCnr.KEYS] = Cat230BCnr.to_cats(
				input[Cat230BCnr.KEYS])  # 230-第四コーナー符号化
			ret[Cat231CHsgn.KEYS] = Cat231CHsgn.to_cats(
				input[Cat231CHsgn.KEYS])  # 231-馬記号コード
			ret[Cat232CVt.KEYS] = Cat232CVt.to_cats(input[Cat232CVt.KEYS])  # 232-品種コード
			ret[Cat233CBlng.KEYS] = Cat233CBlng.to_cats(
				input[Cat233CBlng.KEYS])  # 233-東西所属コード符号化

			ret[Cat262BRcnt.KEYS] = Cat262BRcnt.to_cats(
				input[Cat262BRcnt.KEYS])  # 262-出走数符号化
			ret[Cat268CErr.KEYS] = Cat268CErr.to_cats(
				input[Cat268CErr.KEYS])  # 232-品種コード
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret

	@staticmethod
	def to_cats_hot(input):
		ret = pd.Series()
		try:
			ret[Cat104CWtr.KEYS] = Cat104CWtr.to_cats(
				input[Cat104CWtr.KEYS])  # 104-天候符号化
			ret[Cat106CBct.KEYS] = Cat106CBct.to_cats(
				input[Cat106CBct.KEYS])  # 106-芝馬場符号化
			ret[Cat107CBcd.KEYS] = Cat107CBcd.to_cats(
				input[Cat107CBcd.KEYS])  # 107-ダート馬場符号化
			ret[Cat222CPm.KEYS] = Cat222CPm.to_cats(input[Cat222CPm.KEYS])  # 222-+-符号化
			ret[Cat223BGal.KEYS] = Cat223BGal.to_cats(
				input[Cat223BGal.KEYS])  # 223-馬体重増減符号化
			ret[Cat226BVote.KEYS] = Cat226BVote.to_cats(
				input[Cat226BVote.KEYS])  # 226-人気符号化

		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret
		
	@staticmethod
	def to_onehot_hot(input):
		ret = None
		try:
			output = pd.Series()

			for i in range(len(CategoryManager4._cat_hot_list)):
				cat = CategoryManager4._cat_hot_list[i]
				output = cat.to_onehot(input, output)
				if (output is None):
					break
			ret = output
		except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')
		return ret