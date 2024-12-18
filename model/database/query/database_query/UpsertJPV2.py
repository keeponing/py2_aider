# プログラムヘッダ
import sys
import os
import inspect
sys.path.append(r"C:\Dev\py2")
import model.conf.KJraConst as const
import model.utility.k_jra_util as util
from model.features.onehot_encoding.current.Cat001CPlc import Cat001CPlc
from model.features.onehot_encoding.current.Cat002VYear import Cat002VYear
from model.features.onehot_encoding.current.Cat003VMnt2 import Cat003VMnt2
from model.features.onehot_encoding.current.Cat004VEvtd import Cat004VEvtd
from model.features.onehot_encoding.current.Cat006VRpc import Cat006VRpc

from model.features.onehot_encoding.current.Cat104CWtr import Cat104CWtr
from model.features.onehot_encoding.current.Cat105CTrk2 import Cat105CTrk2
from model.features.onehot_encoding.current.Cat106CBct import Cat106CBct
from model.features.onehot_encoding.current.Cat107CBcd import Cat107CBcd
from model.features.onehot_encoding.current.Cat109CCat import Cat109CCat
from model.features.onehot_encoding.current.Cat110CCls2 import Cat110CCls2
from model.features.onehot_encoding.current.Cat111CCls3 import Cat111CCls3
from model.features.onehot_encoding.current.Cat112CCls4 import Cat112CCls4
from model.features.onehot_encoding.current.Cat113CCls5 import Cat113CCls5
from model.features.onehot_encoding.current.Cat114CClsY import Cat114CClsY
from model.features.onehot_encoding.current.Cat115CRule import Cat115CRule
from model.features.onehot_encoding.current.Cat116CRcnd import Cat116CRcnd
from model.features.onehot_encoding.current.Cat117BDst import Cat117BDst

from model.features.onehot_encoding.current.Cat119BHcnt import Cat119BHcnt
from model.features.onehot_encoding.current.Cat120CGrd import Cat120CGrd

from model.features.onehot_encoding.current.Cat205BHn import Cat205BHn
from model.features.onehot_encoding.current.Cat206BRnk import Cat206BRnk
from model.features.onehot_encoding.current.Cat207CFrm import Cat207CFrm
from model.features.onehot_encoding.current.Cat209CBlink import Cat209CBlink
from model.features.onehot_encoding.current.Cat210BOld import Cat210BOld
from model.features.onehot_encoding.current.Cat211CSex import Cat211CSex
from model.features.onehot_encoding.current.Cat215CJmrk import Cat215CJmrk
from model.features.onehot_encoding.current.Cat217CDiff import Cat217CDiff
from model.features.onehot_encoding.current.Cat218CDiff import Cat218CDiff 
from model.features.onehot_encoding.current.Cat219CDiff import Cat219CDiff 
from model.features.onehot_encoding.current.Cat222CPm import Cat222CPm
from model.features.onehot_encoding.current.Cat223BGal import Cat223BGal
from model.features.onehot_encoding.current.Cat226BVote import Cat226BVote
from model.features.onehot_encoding.current.Cat227BCnr import Cat227BCnr
from model.features.onehot_encoding.current.Cat228BCnr import Cat228BCnr
from model.features.onehot_encoding.current.Cat229BCnr import Cat229BCnr
from model.features.onehot_encoding.current.Cat230BCnr import Cat230BCnr
from model.features.onehot_encoding.current.Cat231CHsgn import Cat231CHsgn
from model.features.onehot_encoding.current.Cat232CVt import Cat232CVt
from model.features.onehot_encoding.current.Cat233CBlng import Cat233CBlng


#TODO 234
#from model.features.onehot_encoding.current.Cat241CJblng import Cat241CJblng

from model.features.onehot_encoding.current.Cat262BRcnt import Cat262BRcnt
from model.features.onehot_encoding.current.Cat268CErr import Cat268CErr

