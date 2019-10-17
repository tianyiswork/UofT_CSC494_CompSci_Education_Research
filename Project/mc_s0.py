import csv
from collections import OrderedDict



def anlyse_mc_s0(csv_file):
	file = open(csv_file, "r")
	reader = csv.DictReader(file)

	giant_dict = {'190':{}, '191':{}, '264':{}, '265':{}, '263':{}, '266':{}}
	students = {}
	correct_at_first = {'190':0, '191':0, '264':0, '265':0, '263':0, '266':0}
	data_dict = {}
	g1_number = 0
	g2_number = 0
	g3_number = 0

	for orderdict in reader:
		row = dict(orderdict)
		sid = row['studentID']
		pid = row['problemID']
		time = row['date']
		correct_first_time = 'F'

		if (sid not in giant_dict[pid]) or (time < giant_dict[pid][sid][0]): #get the initial submit
			giant_dict[pid][sid] = [time, correct_first_time,
									row['op1correct (t/f)'], row['op2correct (t/f)'], 
									row['op3correct (t/f)'], row['op4correct (t/f)'], 
									row['op5correct (t/f)'], row['op6correct (t/f)']]
		
		if 'f' not in giant_dict[pid][sid]:
			correct_at_first[pid] += 1
			giant_dict[pid][sid][1] = 'T'


		if sid not in students:
			if pid == '190' or pid == '191':	
				students[sid]='group_001'
				g1_number += 1

			elif pid == '265' or pid == '264':	
				students[sid]='group_002'
				g2_number += 1

			elif pid == '263' or pid == '266':	
				students[sid]='group_003'
				g3_number += 1

			data_dict[sid] = [students[sid], '', '']

		if pid in ['190','265','263']: 
			data_dict[sid][1] = giant_dict[pid][sid][1]
		else:
			data_dict[sid][2] = giant_dict[pid][sid][1]


	g1_q1_avg_cor = correct_at_first['190']/g1_number
	g1_q2_avg_cor = correct_at_first['191']/g1_number
	g1_diff = g1_q2_avg_cor - g1_q1_avg_cor

	g2_q1_avg_cor = correct_at_first['264']/g2_number
	g2_q2_avg_cor = correct_at_first['265']/g2_number
	g2_diff = g2_q2_avg_cor - g2_q1_avg_cor

	g3_q1_avg_cor = correct_at_first['263']/g3_number
	g3_q2_avg_cor = correct_at_first['266']/g3_number
	g3_diff = g3_q2_avg_cor - g3_q1_avg_cor

	return data_dict

'''
	#print('Giant Dictionary = ', giant_dict)
	print('Students = ', students)
	#print('correct_at_first = ', correct_at_first)
	print('Result Dictionary = ', data_dict)


	print('Number of g1_students = ', g1_number)
	print('G1_q1_correct = ', correct_at_first['190'])
	print('G1_q1_correctness =', g1_q1_avg_cor)
	print('G1_q2_correct = ', correct_at_first['191'])
	print('G1_q2_correctness =', g1_q2_avg_cor)
	print('G1_rate_diff =', g1_diff)
	print('\n')

	print('Number of g2_students = ', g2_number)
	print('G2_q1_correct = ', correct_at_first['264'])
	print('G2_q1_correctness =', g2_q1_avg_cor)
	print('G2_q2_correct = ', correct_at_first['265'])
	print('G2_q2_correctness =', g2_q2_avg_cor)
	print('G2_rate_diff =', g2_diff)
	print('\n')

	print('Number of g3_students = ', g3_number)
	print('G3_q1_correct = ', correct_at_first['263'])
	print('G3_q1_correctness =', g3_q1_avg_cor)
	print('G3_q2_correct = ', correct_at_first['266'])
	print('G3_q2_correctness =', g3_q2_avg_cor)
	print('G3_rate_diff =', g3_diff)


'''





def output_mc_s0(csv_output, data_dict):
	file = open(csv_output, "w")
	writer = csv.DictWriter(file, fieldnames = ['Student ID','Group ID','MC_Q1_init_correct',
												'MC_Q2_init_correct','MC_Q1_tries_correct',
												'MC_Q2_tries_correct','MC_Q1_tries_4_correct',
												'MC_Q2_tries_4_correct','SA_Q1_init_correct',
												'SA_Q2_init_correct','SA_Q3_init_correct',
												'SA_Q4_init_correct','SA_Q5_init_correct',
												'SA_Q1_tries_correct','SA_Q2_tries_correct',
												'SA_Q3_tries_correct','SA_Q4_tries_correct',
												'SA_Q5_tries_correct'])
	writer.writeheader()
	for sid, info in data_dict.items():
	    writer.writerow({'Student ID': sid, 'Group ID': info[0],
	    				 'MC_Q1_init_correct': info[1], 'MC_Q2_init_correct': info[2]})





if __name__ == "__main__":

	csv_file = './week9/mc_data.csv'
	data_dict = anlyse_mc_s0(csv_file)

	csv_output = './w9_output_mc_s0.csv'	
	output_mc_s0(csv_output, data_dict)





