import csv
from collections import OrderedDict



def anlyse_mc_s1_s2(csv_file):
	file = open('./week9/mc_data.csv', "r")
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


	g1_q1_avg_tries_s1 = total_tries_took_s1['190']/g1_number
	g1_q2_avg_tries_s1 = total_tries_took_s1['191']/g1_number
	g1_q2_avg_tries_s2 = total_tries_took_s2['191']/g1_number

	g2_q1_avg_tries_s1 = total_tries_took_s1['264']/g2_number
	g2_q2_avg_tries_s1 = total_tries_took_s1['265']/g2_number
	g2_q2_avg_tries_s2 = total_tries_took_s2['265']/g2_number

	g3_q1_avg_tries_s1 = total_tries_took_s1['263']/g3_number
	g3_q2_avg_tries_s1 = total_tries_took_s1['266']/g3_number
	g3_q2_avg_tries_s2 = total_tries_took_s2['266']/g3_number


	#print('Giant Dictionary = ', giant_dict)
	#print('How many students = ', students)
	#print('total_tries_took_s1 = ', total_tries_took_s1)
	#print('total_tries_took_s2 = ', total_tries_took_s2)


	print('Number of g1_students =', g1_number)
	print('G1_q1_tries_took_s1 =', int(total_tries_took_s1['190']))
	print('G1_q1_avg_tries_s1 =', g1_q1_avg_tries_s1)
	print('G1_q2_tries_took_s1 =', int(total_tries_took_s1['191']))
	print('G1_q2_avg_tries_s1 =', g1_q2_avg_tries_s1)
	print('G1_q2_tries_took_s2 =', int(total_tries_took_s2['191']))
	print('G1_q2_avg_tries_s2 =', g1_q2_avg_tries_s2)
	print('\n')

	print('Number of g2_students =', g2_number)
	print('G2_q1_tries_took_s1 =', int(total_tries_took_s1['264']))
	print('G2_q1_avg_tries_s1 =', g2_q1_avg_tries_s1)
	print('G2_q2_tries_took_s1 =', int(total_tries_took_s1['265']))
	print('G2_q2_avg_tries_s1 =', g2_q2_avg_tries_s1)
	print('G2_q2_tries_took_s2 =', int(total_tries_took_s2['265']))
	print('G2_q2_avg_tries_s2 =', g2_q2_avg_tries_s2)
	print('\n')

	print('Number of g3_students =', g3_number)
	print('G3_q1_tries_took_s1 =', int(total_tries_took_s1['263']))
	print('G3_q1_avg_tries_s1 =', g3_q1_avg_tries_s1)
	print('G3_q2_tries_took_s1 =', int(total_tries_took_s1['266']))
	print('G3_q2_avg_tries_s1 =', g3_q2_avg_tries_s1)
	print('G3_q2_tries_took_s2 =', int(total_tries_took_s2['266']))
	print('G3_q2_avg_tries_s2 =', g3_q2_avg_tries_s2)




	return data_dict




def output_mc_s1_s2(csv_output, data_dict):
	file = open(csv_output, "w")
	writer = csv.DictWriter(file, fieldnames = ['SID','GID','S1_pre','S1_post','S2_post'])
	writer.writeheader()

	for sid, info in data_dict.items():
	    writer.writerow({'SID': sid, 'GID': info[0],
	    				 'S1_pre': info[1],'S1_post': info[2],'S2_post': info[3]})





if __name__=="__main__":

	csv_file = './week9/mc_data.csv'
	data_dict = anlyse_mc_s1_s2(csv_file)

	csv_output = './w9_output_mc_s1_s2.csv'	
	output_mc_s1_s2(csv_output, data_dict)


