__author__ = 'Amras'
import numpy as np
import copy
import random
from UPA import *
from ER import *
from matplotlib import pyplot as plt

x_axis=[]
for i in range(len(a_res)):
    x_axis.append(i)
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

def targeted_order(ugraph):
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

a=make_ER_graph(20,0.5)
b=preferential_attachment(20,5)

a_order=targeted_order(a)
b_order=targeted_order(b)
print a_order,b_order

