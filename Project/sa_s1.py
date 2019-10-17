import csv
from collections import OrderedDict



#def anlyse_sa_s1(csv_file):
file = open('./week9/short_answer_data.csv', "r")
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
			students[sid]='group_003'
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

g1_q1_avg_tries = total_tries_took['29']/g1_number
g1_q2_avg_tries = total_tries_took['30']/g1_number
g1_q3_avg_tries = total_tries_took['31']/g1_number
g1_q4_avg_tries = total_tries_took['32']/g1_number

g2_q1_avg_tries = total_tries_took['36']/g2_number
g2_q2_avg_tries = total_tries_took['38']/g2_number
g2_q3_avg_tries = total_tries_took['42']/g2_number
g2_q4_avg_tries = total_tries_took['45']/g2_number
g2_q5_avg_tries = total_tries_took['33']/g2_number

g3_q1_avg_tries = total_tries_took['37']/g3_number
g3_q2_avg_tries = total_tries_took['39']/g3_number
g3_q3_avg_tries = total_tries_took['43']/g3_number
g3_q4_avg_tries = total_tries_took['44']/g3_number
g3_q5_avg_tries = total_tries_took['35']/g3_number


	#return data_dict




#print('Giant Dictionary = ', giant_dict)
#print('How many students = ', students)
#print('Total_tries_took = ', total_tries_took)

print('Number of g1_students = ', g1_number)
print('G1_q1_tries_took = ', int(total_tries_took['29']))
print('G1_q1_avg_tries =', g1_q1_avg_tries)
print('G1_q2_tries_took = ', int(total_tries_took['30']))
print('G1_q2_avg_tries =', g1_q2_avg_tries)
print('G1_q3_tries_took = ', int(total_tries_took['31']))
print('G1_q3_avg_tries =', g1_q3_avg_tries)
print('G1_q4_tries_took = ', int(total_tries_took['32']))
print('G1_q4_avg_tries =', g1_q4_avg_tries)
print('\n')

print('Number of g2_students = ', g2_number)
print('G2_q1_tries_took = ', int(total_tries_took['36']))
print('G2_q1_avg_tries =', g2_q1_avg_tries)
print('G2_q2_tries_took = ', int(total_tries_took['38']))
print('G2_q2_avg_tries =', g2_q2_avg_tries)
print('G2_q3_tries_took = ', int(total_tries_took['42']))
print('G2_q3_avg_tries =', g2_q3_avg_tries)
print('G2_q4_tries_took = ', int(total_tries_took['45']))
print('G2_q4_avg_tries =', g2_q4_avg_tries)
print('G2_q5_tries_took = ', int(total_tries_took['33']))
print('G2_q5_avg_tries =', g2_q5_avg_tries)
print('\n')

print('Number of g3_students = ', g3_number)
print('G3_q1_tries_took = ', int(total_tries_took['37']))
print('G3_q1_avg_tries =', g3_q1_avg_tries)
print('G3_q2_tries_took = ', int(total_tries_took['39']))
print('G3_q2_avg_tries =', g3_q2_avg_tries)
print('G3_q3_tries_took = ', int(total_tries_took['43']))
print('G3_q3_avg_tries =', g3_q3_avg_tries)
print('G3_q4_tries_took = ', int(total_tries_took['44']))
print('G3_q4_avg_tries =', g3_q4_avg_tries)
print('G3_q5_tries_took = ', int(total_tries_took['35']))
print('G3_q5_avg_tries =', g3_q5_avg_tries)
'''
#print('Giant Dictionary = ', giant_dict)
print('How many students = ', students)
print('Total_tries_took = ', total_tries_took)
g3_q1_avg_tries = total_tries_took['37']/len(students['g3'])
print('Number of g3_students = ', len(students['g3']))
print('G3_q1_tries_took = ', int(total_tries_took['37']))
print('G3_q1_avg_tries =', g3_q1_avg_tries)
	



def output_sa_s1(csv_output, data_dict):
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
	    				 'SA_Q1_tries_correct': info[1],'SA_Q2_tries_correct': info[2],
						 'SA_Q3_tries_correct': info[3],'SA_Q4_tries_correct': info[4],
						 'SA_Q5_tries_correct': info[5]})







if __name__=="__main__":

	csv_file = './week9/short_answer_data.csv'
	data_dict = anlyse_sa_s1(csv_file)

	csv_output = './w9_output_sa_s1.csv'	
	output_sa_s1(csv_output, data_dict)



'''






