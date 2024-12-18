# プログラムヘッダ
import sys
import os
import inspect
sys.path.append(r"C:\Dev\py2")
import model.conf.KJraConst as const
import model.utility.k_jra_util as util


def upsert(accessor, te):

	try:
		template = """
			select 
				count(*) 
			from 
				{0} 
			where 
				te_horse_id='{1}'
		"""
		cmd = template.format(const.TBL_KJDB_TE_CACHE_VALIABLE, 
			te.get('te_horse_id')
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
						te_horse_id,
						te_D0714,
						te_D1418,
						te_D1823,
						te_D2330,
						te_D30OV,
						te_T0714,
						te_T1418,
						te_T1823,
						te_T2330,
						te_T30OV,
						te_09T1823,
						te_07D2330,
						te_07T1418,
						te_05T1418,
						te_06T1418,
						te_99D1418,
						te_06D2330,
						te_99T1418,
						te_08T1823,
						te_02T2330,
						te_02D2330,
						te_10D1418,
						te_09T0714,
						te_03D1418,
						te_99T1823,
						te_10T30OV,
						te_05T1823,
						te_09D0714,
						te_09T2330,
						te_01D0714,
						te_10D2330,
						te_05D1418,
						te_05D1823,
						te_10D0714,
						te_03T2330,
						te_08D0714,
						te_06T2330,
						te_03T1418,
						te_99T0714,
						te_08T0714,
						te_05T0714,
						te_99T30OV,
						te_02T1823,
						te_01T1823,
						te_07T0714,
						te_02T0714,
						te_09D1418,
						te_06T30OV,
						te_08T2330,
						te_09D1823,
						te_99D2330,
						te_10T2330,
						te_06T1823,
						te_09T1418,
						te_03T0714,
						te_03D2330,
						te_06D0714,
						te_99D0714,
						te_07D1418,
						te_03D0714,
						te_07T2330,
						te_99D30OV,
						te_04D2330,
						te_07T30OV,
						te_06T0714,
						te_08D1823,
						te_04T30OV,
						te_06D1418,
						te_07D0714,
						te_01D2330,
						te_02D1418,
						te_04D1418,
						te_01T1418,
						te_03T1823,
						te_08D1418,
						te_01D1418,
						te_04T1823,
						te_10T1418,
						te_01T2330,
						te_05D0714,
						te_07T1823,
						te_04T2330,
						te_99D1823,
						te_02D0714,
						te_10T0714,
						te_04D0714,
						te_08T30OV,
						te_04T1418,
						te_02T1418,
						te_03T30OV,
						te_08T1418,
						te_07D1823,
						te_99T2330,
						te_04T0714,
						te_09T30OV,
						te_01T0714,
						te_10T1823,
						te_05T30OV,
						te_05T2330,
						te_05D2330,
						te_000000000000000,
						te_000000000000703,
						te_000000000000999,
						te_000000000999999,
						te_000000005005005,
						te_000000005010005,
						te_000000009018009,
						te_000000010010010,
						te_000000010020010,
						te_000000016016016,
						te_000000016032016,
						te_000000703703703,
						te_000000999000999,
						te_000000999999999,
						te_000005000000005,
						te_000005005005005,
						te_000005010010005,
						te_000009000000009,
						te_000009018018009,
						te_000010000000010,
						te_000010010010010,
						te_000010020020010,
						te_000016016016016,
						te_000016032032016,
						te_000701000000701,
						te_000702000000702,
						te_000703000000703,
						te_000703703703703,
						te_000999000000999,
						te_000999999999999,
						te_005000000000005,
						te_701000000000701,
						te_703000000000703,
						te_999000000000999,
						te_C2_00,
						te_C2_01,
						te_C2_02,
						te_C2_03,
						te_C2_04,
						te_C2_05,
						te_C2_06,
						te_bpdjy,
						te_bpdsy,
						te_bpdty,
						te_bpds,
						time_upd
					) values (
						 '{1}',  {2},   {3},   {4} ,  {5} ,  {6} ,  {7} ,  {8} ,  {9} , {10} ,
						 {11} , {12} , {13} , {14} , {15} , {16} , {17} , {18} , {19} , {20} ,
						 {21} , {22} , {23} , {24} , {25} , {26} , {27} , {28} , {29} , {30} ,
						 {31} , {32} , {33} , {34} , {35} , {36} , {37} , {38} , {39} , {40} ,
						 {41} , {42} , {43} , {44} , {45} ,'{46}', {47} , {48} , {49} , {50} , 
						 {51} , {52} , {53} ,'{54}', {55} , {56} , {57} , {58} , {59} , {60} , 
						 {61} , {62} , {63} , {64} ,'{65}', {66} , {67} , {68} , {69} , {70} ,		 
						 {71} , {72} , {73} , {74} , {75} , {76} , {77} , {78} , {79} , {80} ,															
						 {81} , {82} , {83} , {84} , {85} , {86} , {87} , {88} , {89} , {90} ,															
						 {91} , {92} , {93} , {94} , {95} , {96} , {97} , {98} , {99} ,{100} ,
						 {101} ,{102}, {103}, {104}, {105}, {106}, {107}, {108}, {109},{110} ,
						 {111} ,{112}, {113}, {114}, {115}, {116}, {117}, {118}, {119},{120} ,
						 {121} ,{122}, {123}, {124}, {125}, {126}, {127}, {128}, {129},{130} ,
					 	 {131} ,{132}, {133}, {134}, {135}, {136}, {137}, {138}, {139},{140} ,
						 {141} ,{142} ,{143} ,{144} ,{145} ,{146}, '{147}'
						)
					"""
			accessor.cur_close()
			cmd = template.format(  
				const.TBL_KJDB_TE_CACHE_VALIABLE,  #0
				# te.get('te_id'), #1
				# te.get('te_race'), #2 
				te.get('te_horse_id'), #3
				te.get('te_D0714',0), #4
				te.get('te_D1418',0),#5
				te.get('te_D1823',0),#6
				te.get('te_D2330',0),#7
				te.get('te_D30OV',0),#8
				te.get('te_T0714',0),#9
				te.get('te_T1418',0),#10
				te.get('te_T1823',0),#11
				te.get('te_T2330',0),#12
				te.get('te_T30OV',0),#13
				te.get('te_09T1823',0),#14
				te.get('te_07D2330',0),#15
				te.get('te_07T1418',0),#16
				te.get('te_05T1418',0),#17
				te.get('te_06T1418',0),#18
				te.get('te_99D1418',0),#19
				te.get('te_06D2330',0),#20
				te.get('te_99T1418',0),#21
				te.get('te_08T1823',0),#22
				te.get('te_02T2330',0),#23
				te.get('te_02D2330',0),#24
				te.get('te_10D1418',0),#25
				te.get('te_09T0714',0),#26
				te.get('te_03D1418',0),#27
				te.get('te_99T1823',0),#28
				te.get('te_10T30OV',0),#28
				te.get('te_05T1823',0),#30
				te.get('te_09D0714',0),#31
				te.get('te_09T2330',0),#32
				te.get('te_01D0714',0),#33
				te.get('te_10D2330',0),#34
				te.get('te_05D1418',0),#35
				te.get('te_05D1823',0),#36
				te.get('te_10D0714',0),#37
				te.get('te_03T2330',0),#38
				te.get('te_08D0714',0),#39
				te.get('te_06T2330',0),#40
				te.get('te_03T1418',0),#41
				te.get('te_99T0714',0),#42
				te.get('te_08T0714',0),#43
				te.get('te_05T0714',0),#44
				te.get('te_99T30OV',0),#45
				te.get('te_02T1823',0),#46
				te.get('te_01T1823',0),#47
				te.get('te_07T0714',0),#48
				te.get('te_02T0714',0),#49
				te.get('te_09D1418',0),#50
				te.get('te_06T30OV',0),#51
				te.get('te_08T2330',0),#52
				te.get('te_09D1823',0),#53
				te.get('te_99D2330',0),#54
				te.get('te_10T2330',0),#55
				te.get('te_06T1823',0),#56
				te.get('te_09T1418',0),#57
				te.get('te_03T0714',0),#58
				te.get('te_03D2330',0),#59
				te.get('te_06D0714',0),#60
				te.get('te_99D0714',0),#61
				te.get('te_07D1418',0),#62
				te.get('te_03D0714',0),#63
				te.get('te_07T2330',0),#64
				te.get('te_99D30OV',0),#65
				te.get('te_04D2330',0),#66
				te.get('te_07T30OV',0),#67
				te.get('te_06T0714',0),#68
				te.get('te_08D1823',0),#69
				te.get('te_04T30OV',0),#70
				te.get('te_06D1418',0),#71
				te.get('te_07D0714',0),#72
				te.get('te_01D2330',0),#73
				te.get('te_02D1418',0),#74
				te.get('te_04D1418',0),#75
				te.get('te_01T1418',0),#76
				te.get('te_03T1823',0),#77
				te.get('te_08D1418',0),#78
				te.get('te_01D1418',0),#79
				te.get('te_04T1823',0),#80
				te.get('te_10T1418',0),#81
				te.get('te_01T2330',0),#82
				te.get('te_05D0714',0),#83
				te.get('te_07T1823',0),#84
				te.get('te_04T2330',0),#85
				te.get('te_99D1823',0),#86
				te.get('te_02D0714',0),#87
				te.get('te_10T0714',0),#88
				te.get('te_04D0714',0),#89
				te.get('te_08T30OV',0),#90
				te.get('te_04T1418',0),#91
				te.get('te_02T1418',0),#92
				te.get('te_03T30OV',0),#93
				te.get('te_08T1418',0),#94
				te.get('te_07D1823',0),#95
				te.get('te_99T2330',0),#96
				te.get('te_04T0714',0),#97
				te.get('te_09T30OV',0),#98
				te.get('te_01T0714',0),#99
				te.get('te_10T1823',0),#100
				te.get('te_05T30OV',0),#101
				te.get('te_05T2330',0),#102
				te.get('te_05D2330',0),#103
				te.get('te_000000000000000',0),#104
				te.get('te_000000000000703',0),#105
				te.get('te_000000000000999',0),#106
				te.get('te_000000000999999',0),#107
				te.get('te_000000005005005',0),#108
				te.get('te_000000005010005',0),#109
				te.get('te_000000009018009',0),#110
				te.get('te_000000010010010',0),#111
				te.get('te_000000010020010',0),#112
				te.get('te_000000016016016',0),#113
				te.get('te_000000016032016',0),#114
				te.get('te_000000703703703',0),#115
				te.get('te_000000999000999',0),#116
				te.get('te_000000999999999',0),#117
				te.get('te_000005000000005',0),#118
				te.get('te_000005005005005',0),#119
				te.get('te_000005010010005',0),#120
				te.get('te_000009000000009',0),#121
				te.get('te_000009018018009',0),#122
				te.get('te_000010000000010',0),#123
				te.get('te_000010010010010',0),#124
				te.get('te_000010020020010',0),#125
				te.get('te_000016016016016',0),#126
				te.get('te_000016032032016',0),#127
				te.get('te_000701000000701',0),#128
				te.get('te_000702000000702',0),#129
				te.get('te_000703000000703',0),#130
				te.get('te_000703703703703',0),#131
				te.get('te_000999000000999',0),#132
				te.get('te_000999999999999',0),#133
				te.get('te_005000000000005',0),#134
				te.get('te_701000000000701',0),#135
				te.get('te_703000000000703',0),#136
				te.get('te_999000000000999',0),#137
				te.get('te_C2_00',0),#138
				te.get('te_C2_01',0),#139
				te.get('te_C2_02',0),#140
				te.get('te_C2_03',0),#141
				te.get('te_C2_04',0),#142
				te.get('te_C2_05',0),#143
				te.get('te_C2_06',0),#144
				te.get('te_bpdjy',0),#145
				te.get('te_bpdsy',0),#146
				te.get('te_bpdty',0),#147
				te.get('te_bpds',0),#148
				te.get('time_upd',0)#148

				)
			# cmd = cmd.replace( '\n' , ' ' )
			# cmd = cmd.replace( '\t' , ' ' )	
			accessor.execute(cmd)
			accessor.commit()
		else:
			cmd = f"""
					update {const.TBL_KJDB_TE_CACHE_VALIABLE} 
					set 
						te_D0714={te.get('te_D0714',0)},
						te_D1418={te.get('te_D1418',0)},
						te_D1823={te.get('te_D1823',0)},
						te_D2330={te.get('te_D2330',0)},
						te_D30OV={te.get('te_D30OV',0)},
						te_T0714={te.get('te_T0714',0)},
						te_T1418={te.get('te_T1418',0)},
						te_T1823={te.get('te_T1823',0)},
						te_T2330={te.get('te_T2330',0)},
						te_T30OV={te.get('te_T30OV',0)},
						te_09T1823={te.get('te_09T1823',0)},
						te_07D2330={te.get('te_07D2330',0)},
						te_07T1418={te.get('te_07T1418',0)},
						te_05T1418={te.get('te_05T1418',0)},
						te_06T1418={te.get('te_06T1418',0)},
						te_99D1418={te.get('te_99D1418',0)},
						te_06D2330={te.get('te_06D2330',0)},
						te_99T1418={te.get('te_99T1418',0)},
						te_08T1823={te.get('te_08T1823',0)},
						te_02T2330={te.get('te_02T2330',0)},
						te_02D2330={te.get('te_02D2330',0)},
						te_10D1418={te.get('te_10D1418',0)},
						te_09T0714={te.get('te_09T0714',0)},
						te_03D1418={te.get('te_03D1418',0)},
						te_99T1823={te.get('te_99T1823',0)},
						te_10T30OV={te.get('te_10T30OV',0)},
						te_05T1823={te.get('te_05T1823',0)},
						te_09D0714={te.get('te_09D0714',0)},
						te_09T2330={te.get('te_09T2330',0)},
						te_01D0714={te.get('te_01D0714',0)},
						te_10D2330={te.get('te_10D2330',0)},
						te_05D1418={te.get('te_05D1418',0)},
						te_05D1823={te.get('te_05D1823',0)},
						te_10D0714={te.get('te_10D0714',0)},
						te_03T2330={te.get('te_03T2330',0)},
						te_08D0714={te.get('te_08D0714',0)},
						te_06T2330={te.get('te_06T2330',0)},
						te_03T1418={te.get('te_03T1418',0)},
						te_99T0714={te.get('te_99T0714',0)},
						te_08T0714={te.get('te_08T0714',0)},
						te_05T0714={te.get('te_05T0714',0)},
						te_99T30OV={te.get('te_99T30OV',0)},
						te_02T1823={te.get('te_02T1823',0)},
						te_01T1823={te.get('te_01T1823',0)},
						te_07T0714={te.get('te_07T0714',0)},
						te_02T0714={te.get('te_02T0714',0)},
						te_09D1418={te.get('te_09D1418',0)},
						te_06T30OV={te.get('te_06T30OV',0)},
						te_08T2330={te.get('te_08T2330',0)},
						te_09D1823={te.get('te_09D1823',0)},
						te_99D2330={te.get('te_99D2330',0)},
						te_10T2330={te.get('te_10T2330',0)},
						te_06T1823={te.get('te_06T1823',0)},
						te_09T1418={te.get('te_09T1418',0)},
						te_03T0714={te.get('te_03T0714',0)},
						te_03D2330={te.get('te_03D2330',0)},
						te_06D0714={te.get('te_06D0714',0)},
						te_99D0714={te.get('te_99D0714',0)},
						te_07D1418={te.get('te_07D1418',0)},
						te_03D0714={te.get('te_03D0714',0)},
						te_07T2330={te.get('te_07T2330',0)},
						te_99D30OV={te.get('te_99D30OV',0)},
						te_04D2330={te.get('te_04D2330',0)},
						te_07T30OV={te.get('te_07T30OV',0)},
						te_06T0714={te.get('te_06T0714',0)},
						te_08D1823={te.get('te_08D1823',0)},
						te_04T30OV={te.get('te_04T30OV',0)},
						te_06D1418={te.get('te_06D1418',0)},
						te_07D0714={te.get('te_07D0714',0)},
						te_01D2330={te.get('te_01D2330',0)},
						te_02D1418={te.get('te_02D1418',0)},
						te_04D1418={te.get('te_04D1418',0)},
						te_01T1418={te.get('te_01T1418',0)},
						te_03T1823={te.get('te_03T1823',0)},
						te_08D1418={te.get('te_08D1418',0)},
						te_01D1418={te.get('te_01D1418',0)},
						te_04T1823={te.get('te_04T1823',0)},
						te_10T1418={te.get('te_10T1418',0)},
						te_01T2330={te.get('te_01T2330',0)},
						te_05D0714={te.get('te_05D0714',0)},
						te_07T1823={te.get('te_07T1823',0)},
						te_04T2330={te.get('te_04T2330',0)},
						te_99D1823={te.get('te_99D1823',0)},
						te_02D0714={te.get('te_02D0714',0)},
						te_10T0714={te.get('te_10T0714',0)},
						te_04D0714={te.get('te_04D0714',0)},
						te_08T30OV={te.get('te_08T30OV',0)},
						te_04T1418={te.get('te_04T1418',0)},
						te_02T1418={te.get('te_02T1418',0)},
						te_03T30OV={te.get('te_03T30OV',0)},
						te_08T1418={te.get('te_08T1418',0)},
						te_07D1823={te.get('te_07D1823',0)},
						te_99T2330={te.get('te_99T2330',0)},
						te_04T0714={te.get('te_04T0714',0)},
						te_09T30OV={te.get('te_09T30OV',0)},
						te_01T0714={te.get('te_01T0714',0)},
						te_10T1823={te.get('te_10T1823',0)},
						te_05T30OV={te.get('te_05T30OV',0)},
						te_05T2330={te.get('te_05T2330',0)},
						te_05D2330={te.get('te_05D2330',0)}
					where 
						te_horse_id='{te.get('te_horse_id',0)}'
					"""
			accessor.cur_close()
			cmd = cmd.replace( '\n' , ' ' )
			cmd = cmd.replace( '\t' , ' ' )	
			accessor.execute(cmd)
			accessor.commit()
			cmd = f"""
					update {const.TBL_KJDB_TE_CACHE_VALIABLE} 
					set 
					te_000000000000000={te.get('te_000000000000000',0)},
					te_000000000000703={te.get('te_000000000000703',0)},
					te_000000000000999={te.get('te_000000000000999',0)},
					te_000000000999999={te.get('te_000000000999999',0)},
					te_000000005005005={te.get('te_000000005005005',0)},
					te_000000005010005={te.get('te_000000005010005',0)},
					te_000000009018009={te.get('te_000000009018009',0)},
					te_000000010010010={te.get('te_000000010010010',0)},
					te_000000010020010={te.get('te_000000010020010',0)},
					te_000000016016016={te.get('te_000000016016016',0)},
					te_000000016032016={te.get('te_000000016032016',0)},
					te_000000703703703={te.get('te_000000703703703',0)},
					te_000000999000999={te.get('te_000000999000999',0)},
					te_000000999999999={te.get('te_000000999999999',0)},
					te_000005000000005={te.get('te_000005000000005',0)},
					te_000005005005005={te.get('te_000005005005005',0)},
					te_000005010010005={te.get('te_000005010010005',0)},
					te_000009000000009={te.get('te_000009000000009',0)},
					te_000009018018009={te.get('te_000009018018009',0)},
					te_000010000000010={te.get('te_000010000000010',0)},
					te_000010010010010={te.get('te_000010010010010',0)},
					te_000010020020010={te.get('te_000010020020010',0)},
					te_000016016016016={te.get('te_000016016016016',0)},
					te_000016032032016={te.get('te_000016032032016',0)},
					te_000701000000701={te.get('te_000701000000701',0)},
					te_000702000000702={te.get('te_000702000000702',0)},
					te_000703000000703={te.get('te_000703000000703',0)},
					te_000703703703703={te.get('te_000703703703703',0)},
					te_000999000000999={te.get('te_000999000000999',0)},
					te_000999999999999={te.get('te_000999999999999',0)},
					te_005000000000005={te.get('te_005000000000005',0)},
					te_701000000000701={te.get('te_701000000000701',0)},
					te_703000000000703={te.get('te_703000000000703',0)},
					te_999000000000999={te.get('te_999000000000999',0)},
					te_C2_00={te.get('te_C2_00',0)},
					te_C2_01={te.get('te_C2_01',0)},
					te_C2_02={te.get('te_C2_02',0)},
					te_C2_03={te.get('te_C2_03',0)},
					te_C2_04={te.get('te_C2_04',0)},
					te_C2_05={te.get('te_C2_05',0)},
					te_C2_06={te.get('te_C2_06',0)},
					te_bpdjy={te.get('te_bpdjy',0)},
					te_bpdsy={te.get('te_bpdsy',0)},
					te_bpdty={te.get('te_bpdty',0)},
					te_bpds={te.get('te_bpds',0)},
					time_upd='{te.get('time_upd',0)}'
					where 
						te_horse_id='{te.get('te_horse_id',0)}'
					"""
			# cmd = cmd.replace( '\n' , ' ' )
			# cmd = cmd.replace( '\t' , ' ' )	
			accessor.execute(cmd)
			accessor.commit()
	 #   accessor.cur_close()
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	



