import csv
from collections import OrderedDict
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
#import plotly.plotly as py




def anlyse_mc_s1_s2(csv_file):
	file = open(csv_file, "r")
	reader = csv.DictReader(file)

	giant_dict = {'190':{}, '191':{}, '264':{}, '265':{}, '263':{}, '266':{}}
	students = {}
	total_tries_took_s1 = {'190':0, '191':0, '264':0, '265':0, '263':0, '266':0}
	total_tries_took_s2 = {'191':0, '265':0, '266':0}
	data_dict = {}
	g1_number = 0
	g2_number = 0
	g3_number = 0

	for orderdict in reader:
		row = dict(orderdict)
		sid = row['studentID']
		pid = row['problemID']
		time = row['date']
		s1_num_of_tries = 0	
		s2_num_of_tries = 0
		s1_already_correct = False
		s2_already_correct = False

		if sid not in giant_dict[pid]: #get the initial submit
			giant_dict[pid][sid] = [s1_num_of_tries, s2_num_of_tries, 
			 						s1_already_correct, s2_already_correct, time, 
									row['op1correct (t/f)'], row['op2correct (t/f)'], 
									row['op3correct (t/f)'], row['op4correct (t/f)'], 
									row['op5correct (t/f)'], row['op6correct (t/f)']]
			giant_dict[pid][sid][0] += 1
			giant_dict[pid][sid][1] += 1

		elif giant_dict[pid][sid][2] == False:
			giant_dict[pid][sid][4:] = [time, row['op1correct (t/f)'], row['op2correct (t/f)'], 
										 row['op3correct (t/f)'], row['op4correct (t/f)'], 
										 row['op5correct (t/f)'], row['op6correct (t/f)']]
			giant_dict[pid][sid][0] += 1
			if giant_dict[pid][sid][3] == False:
				giant_dict[pid][sid][1] += 1


		if 'f' not in (giant_dict[pid][sid][5], giant_dict[pid][sid][7], 
					   giant_dict[pid][sid][8], giant_dict[pid][sid][10]):
			giant_dict[pid][sid][3] = True
			if 'f' not in (giant_dict[pid][sid][6], giant_dict[pid][sid][9]):
				giant_dict[pid][sid][2] = True


		if sid not in students:
			if pid == '190' or pid == '191':	
				students[sid]='1'
				g1_number += 1

			elif pid == '265' or pid == '264':	
				students[sid]='2'
				g2_number += 1

			elif pid == '263' or pid == '266':	
				students[sid]='3'
				g3_number += 1

			data_dict[sid] = [students[sid], '', '', '']


		if pid in ['190','264','263']: 
			data_dict[sid][1] = giant_dict[pid][sid][0]
		else:
			data_dict[sid][2] = giant_dict[pid][sid][0]
			data_dict[sid][3] = giant_dict[pid][sid][1]

	for pid in giant_dict:	
		for sid in giant_dict[pid]:
			total_tries_took_s1[pid] += giant_dict[pid][sid][0]
			if pid in ['191','265','266']:
				total_tries_took_s2[pid] += giant_dict[pid][sid][1]

	return data_dict





def anlyse_sa_s1(csv_file):
	file = open(csv_file, "r")
	reader = csv.DictReader(file)

	giant_dict = {'29':{}, '30':{}, '31':{}, '32':{},                  #group_1
				  '36':{}, '38':{}, '42':{}, '45':{}, '33':{},         #group_2
				  '37':{}, '39':{}, '43':{}, '44':{}, '35':{}}         #group_3
	students = {}
	total_tries_took = {'29':0, '30':0, '31':0, '32':0,
						'36':0, '38':0, '42':0, '45':0, '33':0,
						'37':0, '39':0, '43':0, '44':0, '35':0}
	data_dict = {}
	g1_number = 0
	g2_number = 0
	g3_number = 0

	for orderdict in reader:
		row = dict(orderdict)
		sid = row['user']
		pid = row['problem_id']
		time = row['date']
		score = int(row['score'])
		num_of_tries = 0
		already_correct = False


		if sid not in giant_dict[pid]: #get the initial submit
			giant_dict[pid][sid] = [num_of_tries, already_correct, score, time, row['submission']]
			giant_dict[pid][sid][0] += 1

		elif giant_dict[pid][sid][1] == False:
			giant_dict[pid][sid][3:] = [time, row['submission']]		
			giant_dict[pid][sid][0] += 1

		if score == 1:
			giant_dict[pid][sid][1] = True

		if sid not in students:
			if pid in ['29','30','31','32'] :	
				students[sid]='group_001'
				g1_number += 1

			elif pid in ['36','38','42','45','33']:	
				students[sid]='group_002'
				g2_number += 1

			elif pid in ['37','39','43','44','35']:	
				students[sid]='group_003'
				g3_number += 1

			data_dict[sid] = [students[sid], '', '', '', '', '']

		if pid in ['29','36','37']: 
			data_dict[sid][1] = giant_dict[pid][sid][0]
		elif pid in ['30','38','39']: 
			data_dict[sid][2] = giant_dict[pid][sid][0]		
		elif pid in ['31','42','43']: 
			data_dict[sid][3] = giant_dict[pid][sid][0]		
		elif pid in ['32','45','44']: 
			data_dict[sid][4] = giant_dict[pid][sid][0]		
		else:
			data_dict[sid][5] = giant_dict[pid][sid][0]

	for pid in giant_dict:	
		for sid in giant_dict[pid]:
			total_tries_took[pid] += giant_dict[pid][sid][0]

	return data_dict


def merge_dictionaries(data_dict_mc_s1_s2, data_dict_sa_s1):

	giant_dict = defaultdict(list)
	dicts = [data_dict_mc_s1_s2, data_dict_sa_s1]	
	
	for dict in dicts:
		for k, v in dict.items():
			giant_dict[k].append(v)

	return giant_dict





def write_output(csv_output, giant_dict):

	file = open(csv_output, "w")
	writer = csv.DictWriter(file, fieldnames = ['SID','GID','s1_pre1','s1_post',
												's2_post','s1_pre2_1','s1_pre2_2',
												's1_pre2_3','s1_pre2_4','s1_pre2_5'])
	writer.writeheader()

	for sid, info in giant_dict.items():
		try:
			writer.writerow({'SID': sid, 'GID': info[0][0],
							 's1_pre1': info[0][1],'s1_post': info[0][2],
							 's2_post': info[0][3],'s1_pre2_1': info[0][1],
							 's1_pre2_2': info[1][2],'s1_pre2_3': info[1][3],
							 's1_pre2_4': info[1][2],'s1_pre2_5': info[1][5]})
		except IndexError:
   			pass





if __name__ == "__main__":

	mc_file = './week9/mc_data.csv'
	sa_file = './week9/short_answer_data.csv'
	data_dict_mc_s1_s2 = anlyse_mc_s1_s2(mc_file)
	data_dict_sa_s1 = anlyse_sa_s1(sa_file)
	csv_output = './w9_output.csv'
	giant_dict = merge_dictionaries(data_dict_mc_s1_s2, data_dict_sa_s1)
	write_output(csv_output, giant_dict)









