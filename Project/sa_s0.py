import csv
from collections import OrderedDict



def anlyse_sa_s0(csv_file):
	file = open(csv_file, "r")
	reader = csv.DictReader(file)

	giant_dict = {'29':{}, '30':{}, '31':{}, '32':{},                  #group_1
				  '36':{}, '38':{}, '42':{}, '45':{}, '33':{},         #group_2
				  '37':{}, '39':{}, '43':{}, '44':{}, '35':{}}         #group_3
	students = {}
	correct_at_first = {'29':0, '30':0, '31':0, '32':0,
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
		correct_first_time = 'F'

		if (sid not in giant_dict[pid]) or (time < giant_dict[pid][sid][0]): #get the initial submit
			giant_dict[pid][sid] = [time, row['submission'], row['score'], correct_first_time]
			correct_at_first[pid] += int(giant_dict[pid][sid][2])
			if giant_dict[pid][sid][2] == '1': correct_first_time = 'T'
		
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
			data_dict[sid][1] = giant_dict[pid][sid][-1]
		elif pid in ['30','38','39']: 
			data_dict[sid][2] = giant_dict[pid][sid][-1]		
		elif pid in ['31','42','43']: 
			data_dict[sid][3] = giant_dict[pid][sid][-1]		
		elif pid in ['32','45','44']: 
			data_dict[sid][4] = giant_dict[pid][sid][-1]		
		else:
			data_dict[sid][5] = giant_dict[pid][sid][-1]

	g1_q1_avg_cor = correct_at_first['29']/g1_number
	g1_q2_avg_cor = correct_at_first['30']/g1_number
	g1_q3_avg_cor = correct_at_first['31']/g1_number
	g1_q4_avg_cor = correct_at_first['32']/g1_number

	g2_q1_avg_cor = correct_at_first['36']/g2_number
	g2_q2_avg_cor = correct_at_first['38']/g2_number
	g2_q3_avg_cor = correct_at_first['42']/g2_number
	g2_q4_avg_cor = correct_at_first['45']/g2_number
	g2_q5_avg_cor = correct_at_first['33']/g2_number

	g3_q1_avg_cor = correct_at_first['37']/g3_number
	g3_q2_avg_cor = correct_at_first['39']/g3_number
	g3_q3_avg_cor = correct_at_first['43']/g3_number
	g3_q4_avg_cor = correct_at_first['44']/g3_number
	g3_q5_avg_cor = correct_at_first['35']/g3_number


	return data_dict


	'''
	#print('Giant Dictionary = ', giant_dict['37'])
	#print('correct_at_first = ', correct_at_first)

	print('Number of g1 students = ', g1_number)
	print('G1_q1_correct = ', correct_at_first['29'])
	print('G1_q1_correctness =', g1_q1_avg_cor)
	print('G1_q2_correct = ', correct_at_first['30'])
	print('G1_q2_correctness =', g1_q2_avg_cor)
	print('G1_q3_correct = ', correct_at_first['31'])
	print('G1_q3_correctness =', g1_q3_avg_cor)
	print('G1_q4_correct = ', correct_at_first['32'])
	print('G1_q4_correctness =', g1_q4_avg_cor)
	print('\n')


	print('Number of g2_students = ', g2_number)
	print('G2_q1_correct = ', correct_at_first['36'])
	print('G2_q1_correctness =', g2_q1_avg_cor)
	print('G2_q2_correct = ', correct_at_first['38'])
	print('G2_q2_correctness =', g2_q2_avg_cor)
	print('G2_q3_correct = ', correct_at_first['42'])
	print('G2_q3_correctness =', g2_q3_avg_cor)
	print('G2_q4_correct = ', correct_at_first['45'])
	print('G2_q4_correctness =', g2_q4_avg_cor)
	print('G2_q5_correct = ', correct_at_first['33'])
	print('G2_q5_correctness =', g2_q5_avg_cor)
	print('\n')


	print('Number of g3_students = ', g3_number)
	print('G3_q1_correct = ', correct_at_first['37'])
	print('G3_q1_correctness =', g3_q1_avg_cor)
	print('G3_q2_correct = ', correct_at_first['39'])
	print('G3_q2_correctness =', g3_q2_avg_cor)
	print('G3_q3_correct = ', correct_at_first['43'])
	print('G3_q3_correctness =', g3_q3_avg_cor)
	print('G3_q4_correct = ', correct_at_first['44'])
	print('G3_q4_correctness =', g3_q4_avg_cor)
	print('G3_q5_correct = ', correct_at_first['35'])
	print('G3_q5_correctness =', g3_q5_avg_cor)

	print('How many students = ', students)
	print('correct_at_first = ', correct_at_first)
	g3_q1_avg_cor = correct_at_first['37']/len(students['g3'])
	print('Number of g3_students = ', len(students['g3']))
	print('G3_q1_correct = ', int(correct_at_first['37']))
	print('G3_q1_correctness =', g3_q1_avg_cor)

	'''




def output_sa_s0(csv_output, data_dict):
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
	    				 'SA_Q1_init_correct': info[1],'SA_Q2_init_correct': info[2],
	    				 'SA_Q3_init_correct': info[3],'SA_Q4_init_correct': info[4],
	    				 'SA_Q5_init_correct': info[5]})







if __name__=="__main__":

	csv_file = './week9/short_answer_data.csv'
	data_dict = anlyse_sa_s0(csv_file)

	csv_output = './w9_output_sa_s0.csv'	
	output_sa_s0(csv_output, data_dict)


