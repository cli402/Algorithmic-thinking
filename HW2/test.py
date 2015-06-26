__author__ = 'Amras'
import numpy as np
import copy
import time
import random
from UPA import *
from ER import *
from HW2 import *
from targeted import *
from matplotlib import pyplot as plt


'''
text_file = open("filename.dat", "r")
lines = text_file.readlines()
print lines
print len(lines)
text_file.close()

plt.plot(x_axis,a_res)
plt.plot(x_axis,b_res)
plt.plot(x_axis,c_res)

plt.xlabel('Number of the attack ')
plt.ylabel('Resilience of the Network')
plt.legend(['Example Computer Network','ER Graph','UPA Graph'])
plt.title('resilience of the network under an attack')
plt.grid(True)
plt.savefig("test.png")
plt.show()
'''

def fast_targeted_order(ugraph):
    degree_set={}
    ugraph_copy=copy.deepcopy(ugraph)
    for node in ugraph_copy:
        for val in ugraph_copy[node]:
            if node not in ugraph_copy[val]:
                ugraph_copy[val].add(node)
    for node in ugraph_copy:
        degree=len(ugraph_copy[node])
        if degree in degree_set:
            degree_set[degree].add(node)
        else:
            degree_set[degree]=set();
            degree_set[degree].add(node)
    degree_list=[]
    while len(degree_set)!=0:
        max_degree=max(list(degree_set.keys()));
        node_set=list(degree_set[max_degree])
        while len(node_set)!=0:
            random_node=random.randrange(0,len(node_set))
            degree_list.append(node_set[random_node]);
            node_set.pop(random_node)
        degree_set.pop(max_degree)
    return degree_list
'''
a=make_ER_graph(1239,0.004)
b=preferential_attachment(1239,3)
'''
def compute_edges(ugraph):
    cout=0
    for node in ugraph:
        nodeset=copy.deepcopy(ugraph[node])
        for val in nodeset:
            ugraph[node].remove(val)
            cout+=1
            if node in ugraph[val]:
                ugraph[val].remove(node)
    return cout




'''
text_file = open("new_filea.txt", "r")
a_res = text_file.readlines()
print len(a_res)
text_file.close()

text_file = open("new_fileb.txt", "r")
b_res = text_file.readlines()
print len(b_res)
text_file.close()

text_file = open("new_filec.txt", "r")
c_res = text_file.readlines()
print len(c_res)
text_file.close()


a_axis=[]
for i in range(len(a_res)):
    a_res[i]=int(a_res[i])
    a_axis.append(i)

b_axis=[]
for i in range(len(b_res)):
    b_axis.append(i)

c_axis=[]
for i in range(len(c_res)):
    c_axis.append(i)


plt.plot(a_axis,a_res)

plt.plot(b_axis,b_res)
plt.plot(c_axis,c_res)

plt.xlabel('Number of the attack ')
plt.ylabel('Resilience of the Network')
plt.legend(['Example Computer Network','ER Graph','UPA Graph'])
plt.title('resilience of the network under an attack')
plt.grid(True)
plt.savefig("test.png")
plt.show()

'''


#get the time of the runnning the targeted sequence
tar_time=[]
fast_time=[]
x_axis=[]
for i in range(10,1000,10):
    x_axis.append(i)
    graph=preferential_attachment(i,5)

    startime=time.time()
    targeted_order(graph);
    time_consum=time.time()-startime;
    tar_time.append(time_consum);

    startime=time.time()
    fast_targeted_order(graph);
    time_consum=time.time()-startime;
    fast_time.append(time_consum);



print x_axis
print tar_time
print fast_time

plt.plot(x_axis,tar_time)
plt.plot(x_axis,fast_time)


plt.xlabel('Number of Nodes')
plt.ylabel('Time consumed')
plt.legend(['Targeted order','fast_targed_order'])
plt.title('desktop Python to generate the timing')
plt.grid(True)
plt.savefig("test1.png")
plt.show()
