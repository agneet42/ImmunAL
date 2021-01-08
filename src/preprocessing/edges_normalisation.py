#%%
import csv

file1 = csv.reader(open('diseased1.csv','r'))
total_list = []

for lines in file1:
	total_list.append(lines)
	break

# print(total_list[0][0])

#%%
file2 = open('finalproteins.txt','r')
controlled_list = []

for lines2 in file2:
	if("['NA']" not in lines2):
		controlled_list.append(lines2.lstrip('[').rstrip(']'))

# print(len(controlled_list))

indexes = []

for each in controlled_list:
	for i in range(0,len(total_list[0])):
		if(total_list[0][i] != "NA" and total_list[0][i] in each):
			indexes.append(i)
			break

# print((indexes))

the_values = []
count = 0

file3 = csv.reader(open('diseased1.csv','r'))

for lines3 in file3:
	break

for lines3 in file3:
	the_values.append(lines3)


final_values = []
for arr in the_values:
	temp = []
	temp = [arr[i] for i in indexes]
	final_values.append(temp)

print(len(final_values))


file4 = csv.writer(open('diseased_final.csv','w'))

for arr in final_values:
	file4.writerow(arr)
