
KJDB_MDB_FILE =  r"C:\Dev\Kjvan\kjdb.accdb"
KJDB_PREDICT_MDB_FILE =  r"C:\Dev\Kjvan\kjdb_predictor_variable_{0}.accdb"
KJDB_PREDICT_CAHCE_MDB_FILE =  r"C:\Dev\Kjvan\kjdb_prediction_cache_{0}.accdb"
KJDB_SCORE_MDB_FILE =  r"C:\Dev\Kjvan\kjdb_score.accdb"
KJDB_MASTER_MDB_FILE =  r"C:\Dev\Kjvan\kjdb_master.accdb"
KJDB_COMMENT_FILE =  r"C:\Dev\Kjvan\kjdb_comment.accdb"
KJDB_PREDICT_VALUE_MDB_FILE =  r"C:\Dev\Kjvan\kjdb_predict_value.accdb"
KJDB_PREDICT_RESULT_MDB_FILE =  r"C:\Dev\Kjvan\kjdb_predict.accdb"
KJDB_TEMP_MDB_FILE =  r"C:\Dev\Kjvan\kjtemp.accdb"
KJDB_TEMP_KJVAN_MDB_FILE =  r"C:\Dev\Kjvan\kjvan_mdb.accdb"
KJDB_TEMP_TE = 'C:\Dev\Kjvan\kjdb_te_temp.accdb'
KJDB_PREDICT_CACHE_MDB_FILE =  r"C:\Dev\Kjvan\kjdb_prediction_cache_{0}.accdb"
KJDB_PREDICT_SCORE_MDB_FILE = r"C:\Dev\Kjvan\kjdb_predict_score.accdb"
KJDB_LINEAGE_COUPLE_MDB_FILE = r"C:\Dev\Kjvan\kjdb_lineage_couple.accdb"
#KJDB_LINEAGE2_MDB_FILE = r"C:\Dev\Kjvan\kjdb_lineage2.accdb"
KJDB_LINEAGE_PAC_MDB_FILE = r"C:\Dev\Kjvan\kjdb_lineage_parent_child.accdb"



JRA_VAN_CODE_TABLE = "C:\Dev\Kjvan\Config\CodeTable.csv"
ACTIVE_DUTY_FILE = "ActiveDutyYear.txt"

KJDB_PICKLES_FOLDER= "C:\Dev\Kjvan\pickles"
BLOODS_PREDICT_MODEL = r"C:\Dev\Kjvan\Models\bloods_mul_model.pkl"

HASH256_COLUMNS_PATH = r'C:\Dev\py2\hash256_columns.csv'                           

LGBM_MODEL_PWTDWC_PATH = r'C:\Dev\py2\model\predict\models\lgbm_pwtdwc.pkl'
LGBM_MODEL_COMP_PWTDWC_PATH_AT = r'C:\Dev\py2\model\predict\models\lgbm_comp_mul_{0}_{1}_pwtdwc.pkl'
LGBM_MODEL_COMP_PWTDWC_PATH_AT2 = r'C:\Dev\py2\model\predict\models\lgbm_comp_mul_{0}_{1}_{2}_pwtdwc.pkl'
GNN_MODEL_LINEAGE_AT = r'C:\dev\Kjvan\gnn\lineage\best_model_{0}_{1}_{2}.pth'
GNN_MODEL_LINEAGE_AT2 = r'C:\dev\Kjvan\gnn\lineage\best_model_{0}.pth'
MLP_MODEL_LINEAGE_AT = r'C:\dev\Kjvan\mlp\lineage\best_model_{0}.pth'

LGBM_MODEL_COMP_PWTDWC_PATH = r'C:\Dev\py2\model\predict\models\lgbm_comp_mul_{0}_pwtdwc.pkl'
CACHE_HISTORY_PATH = r"C:\temp\pv_cache\{0}.pkl"
CACHE_HISTORY_COLUMNS_PATH = r"C:\temp\pv_cache\columns.pkl"
CACHE_CONF_TE_BPD_LIST_PATH =  r"C:\Dev\py2\model\conf\CacheConf\te_bpd_list.pkl"
CACHE_CONF_TE_BD_LIST_PATH =  r"C:\Dev\py2\model\conf\CacheConf\te_bd_list.pkl"
CACHE_CONF_TE_C_LIST_PATH =  r"C:\Dev\py2\model\conf\CacheConf\te_c_list.pkl"

