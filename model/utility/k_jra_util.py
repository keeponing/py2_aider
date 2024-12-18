#ユーティリティ
import datetime
import math
import numpy as np
import pandas as pd
import model.conf.KJraConst as const
import warnings
import csv
warnings.simplefilter('ignore')
import os
import inspect
import model.conf.KJraConfig as conf
from sklearn.preprocessing import LabelEncoder
import hashlib
#Smooth radio Features
def smooth_radio_features(value, value_count, value_average):
    alpha =0.1
    temp=-alpha*value_count
    return (1-np.exp(temp)*value+np.exp(temp)*value_average)

def pickup_year_range(args):
	today = datetime.date.today()
	year = today.year
 
	if(len(args)==2):
		args.append(year+1)
		args.append(1)   
	if(len(args)==3):
		args.append(1)
	if(len(args)<=1):
		args.append(year)
		args.append(year+1)
		args.append(1)
	
	start = int(args[1])	
	stop = int(args[2])
 
	if(stop < start):
		args[3] = -1
	return int(args[1]), int(args[2]), int(args[3])

def softmax(x):
    u = np.sum(np.exp(x))
    return np.exp(x)/u

def sigmoid(x, gain=-1.5):
	try:
		#return 1 / (1 + math.exp(-x))
		return 1 / (1+ math.exp(-(gain*x)))
	except Exception as e:
		return 0
def sigmoid_gain_custom(x):
	try:
		#return 1 / (1 + math.exp(-x))
		return (1 / (1+ math.exp(-(4*(x-0.5)))))
	except Exception as e:
		return 0
# 'MSSmi'形式の文字列を秒に変換する
def conv_str_time_to_float(input): 
	min = int(input[0])
	sec = int(input[1:3])
	ms = int(input[3])
	return min*60+sec+ms/10.0

# 'SSmi'形式の文字列を秒に変換する
def conv_str_3f_time_to_float(input): 
	sec = int(input[0:2])
	ms = int(input[2])
	return sec+ms/10.0

# 'DDDD'形式の文字列を秒に変換する
def conv_str_distance_to_int(input): 
	distance = int(input)
	return distance

#　'MSSmi'形式の文字列の偏差値を計算する。
def calc_str_time_deviation(input, avg, std): 
	ret = .0
	if(input!='0000'):
		if((std != 0.0) and (avg != None) and (std != None)):
			temp = conv_str_time_to_float(input)
			ret = (temp - avg)/std
	return sigmoid(ret)

#　'SSmi'形式の文字列の偏差値を計算する。
def calc_str_3f_time_deviation(input, avg, std): 
	ret = .0
	temp=input
	input = input if(input > '300') else '380'
	if(temp!='000'):
		if((std != 0.0) and (avg != None) and (std != None)):
			temp = conv_str_3f_time_to_float(input)
			ret = (temp - avg)/std
	return sigmoid(ret)

# 平均距離を計算する
def calc_str_avg_distance(df): 
	ret = .0
	if(0 != len(df)):
		df_dist = df.apply(conv_str_distance_to_int)
		ret = df_dist.mean()
	return ret

#距離の差を求める
def calc_str_distance_diff(dist1, dist2): 
	ret = 0
	#どちらか0なら差なしとする。
	if( 0 != dist1 and 0 != dist1):
		ret = conv_str_distance_to_int(dist1) - conv_str_distance_to_int(dist2)
	return ret

def percent(value, min, max):
	ret =.0
	if(min!=max):
		ret = (value - min)/(max-min)
		if(ret < 0 ):ret=0.0
		if(1 < ret):ret=1.0
	return ret

#外れ値クリッピング
def trim_outlier(input, min, max):
	ret =min
	val = float(input)
	if(val < min): 
		ret=min
	elif(max < val): 
		ret=max
	else:
		ret=val
	return ret

