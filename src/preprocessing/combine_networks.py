#%%
import csv

file1 = csv.reader(open('controlled_pcc_final.csv','r'))
file2 = csv.reader(open('diseased_pcc_final.csv','r'))

arr1 = []
arr2 = []

for lines in file1:
	if(len(lines)>0):
		arr1.append([lines[0],lines[1],float(lines[2])])

for lines in file2:
	if(len(lines)>0):
		arr2.append([lines[0],lines[1],float(lines[2])])

arr_common = []

for i in range(0,len(arr1)):
	weights = arr1[i][2] * 0.5 + arr2[i][2] * 0.5
	arr_common.append([arr1[i][0],arr1[i][1],weights])

for i in range(len(arr1),len(arr2)):
	weights = arr2[i][2] * 0.5
	arr_common.append([arr2[i][0],arr2[i][1],weights])

# print(len(arr_common))

file3 = csv.writer(open('controlled_diseased_final.csv','w'))
for arr in arr_common:
	file3.writerow(arr)