TREES_TRAIN_SP_PATH_AT2 = r"C:\temp\tree_train_mul_sp_{0}.csv"
TREES_TRAIN_PTD_PATH_AT2 = r"C:\temp\trees_train_mul_{0}_{1}_{2}.csv"

LGBM_MODEL_PTD_PATH_AT2 = r"C:\Dev\Kjvan\tree_models\lgbm\lgbm_mul_{0}_{1}_{2}_ptd.pkl"
CAT_MODEL_PTD_PATH_AT2 = r"C:\Dev\Kjvan\tree_models\catboost\cat_mul_{0}_{1}_{2}_ptd.pkl"

LGBM_MODEL_SP_PATH_AT = r"C:\Dev\Kjvan\tree_models\lgbm\lgbm_comp_mul_sp_{0}.pkl"
CAT_MODEL_SP_PATH_AT = r"C:\Dev\Kjvan\tree_models\catboost\cat_comp_mul_sp_{0}.pkl"


DEFAULT_VALU_PAHT = r'C:\Dev\py2\default_value.csv'

WA_WIN_ACG_FILE = r'C:\Dev\py2\model\conf\cache_win_avg.txt'
WA_MUL_ACG_FILE = r'C:\Dev\py2\model\conf\cache_mul_avg.txt'
#出力ファイルベースフォルダ
BASE_DIR1 = "G:\\マイドライブ\\Kjvan\\"
#BASE_DIR1 = "C:\\Temp\\Kjvan\\"
SUB_HOT_PATH="hot\\"
SUB_COLD_PATH="cld\\"
SUB_STATIC_PATH="stc\\"

#グラフパス
GRAPH_PARAM_FOLDER = BASE_DIR1+SUB_COLD_PATH+"G"
#グラフパス
GRAPH2_PARAM_FOLDER = BASE_DIR1+SUB_COLD_PATH+"F"
#出走情報
CURRENT_RACING_FOLDER = BASE_DIR1+SUB_HOT_PATH+"A"
#出走情報パラメータパス
HORSE_HISTORY_FOLDER = BASE_DIR1+SUB_COLD_PATH+"B"
#前４レースサマリ
HORSE_SUMMARY_FOLDER = BASE_DIR1+SUB_COLD_PATH+"E"
#ハロンパラメータパス
HORSE_HARON_FOLDER = BASE_DIR1+SUB_COLD_PATH+"I"
#予想
PREDICT_PRECISION_PARAM_FOLDER = BASE_DIR1+SUB_HOT_PATH+"H"
PREDICT_ROUGTH_PARAM_FOLDER = BASE_DIR1+SUB_HOT_PATH+"HR"
PREDICT_ROUGTH_PARAM_FOLDER2 = BASE_DIR1+SUB_HOT_PATH+"HR2"
PREDICT_LINEAGE_PARAM_FOLDER = BASE_DIR1+SUB_HOT_PATH+"HG"
#作業用
TEMP_PARAM_FOLDER = BASE_DIR1+SUB_STATIC_PATH+"T"

ATTR_PARAM_FOLDER = BASE_DIR1+SUB_STATIC_PATH+"D"

COMMENT_FILE_FOLDER = BASE_DIR1+SUB_COLD_PATH+"N"

#コース情報
COURSE_FEATURE_FOLDER = BASE_DIR1+SUB_STATIC_PATH+"C"

#過去４レースパス
PREDICT_BASE_DATA_FOLDER = BASE_DIR1+SUB_COLD_PATH+"J"

#マイニング
PREDICT_LGBM_BASE_DATA_FOLDER = BASE_DIR1+SUB_HOT_PATH+"K"



#学習済みパラメータファイルフォルダ
NNC_MODELS_FOLDER= r"C:\Dev\Kjvan\nnc_models"
NNC_MODELS_PLACE_AND_CLASS_FOLDER= r"C:\Dev\Kjvan\nnc_models\place_and_class"
TRAIN_FILE_PATH= r"c:\temp\train"