def create_class_color4():
	#https://stackoverflow.com/questions/46173419/seaborn-change-bar-colour-according-to-hue-name
	ret ={
		'000':"#AAAAAA",  #未設定・未整備
		'A000':"#AAAAAA",  #未設定・未整備
		'B000':"#AAAAAA",  #未設定・未整備
		'C000':"#AAAAAA",  #未設定・未整備
		'D000':"#AAAAAA",  #未設定・未整備
		'E000':"#AAAAAA",  #未設定・未整備
		'F000':"#AAAAAA",  #未設定・未整備
		'G000':"#AAAAAA",  #未設定・未整備
		'H000':"#AAAAAA",  #未設定・未整備
		'L000':"#AAAAAA",  #未設定・未整備
		'999':"#A8A8FF", # オープン
		'D999':"#A8A8FF", # オープン
		'E999':"#A8A8FF", # オープン
		'L999':"#A8A8FF", # オープン
		'701':"#C8FFC8",  #新馬
		'702':"#C8FFC8",  #未出走
		'703':"#90FF90",  # 未勝利  
		'001':"#FFF090",  #500万円以下
		'002':"#FFF090",  #500万円以下
		'003':"#FFF090",  #500万円以下
		'004':"#FFF090",  #500万円以下
		'005':"#FFF090",  #500万円以下
		'E005':"#FFF090",  #500万円以下
		'006':"#FFC820",  #900万円以下
		'007':"#FFC820",  #900万円以下
		'008':"#FFC820",  #900万円以下
		'009':"#FFC820",  #900万円以下
		'010':"#FFC820",  #1000万円以下
		'E010':"#FFC820",  #1000万円以下
		'011':"#F09060",  #1600万円以下
		'012':"#F09060",  #1600万円以下
		'013':"#F09060",  #1600万円以下
		'014':"#F09060",  #1600万円以下
		'015':"#F09060",  #1600万円以下
		'016':"#F09060",  #1600万円以下
		'E016':"#F09060",  #1600万円以下
		'017':"#F09060",  #1600万円以下
		'018':"#F09060",  #1600万円以下
		'019':"#F09060",  #1600万円以下
		'020':"#F09060",  #1600万円以下
		'021':"#F09060",  #1600万円以下
		'022':"#F09060",  #1600万円以下
		'023':"#F09060",  #1600万円以下
		'024':"#F09060",  #1600万円以下
		'025':"#F09060",  #1600万円以下
		'026':"#F09060",  #1600万円以下
		'027':"#F09060",  #1600万円以下
		'028':"#F09060",  #1600万円以下
		'029':"#F09060",  #1600万円以下
		'030':"#F09060",  #1600万円以下
		'031':"#F09060",  #1600万円以下
		'032':"#F09060",  #1600万円以下
		'033':"#F09060",  #1600万円以下
		'034':"#F09060",  #1600万円以下
		'035':"#F09060",  #1600万円以下
		'036':"#F09060",  #1600万円以下
		'037':"#F09060",  #1600万円以下
		'038':"#F09060",  #1600万円以下
		'039':"#F09060",  #1600万円以下
		'040':"#F09060",  #1600万円以下
		'041':"#F09060",  #1600万円以下
		'042':"#F09060",  #1600万円以下
		'043':"#F09060",  #1600万円以下
		'044':"#F09060",  #1600万円以下
		'045':"#F09060",  #1600万円以下
		'046':"#F09060",  #1600万円以下
		'047':"#F09060",  #1600万円以下
		'048':"#F09060",  #1600万円以下
		'049':"#F09060",  #1600万円以下
		'050':"#F09060",  #1600万円以下
		'051':"#F09060",  #1600万円以下
		'052':"#F09060",  #1600万円以下
		'053':"#F09060",  #1600万円以下
		'054':"#F09060",  #1600万円以下
		'055':"#F09060",  #1600万円以下
		'056':"#F09060",  #1600万円以下
		'057':"#F09060",  #1600万円以下
		'058':"#F09060",  #1600万円以下
		'059':"#F09060",  #1600万円以下
		'060':"#F09060",  #1600万円以下
		'061':"#F09060",  #1600万円以下
		'062':"#F09060",  #1600万円以下
		'063':"#F09060",  #1600万円以下
		'064':"#F09060",  #1600万円以下
		'065':"#F09060",  #1600万円以下
		'066':"#F09060",  #1600万円以下
		'067':"#F09060",  #1600万円以下
		'068':"#F09060",  #1600万円以下
		'069':"#F09060",  #1600万円以下
		'070':"#F09060",  #1600万円以下
		'071':"#F09060",  #1600万円以下
		'072':"#F09060",  #1600万円以下
		'073':"#F09060",  #1600万円以下
		'074':"#F09060",  #1600万円以下
		'075':"#F09060",  #1600万円以下
		'076':"#F09060",  #1600万円以下
		'077':"#F09060",  #1600万円以下
		'078':"#F09060",  #1600万円以下
		'079':"#F09060",  #1600万円以下
		'080':"#F09060",  #1600万円以下
		'081':"#F09060",  #1600万円以下
		'082':"#F09060",  #1600万円以下
		'083':"#F09060",  #1600万円以下
		'084':"#F09060",  #1600万円以下
		'085':"#F09060",  #1600万円以下
		'086':"#F09060",  #1600万円以下
		'087':"#F09060",  #1600万円以下
		'088':"#F09060",  #1600万円以下
		'089':"#F09060",  #1600万円以下
		'090':"#F09060",  #1600万円以下
		'091':"#F09060",  #1600万円以下
		'092':"#F09060",  #1600万円以下
		'093':"#F09060",  #1600万円以下
		'094':"#F09060",  #1600万円以下
		'095':"#F09060",  #1600万円以下
		'096':"#F09060",  #1600万円以下
		'097':"#F09060",  #1600万円以下
		'098':"#F09060",  #1600万円以下
		'099':"#F09060",  #1600万円以下
		'100':"#F09060",  #1600万円以下
		'A999':"#FF0000", #ＧⅠ
		'F999':"#FF0000", #ＧⅠ
		'B999':"#2020FF", #ＧⅡ
		'G999':"#2020FF", #ＧⅡ
		'C999':"#A875FF", #ＧⅢ
		'H999':"#A875FF", #ＧⅢ
	 
		}
	return ret

