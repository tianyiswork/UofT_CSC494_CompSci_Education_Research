import csv
from collections import OrderedDict



#def anlyse_sa_s0(csv_file):
file = open('./week9/short_answer_data.csv', "r")
reader = csv.DictReader(file)

giant_dict = {'33':{},         #explain
			  '35':{}}         #motivate
num_attempts = {'33':0,'35':0}
data_dict = {}

g2_number = 0
g3_number = 0

for orderdict in reader:
	row = dict(orderdict)
	sid = row['user']
	pid = row['problem_id']
	attempts = 1

	if (pid in ['33','35']): 
		if sid not in giant_dict[pid]: #get the initial submit
			giant_dict[pid][sid] = [attempts]
			if pid == '33':	
				data_dict[sid]=['2',0]
				g2_number += 1

			else:	
				data_dict[sid]=['3',0]
				g3_number += 1

		else:
			giant_dict[pid][sid][0] += 1
		num_attempts[pid] += 1
		data_dict[sid][1] = giant_dict[pid][sid][0]


g2_q5_avg_cor = num_attempts['33']/g2_number
g3_q5_avg_cor = num_attempts['35']/g3_number


print('Giant Dictionary =', giant_dict)
print('num_attempts =', num_attempts)


print('Number of g2_students =', g2_number)
print('G2_q5_total_num_attempts =', num_attempts['33'])
print('G2_q5_avg_num_attempts =', g2_q5_avg_cor)
print('\n')


print('Number of g3_students =', g3_number)
print('G3_q5_total_num_attempts =', num_attempts['35'])
print('G3_q5_avg_num_attempts =', g3_q5_avg_cor)
print('\n')


#return data_dict

'''




def output_sa_s0(csv_output, data_dict):
	file = open(csv_output, "w")
	writer = csv.DictWriter(file, fieldnames = ['SID','GID','summary_num_attempts'])
	writer.writeheader()

	for sid, info in data_dict.items():
	    writer.writerow({'SID': sid, 'GID': info[0],'summary_num_attempts': info[5]})







if __name__=="__main__":

	csv_file = './week9/short_answer_data.csv'
	data_dict = anlyse_sa_s0(csv_file)

	csv_output = './w9_output_sa_s0.csv'	
	output_sa_s0(csv_output, data_dict)

'''