#Jra van 2001コードグルーピング
code_group_2001_value=[
	"01",
	"02",
	"03",
	"04",
	"05",
	"06",
	"07",
	"08",
	"09",
	"10",
	"11",
	"12",
]
code_group_2001={
	"00":"12",
	"01":"01",
	"02":"02",
	"03":"03",
	"04":"04",
	"05":"05",
	"06":"06",
	"07":"07",
	"08":"08",
	"09":"09",
	"10":"10",
	"30":"11",
	"31":"11",
	"32":"11",
	"33":"11",
	"34":"11",
	"35":"11",
	"36":"11",
	"37":"11",
	"38":"11",
	"39":"11",
	"40":"11",
	"41":"11",
	"42":"11",
	"43":"11",
	"44":"11",
	"45":"11",
	"46":"11",
	"47":"11",
	"48":"11",
	"49":"11",
	"50":"11",
	"51":"11",
	"52":"11",
	"53":"11",
	"54":"11",
	"55":"11",
	"56":"11",
	"57":"11",
	"58":"11",
	"59":"11",
	"60":"11",
	"61":"11",
	"A0":"12",
	"A2":"12",
	"A4":"12",
	"A6":"12",
	"A8":"12",
	"B0":"12",
	"B2":"12",
	"B4":"12",
	"B6":"12",
	"B8":"12",
	"C0":"12",
	"C2":"12",
	"C4":"12",
	"C5":"12",
	"C6":"12",
	"C7":"12",
	"C8":"12",
	"D0":"12",
	"D2":"12",
	"D4":"12",
	"D6":"12",
	"D8":"12",
	"E0":"12",
	"E2":"12",
	"E4":"12",
	"E6":"12",
	"E8":"12",
	"F0":"12",
	"F1":"12",
	"F2":"12",
	"F4":"12",
	"F6":"12",
	"F8":"12",
	"G0":"12",
	"G2":"12",
	"G4":"12",
	"G6":"12",
	"G8":"12",
	"H0":"12",
	"H2":"12",
	"H4":"12",
	"H6":"12",
	"H8":"12",
	"I0":"12",
	"I2":"12",
	"I4":"12",
	"I6":"12",
	"I8":"12",
	"J0":"12",
	"J2":"12",
	"J4":"12",
	"J6":"12",
	"J8":"12",
	"K0":"12",
	"K2":"12",
	"K4":"12",
	"K6":"12",
	"K8":"12",
	"L0":"12",
	"L2":"12",
	"L4":"12",
	"L6":"12",
	"L8":"12",
	"M0":"12",
	"M2":"12",
	"M4":"12",
	"M6":"12",
	"M8":"12",
		
}


#Jra van 2007コードグルーピング
code_group_2007_value=[
	"00",	#なし
	"01",	#新馬
	"02",	#未勝利
	"03",	#500万
	"04",	#1000万
	"05",	#1600万
	"06",	#オープン
]
code_group_2007={
	"000":"00",
	"001":"03",
	"002":"03",
	"003":"03",
	"004":"03",
	"005":"03",
	"006":"04",
	"007":"04",
	"008":"04",
	"009":"04",
	"010":"04",
	"011":"05",
	"012":"05",
	"013":"05",
	"014":"05",
	"015":"05",
	"016":"05",
	"017":"05",
	"018":"05",
	"019":"05",
	"020":"05",
	"021":"05",
	"022":"05",
	"023":"05",
	"024":"05",
	"025":"05",
	"026":"05",
	"027":"05",
	"028":"05",
	"029":"05",
	"030":"05",
	"031":"05",
	"032":"05",
	"033":"05",
	"034":"05",
	"035":"05",
	"036":"05",
	"037":"05",
	"038":"05",
	"039":"05",
	"040":"05",
	"041":"05",
	"042":"05",
	"043":"05",
	"044":"05",
	"045":"05",
	"046":"05",
	"047":"05",
	"048":"05",
	"049":"05",
	"050":"05",
	"051":"05",
	"052":"05",
	"053":"05",
	"054":"05",
	"055":"05",
	"056":"05",
	"057":"05",
	"058":"05",
	"059":"05",
	"060":"05",
	"061":"05",
	"062":"05",
	"063":"05",
	"064":"05",
	"065":"05",
	"066":"05",
	"067":"05",
	"068":"05",
	"069":"05",
	"070":"05",
	"071":"05",
	"072":"05",
	"073":"05",
	"074":"05",
	"075":"05",
	"076":"05",
	"077":"05",
	"078":"05",
	"079":"05",
	"080":"05",
	"081":"05",
	"082":"05",
	"083":"05",
	"084":"05",
	"085":"05",
	"086":"05",
	"087":"05",
	"088":"05",
	"089":"05",
	"090":"05",
	"091":"05",
	"092":"05",
	"093":"05",
	"094":"05",
	"095":"05",
	"096":"05",
	"097":"05",
	"098":"05",
	"099":"05",
	"100":"05",
	"701":"01",
	"702":"01",
	"703":"02",
	"999":"06"
	}