def convert_dataframe_columns(df):
	columns = df.columns
	index=0
	ret ={}
	for col in columns:
		col2 = "x__{0}:{1}".format(index, col)
		ret[col]= col2
		index+=1
	return ret

def get_course_type(place_code, distance):
	ret ="0"
	if(place_code=="01"):
		ret=1
	elif(place_code=="02"):
		ret=1
	elif(place_code=="03"):
		ret=1
	elif(place_code=="04"):
		ret=2
	elif(place_code=="05"):
		ret=2
	elif(place_code=="06"):
		ret=1
	elif(place_code=="07"):
		ret=2
		if(distance=="1000"):
			ret=3
	elif(place_code=="08"):
		ret=1
	elif(place_code=="09"):
		ret=1
	elif(place_code=="10"):
		ret=1
	return ret

def conv_track_code_to_id(input):
	ret=0
	if(input=='10'): ret =0
	elif(input=='11'): ret =0
	elif(input=='12'): ret =0
	elif(input=='13'): ret =0
	elif(input=='14'): ret =0
	elif(input=='15'): ret =0
	elif(input=='16'): ret =0
	elif(input=='17'): ret =0
	elif(input=='18'): ret =0
	elif(input=='19'): ret =0
	elif(input=='20'): ret =0
	elif(input=='21'): ret =0
	elif(input=='22'): ret =0
	elif(input=='51'): ret =0
	elif(input=='52'): ret =0
	elif(input=='53'): ret =0
	elif(input=='54'): ret =0
	elif(input=='55'): ret =0
	elif(input=='56'): ret =0
	elif(input=='57'): ret =0
	elif(input=='58'): ret =0
	elif(input=='59'): ret =0

	if(input=='23'): ret =1
	elif(input=='24'): ret =1
	elif(input=='25'): ret =1
	elif(input=='26'): ret =1
	elif(input=='27'): ret =1
	elif(input=='28'): ret =1
	elif(input=='29'): ret =1
	return ret

#汎用カテゴリ文字列作成
def create_num_bin_category_index(bins, value):
	ret =0
	try:
	   #2000012905 1997100623
	   #2000030406 1997100342 
	   #2000032509 1997104715 
		temp = int(value)
		temp0 =[temp]
		temp1 = pd.cut(temp0, bins, labels=False)
		if(np.isnan(temp1[0]) == False) : 
			ret = int(temp1[0])
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

#汎用カテゴリ文字列作成
def create_float_bin_category_index(bins, value):
	ret =0
	try:
	   #2000012905 1997100623
	   #2000030406 1997100342 
	   #2000032509 1997104715 
		temp0 =[value]
		temp1 = pd.cut(temp0, bins, labels=False)
		if(np.isnan(temp1[0]) == False) : 
			ret = int(temp1[0])
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

def get_rank_bias(input):
	ret =25
	if(1 == input):# "00",	#新馬
		ret = 25
	elif(2 == input):# "01",	#未勝利
		ret = 20
	elif(3 == input):# "02",	#500万
		ret = 15
	elif(4 == input):# "03",	#1000万
		ret = 10
	elif(5 == input):# "04",	#1600万
		ret = 5
	# elif(5 == input):# "06",	#オープン
	# 	ret = 5
	# elif(6 == input):# "07",	#オープン
	# 	ret = 0
	elif(6 == input):# "05",	#オープン
		ret = 0
	return ret

