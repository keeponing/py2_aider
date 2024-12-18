from numpy import empty
import pyodbc
import model.conf.KJraConst as const
import pandas as pd


def get_record_to_sr_by_y_hid(accessor,ys,horse_id):
	ret = pd.DataFrame()
	
	for element in ys.values:
		y = element[0]
		cmd = f"""
			SELECT 
				TargetEncodingVariables_{y}.*, 
				PredictorVariables_{y}.*, 
				StatisticsVariables_{y}.*
			FROM 
				(
					TargetEncodingVariables_{y} LEFT JOIN 
					PredictorVariables_{y} ON 
					(
						TargetEncodingVariables_{y}.te_horse_id = PredictorVariables_{y}.key_horse_id
					) 
					AND (
						TargetEncodingVariables_{y}.te_id = PredictorVariables_{y}.key_program_id
					)
					
				) 
				LEFT JOIN StatisticsVariables_{y} ON 
				(
					PredictorVariables_{y}.key_horse_id = StatisticsVariables_{y}.sv_horse_id
				) 
				AND 
				(
					PredictorVariables_{y}.key_program_id = StatisticsVariables_{y}.sv_program_id
				)
			WHERE
				sv_horse_id='{horse_id}'
			"""
		
		df_temp = accessor.read_sql_to_df(cmd)
		if(len(df_temp)):
			ret =pd.concat([ret, df_temp])
	return ret


def get_record_to_sr(accessor, program_id, horse_id):
	ret = pd.Series()
	y = program_id[:4]
	if('0000'!= y):
		cmd = f"""
			SELECT 
				TargetEncodingVariables_{y}.*, 
				PredictorVariables_{y}.*, 
				StatisticsVariables_{y}.*
			FROM 
				(
					TargetEncodingVariables_{y} INNER JOIN 
					PredictorVariables_{y} ON 
					(
						TargetEncodingVariables_{y}.te_horse_id = PredictorVariables_{y}.key_horse_id
					) 
					AND (
						TargetEncodingVariables_{y}.te_id = PredictorVariables_{y}.key_program_id
					)
					
				) 
				INNER JOIN StatisticsVariables_{y} ON 
				(
					PredictorVariables_{y}.key_horse_id = StatisticsVariables_{y}.sv_horse_id
				) 
				AND 
				(
					PredictorVariables_{y}.key_program_id = StatisticsVariables_{y}.sv_program_id
				)
			WHERE
				sv_program_id = '{program_id}'
				AND 
				sv_horse_id='{horse_id}'
			"""
		
		df_temp = accessor.read_sql_to_df(cmd)
		if(len(df_temp)):
			ret = df_temp.iloc[0]
	return ret