code_group_2007_index={
	"000":0,
	"001":3,
	"002":3,
	"003":3,
	"004":3,
	"005":3,
	"006":4,
	"007":4,
	"008":4,
	"009":4,
	"010":4,
	"011":5,
	"012":5,
	"013":5,
	"014":5,
	"015":5,
	"016":5,
	"017":5,
	"018":5,
	"019":5,
	"020":5,
	"021":5,
	"022":5,
	"023":5,
	"024":5,
	"025":5,
	"026":5,
	"027":5,
	"028":5,
	"029":5,
	"030":5,
	"031":5,
	"032":5,
	"033":5,
	"034":5,
	"035":5,
	"036":5,
	"037":5,
	"038":5,
	"039":5,
	"040":5,
	"041":5,
	"042":5,
	"043":5,
	"044":5,
	"045":5,
	"046":5,
	"047":5,
	"048":5,
	"049":5,
	"050":5,
	"051":5,
	"052":5,
	"053":5,
	"054":5,
	"055":5,
	"056":5,
	"057":5,
	"058":5,
	"059":5,
	"060":5,
	"061":5,
	"062":5,
	"063":5,
	"064":5,
	"065":5,
	"066":5,
	"067":5,
	"068":5,
	"069":5,
	"070":5,
	"071":5,
	"072":5,
	"073":5,
	"074":5,
	"075":5,
	"076":5,
	"077":5,
	"078":5,
	"079":5,
	"080":5,
	"081":5,
	"082":5,
	"083":5,
	"084":5,
	"085":5,
	"086":5,
	"087":5,
	"088":5,
	"089":5,
	"090":5,
	"091":5,
	"092":5,
	"093":5,
	"094":5,
	"095":5,
	"096":5,
	"097":5,
	"098":5,
	"099":5,
	"100":5,
	"701":1,
	"702":1,
	"703":2,
	"999":6
	}


code_group_2007_summary_index={
	'000000000000000':'00',
	'000000000000703':'02',
	'000000000000999':'06',
	'000000000999999':'06',
	'000000005005005':'03',
	'000000005010005':'03',
	'000000009018009':'04',
	'000000010010010':'04',
	'000000010020010':'04',
	'000000016016016':'05',
	'000000016032016':'05',
	'000000703703703':'02',
	'000000999000999':'06',
	'000000999999999':'06',
	'000005000000005':'03',
	'000005005005005':'03',
	'000005010010005':'03',
	'000009000000009':'04',
	'000009018018009':'04',
	'000010000000010':'04',
	'000010010010010':'04',
	'000010020020010':'04',
	'000016016016016':'05',
	'000016032032016':'05',
	'000701000000701':'01',
	'000702000000702':'02',
	'000703000000703':'02',
	'000703703703703':'02',
	'000999000000999':'06',
	'000999999999999':'06',
	'005000000000005':'03',
	'701000000000701':'01',
	'703000000000703':'02',
	'999000000000999':'06',
	'999999999999999':'06',
}
code_group_2007_softmax_index={
	1:25, #新馬
	2:20, #未勝利
	3:15, #500万
	4:10, #1000万
 	5:5,  #1600万
	6:0,  #OPEN
}