def decide_horse_class(dt_re):
	#0-6
	c2 = int(dt_re['cats_cls2'])
	c3 = int(dt_re['cats_cls3'])
	c4 = int(dt_re['cats_cls4'])
	c5 = int(dt_re['cats_cls5'])
	cy = int(dt_re['cats_clsy'])

	ret = 5
	if(c2 != 0):
		ret = c2
	elif(c3 != 0):
		ret = c3
	elif(c4 != 0):
		ret = c4
	elif(c5 != 0):
		ret = c5
	elif(cy != 0):
		ret = cy 
	return ret  	
	
def decide_horse_class2(dt_re):
	#0-6
	c2 = int(dt_re['rh_class2'])
	c3 = int(dt_re['rh_class3'])
	c4 = int(dt_re['rh_class4'])
	c5 = int(dt_re['rh_class5over'])
	cy = int(dt_re['rh_classYoung'])

	ret = 5
	if(c2 != 0):
		ret = c2
	elif(c3 != 0):
		ret = c3
	elif(c4 != 0):
		ret = c4
	elif(c5 != 0):
		ret = c5
	elif(cy != 0):
		ret = cy 
	return ret  	

def convert_rank_to_category(df_tr, df_code):
	dt_tr = df_tr.iloc[0]
	val1 = 4
	temp = int(dt_tr['obj_rank'])
	if(1 == temp):val1=0
	elif(2 == temp):val1=1
	elif(3 == temp):val1=1
	elif(4 == temp):val1=2
	elif(5 == temp):val1=2
	elif(6 == temp):val1=2
	elif(7 == temp):val1=3
	elif(8 == temp):val1=3
	elif(9 == temp):val1=3
	elif(10 == temp):val1=3
	else:val1=4

	if(val1==0):
		i=0
	if(val1==1):
		i=0
	if(val1==2):
		i=0
	if(val1==3):
		i=0
	if(val1==4):
		i=0
	if(val1==5):
		i=0
	cls_index = decide_horse_class(dt_tr)
	val2=get_rank_bias(cls_index)
 
	# if(
	# 	(cls_index==0) or 
	# 	(cls_index==101) or 
	# 	(cls_index==102) 
	# 	):
	# 	val2=get_rank_bias(1)
	# if(cls_index==103):
	# 	val2=get_rank_bias(2)
	# if((cls_index<=1) and (5<=cls_index)): 
	# 	val2=get_rank_bias(3)
	# if((cls_index<=6) and (10<=cls_index)): 
	# 	val2=get_rank_bias(4)
	# if((cls_index<=11) and (16<=cls_index)): 
	# 	val2=get_rank_bias(5)
	# if((cls_index<=17) and (32<=cls_index)): 		 
	# 	val2=get_rank_bias(6)
	# if(
	# 	((cls_index<=33) and (99<=cls_index))
	# 	or
	# 	(cls_index==100) 
	# 	or
	# 	(cls_index==104)  
	# 	):  
	# 	val2=get_rank_bias(7)
	ret = df_tr.iloc[0].copy()
	ret['obj_rank'] = val1+val2	
	if(30<val1+val2):
		a=0
	return ret
		
def convert_rank_to_category2(sr_tr):
	#sr_tr = df_tr.iloc[0]
	val1 = 0
	temp = sr_tr['obj_rank']
	if(1 == temp):val1=1
	elif(2 == temp):val1=1
	elif(3 == temp):val1=1
	else:val1=0
	ret = sr_tr.copy()
	ret['obj_rank'] = val1
	return ret


def convert_rank_to_category9(sr_tr):
	#sr_tr = df_tr.iloc[0]
	val1 = 2
	temp = sr_tr['obj_rank']
	if(1 == temp):val1=0
	elif(2 == temp):val1=0
	elif(3 == temp):val1=0
	elif(4 == temp):val1=1
	elif(5 == temp):val1=1
	elif(6 == temp):val1=1
	else:val1=2
	#ret = sr_tr.iloc[0].copy()
	ret = sr_tr.copy()
	ret['obj_rank'] = val1
	return ret
	
