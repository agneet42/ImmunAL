#%%

import csv
from scipy.stats.stats import pearsonr

file = csv.reader(open("diseased_final.csv","r"))

all_arr = []
temp_all_arr = []

for lines in file:
    if(len(lines) > 0):
	    temp_all_arr.append(lines)

print(len(temp_all_arr))

for k in range(0,2333):
	temp = []
	for all in temp_all_arr:
		temp.append(all[k])
	all_arr.append(temp)
    
for x in range(0,2333):
	all_arr[x] = [float(j) for j in all_arr[x]]

arr_fin = []
for i in range(0,2333):
    for j in range(i+1,2333):
        temp = []
        temp.append(i+1)
        temp.append(j+1)
        val,unimp = pearsonr(all_arr[i],all_arr[j])
        temp.append(val)
        arr_fin.append(temp)
    print(i)


new_file = csv.writer(open("diseased_pcc_final.csv","w"))

for i in arr_fin:
	new_file.writerow(i)

print("Part 1 done")




#%%

import csv
import networkx as nx
import operator
import statistics
import numpy as np

G = nx.Graph()
file = csv.reader(open("controlled_diseased_final.csv",'r'))
file1 = csv.reader(open("controlled_diseased_final.csv",'r'))
file2 = csv.reader(open("controlled_diseased_final.csv",'r'))
nodes = []
nodes_temp = []
count = 0
for lines in file:
    if (len(lines)>0):
        nodes_temp.append(lines[0])
        nodes_temp.append(lines[1])
        count = count + 1

nodes = list(set(nodes_temp))
# print(len(nodes))
# G.add_nodes_from(nodes)

corr_array = []
for lines in file2:
    if(len(lines)>0):
       corr_array.append(float(lines[2]))

# print(len(corr_array))
mean1 = np.mean(corr_array)
stddev1 = statistics.stdev(corr_array)
max_range = mean1 + stddev1
max_range = max_range / 2 # variable, to be changed during testing
min_range = mean1 - stddev1
min_range = min_range / 2 # variable, to be changed during testing

edges = []
nodes_count = []
for lines in file1:
    if (len(lines)>0):
        if((float(lines[2]) > min_range) and (float(lines[2]) < max_range)):
            nodes_count.append(lines[0])
            nodes_count.append(lines[1])
            edges_temp = []
            # edges_temp = [lines[0],lines[1]]
            edges_temp = [lines[0],lines[1],float(lines[2])]
            edges.append(edges_temp)

# print(len(edges))

with open("layer1_unweighted_v2_final.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(edges)

print("done1")


nodes = []
nodes = list(set(nodes_count))
print(len(nodes))
print(len(edges))


G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges,weight='weight')
print("ready for calculation")
# dict1 = nx.closeness_centrality(G,distance='weight')
# dict1 = nx.degree_centrality(G)
dict1 = nx.eigenvector_centrality(G,weight='weight') 
sorted_dict1 = sorted(dict1.items(),key = operator.itemgetter(1),reverse = True)
sorted_dict1 = sorted_dict1[:40] # variable, to be changed during testing
for x in sorted_dict1:
    print(x[0])
# file3 = csv.writer(open('result_controlled.csv','w'))
print("Part 2 done")