def upsert(accessor, te):

	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
					key_program_id='{1}' 
				and 
					key_horse_id='{2}'
		"""
		cmd = template.format(const.TBL_KJDB_PREDICT_CACHE_VALIABLE, 
			te['key_program_id'],
			te['key_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count: 
			template = """
					insert into {0} 
					( 
						key_program_id,
						key_horse_id,
						desc_horse_no,
						obj_rank,
						cats_plc,
						cats_year,
						cats_mnt,
						cats_evtd,
						cats_rpc,
						cats_wtr,
						cats_bct,
						cats_bcd,
						cats_cat,
						cats_cls2,
						cats_cls3,
						cats_cls4,
						cats_cls5,
						cats_clsy,
						cats_rule,
						cats_rcnd,
						cats_dst,
						cats_hcnt,
						cats_grd,
						cats_hn,
						cats_rnk,
						cats_frm,
						cats_blink,
						cats_old,
						cats_sex,
						cats_jmk,
						cats_diff1,
						cats_diff2,
						cats_diff3,
						cats_pm,
						cats_gal,
						cats_vote,
						cats_cnr1,
						cats_cnr2,
						cats_cnr3,
						cats_cnr4,
						cats_hsgn,
						cats_vt,
						cats_blng,
						cats_rcnt,
						cats_err,
						cats_trk2,
						upd
					) values (
						 '{1}', '{2}',  {3} ,  {4} ,  {5} ,  {6} ,  {7} ,  {8} ,  {9} , {10} ,
						 {11} , {12} , {13} , {14} , {15} , {16} , {17} , {18} , {19} , {20} ,
						 {21} , {22} , {23} , {24} , {25} , {26} , {27} , {28} , {29} , {30} ,
						 {31} , {32} , {33} , {34} , {35} , {36} , {37} , {38} , {39} , {40} ,
						 {41} , {42} , {43} , {44} , {45} ,'{46}', {47}  
					)
					"""

		else:
			# CAT-ADD：★KJDB
			template = """
					update {0} 
					set 
						desc_horse_no={3}
						, obj_rank={4}
						, cats_plc={5}
						, cats_year={6}
						, cats_mnt={7}
						, cats_evtd={8}
						, cats_rpc={9}
						, cats_wtr={10}
						, cats_bct={11}
						, cats_bcd={12}
						, cats_cat={13}
						, cats_cls2={14}
						, cats_cls3={15}
						, cats_cls4={16}
						, cats_cls5={17}
						, cats_clsy={18}
						, cats_rule={19}
						, cats_rcnd={20}
						, cats_dst={21}
						, cats_hcnt={22}
						, cats_grd={23}
						, cats_hn={24}
						, cats_rnk={25}
						, cats_frm={26}
						, cats_blink={27}
						, cats_old={28}
						, cats_sex={29}
						, cats_jmk={30}
						, cats_diff1={31}
						, cats_diff2={32}
						, cats_diff3={33}
						, cats_pm={34}
						, cats_gal={35}
						, cats_vote={36}
						, cats_cnr1={37}
						, cats_cnr2={38}
						, cats_cnr3={39}
						, cats_cnr4={40}
						, cats_hsgn={41}
						, cats_vt={42}
						, cats_blng={43}
						, cats_rcnt={44}
						, cats_err={45}
						, cats_trk2={46}
						, upd={47}
					where 
							key_program_id='{1}'
						and 
							key_horse_id='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(  
			const.TBL_KJDB_PREDICT_CACHE_VALIABLE, 
			te['key_program_id'], #01 
			te['key_horse_id'], #02 
			te['desc_horse_no'], #03
			te['obj_rank'], #04
			te[Cat001CPlc.KEYS], #05
			te[Cat002VYear.KEYS], #06
			te[Cat003VMnt2.KEYS],#07
			te[Cat004VEvtd.KEYS],#08	
			te[Cat006VRpc.KEYS],#09
			te[Cat104CWtr.KEYS], #10
			te[Cat106CBct.KEYS],#12
			te[Cat107CBcd.KEYS],#13
			te[Cat109CCat.KEYS],#14
			te[Cat110CCls2.KEYS],	#15
			te[Cat111CCls3.KEYS],	#16
			te[Cat112CCls4.KEYS],	#17
			te[Cat113CCls5.KEYS],	#18
			te[Cat114CClsY.KEYS],	#19
			te[Cat115CRule.KEYS],	#20
			te[Cat116CRcnd.KEYS],   #21
			te[Cat117BDst.KEYS],#22
			te[Cat119BHcnt.KEYS],#23
			te[Cat120CGrd.KEYS],#24
			te[Cat205BHn.KEYS],#25
			te[Cat206BRnk.KEYS],#26
			te[Cat207CFrm.KEYS],#27
			te[Cat209CBlink.KEYS],#28
			te[Cat210BOld.KEYS],#29
			te[Cat211CSex.KEYS], #30	
			te[Cat215CJmrk.KEYS] ,#31
			te[Cat217CDiff.KEYS],#32
			te[Cat218CDiff.KEYS],#33
			te[Cat219CDiff.KEYS],#34
			te[Cat222CPm.KEYS],#35
			te[Cat223BGal.KEYS],#36
			te[Cat226BVote.KEYS], #37
			te[Cat227BCnr.KEYS], #38
			te[Cat228BCnr.KEYS], #39
			te[Cat229BCnr.KEYS], #40
			te[Cat230BCnr.KEYS], #41
			te[Cat231CHsgn.KEYS], #42
			te[Cat232CVt.KEYS], #43
			te[Cat233CBlng.KEYS], #44
			te[Cat262BRcnt.KEYS],#45
			te[Cat268CErr.KEYS],#46
			te[Cat105CTrk2.KEYS],#47
			1 #48
			)
		accessor.execute(cmd)
		accessor.commit()
	 #   accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	


def update_hot(accessor, te):
	try:
		template = """
			select 
				count(*) 
			from 
				{0}  
			where 
					key_program_id='{1}' 
				and 
					key_horse_id='{2}'
		"""
		cmd = template.format(const.TBL_KJDB_PREDICT_CACHE_VALIABLE, 
			te['key_program_id'],
			te['key_horse_id']
			)
		accessor.execute(cmd)

		count =0
		for c in accessor.cur.fetchall():
			count = int(c[0])
			break	  
		if 0 ==  count: 
			i=0
			#Nothing to do...
		else:
			# CAT-ADD：★KJDB
			template = """
					update {0} 
					set 
						cats_wtr={3}
						, cats_bct={4}
						, cats_bcd={5}
						, cats_pm={6}
						, cats_gal={7}
						, cats_vote={8}
					where 
							key_program_id='{1}'
						and 
							key_horse_id='{2}'
					"""
		accessor.cur_close()
		cmd = template.format(  
			const.TBL_KJDB_PREDICT_CACHE_VALIABLE, #0
			te['key_program_id'], #1 
			te['key_horse_id'], #2 
			te[Cat104CWtr.KEYS], #3
			te[Cat106CBct.KEYS],#4
			te[Cat107CBcd.KEYS],#5
			te[Cat222CPm.KEYS],#6
			te[Cat223BGal.KEYS],#7
			te[Cat226BVote.KEYS]#8
			)
		accessor.execute(cmd)
		accessor.commit()
	 #   accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