def convert_rank_to_category8(input):

	val1 = 1
	temp = int(input)
	if(1 == temp):val1=0
	elif(2 == temp):val1=0
	elif(3 == temp):val1=0
	else:val1=1
	ret= val1
	return ret

def convert_rank_to_category3(df_tr, df_code):
	dt_tr = df_tr.iloc[0]
	val1 = dt_tr['obj_rank']

	ret = df_tr.iloc[0].copy()
	ret['obj_rank'] = val1-1
	return ret

def rename_index(sr, prefix):
	cols = sr.index
	dict_cols = {}
	for col in cols:
		dict_cols[col]= '{0}_{1}'.format(prefix, col)
	return sr.rename(index=dict_cols)

def rename_index2(sr, prefix):
	cols = sr.index
	dict_cols = {}
	for col in cols:
		dict_cols[col]= f'{col}_{prefix}'
	return sr.rename(index=dict_cols)	

def save_dict_keys(name, dct):
	with open(name, "w") as f:
		for key, value in dct.items():
			f.write('{}'.format(key)+"\n")
   
def convert_class_code(re):
	ret = '000'
	if(re['rh_class5over'] != '000'):
		ret = re['rh_class5over']	
	elif(re['rh_class4'] != '000'):
		ret = re['rh_class4']
	elif(re['rh_class3'] != '000'):
		ret = re['rh_class3']	
	elif(re['rh_class2'] != '000'):
		ret = re['rh_class2']	
	elif(re['rh_classYoung'] != '000'):
		ret = re['rh_classYoung']	
	ret = re['rh_grade'] + 	ret
	return ret.strip()

def convert_class_code_without_grade(re):
	ret = '000'
	if(re['rh_class5over'] != '000'):
		ret = re['rh_class5over']	
	elif(re['rh_class4'] != '000'):
		ret = re['rh_class4']
	elif(re['rh_class3'] != '000'):
		ret = re['rh_class3']	
	elif(re['rh_class2'] != '000'):
		ret = re['rh_class2']	
	elif(re['rh_classYoung'] != '000'):
		ret = re['rh_classYoung']	
	return ret	

def calc_speed_exponent(bt, rt, de, re, weight):
	ret = sigmoid_gain_custom(( (bt-rt)*de+re+(weight-55)*2+70)/100)
	return ret	

def calc_speed_3f_exponent(bt, rt, de, re, weight):
	ret = sigmoid_gain_custom(( (bt-rt)*de+re+(weight-55)*2+30)/100)
	return ret	


def convert_safe_pid(input):
	ret = input if (0 != input) else const.VOID_PID
	return ret	

def dump_span_time(co_name, span):
	print(f"{span:.2f}秒: {co_name}")
	pass

def convert_2007_index_summary(te_code):
	ret =0
	try:
		if(te_code in conf.code_group_2007_summary_index):
			ret = int(conf.code_group_2007_summary_index[te_code])
	except Exception as e:
		print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret 	

def get_default_value():
	ret = {}
	try:
		
		with open(conf.DEFAULT_VALU_PAHT, 'r', encoding="utf-8_sig") as f:
			for row in csv.DictReader(f):
				ret[row['key']] = row['value']
	except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret


def calc_rank_average(df_input):
	ret = 0.0
	try:
		max_count = const.MAX_HORSE_COUNT 
		if(len(df_input)):
			temp = df_input['rank'].mean()					
			temp = temp if(temp!=0) else max_count
			ret = (max_count - temp) /max_count	
	except Exception as e:
			print(f'{os.path.basename(__file__)}->{inspect.currentframe().f_code.co_name} {e}')	
	return ret

def dump_feature(df_feature, input_file):
	today = datetime.datetime.now() 
	t = today.time()
	ts = t.strftime('%H')
	dump_path = os.path.join(r"c:\\temp", f'{input_file}_{ts}.json')
	df_feature.to_json(dump_path)

def to_le(df_feature, cols):
	ret = pd.DataFrame()
	for col in cols:
		le = LabelEncoder()
		le.fit(df_feature[col])
		ret[col] = le.transform(df_feature[col])
	return ret

def to_sha256(sr_race, cols):
	lst=[]
	for col in cols:
		lst.append(str(sr_race[col]))
	temp = "-".join(lst)
	ret = hashlib.sha256(temp.encode())
	return ret


def get_feature_columns():
	lines = []
	filename =  conf.HASH256_COLUMNS_PATH
	with open(filename, 'r') as f:
		lines = f.readlines()
	ret = [line.strip() for line in lines]
	return ret