__author__ = 'Amras'

# general imports
import urllib2
import random
import time
import math
import copy
from UPA import preferential_attachment
from HW2 import *
from ER import make_ER_graph
# Desktop imports
import matplotlib.pyplot as plt


############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order

##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def random_order(graph):
    graph_copy=copy.deepcopy(graph)
    random_list=[]
    for itex in range(len(graph_copy)):
        random_choice=random.choice(graph_copy.keys())
        random_list.append(random_choice)
        graph_copy.pop(random_choice)
    return random_list

def targeted_order(ugraph):
    degree_set={}
    ugraph_copy=copy.deepcopy(ugraph)
    for node in ugraph_copy:
        for val in ugraph_copy[node]:
            if node not in ugraph_copy[val]:
                ugraph_copy[val].append(node)
    for node in ugraph_copy:
        degree=len(ugraph_copy[node])
        degree_set[degree].append(node)
    degree_list=[]
    while len(degree_set)!=0:
        max_degree=max(list(degree_set.keys));
        node_set=degree_set[max_degree]
        while len(node_set)!=0:
            random_node=random.randint(len(node_set))
            degree_list.append(node_set[random_node]);
            node_set.pop(random_node)
        degree_set.pop(max_degree)
    return degree_list


print "Work Start"
a=load_graph(NETWORK_URL)
b=make_ER_graph(1239,0.004)
c=preferential_attachment(1239,3)

print "Compute the random order"
a_order=random_order(a)
b_order=random_order(b)
c_order=random_order(c)

print "Compute the resilience"
a_res=compute_resilience(a,a_order)
b_res=compute_resilience(b,b_order)
c_res=compute_resilience(c,c_order)

###############################################
with open('new_filea.txt', 'w') as out_file:
    for i in range(len(a_res)):
        out_file.write('%d\n'%a_res[i])
out_file.close()
with open('new_fileb.txt', 'w') as out_file:
    for i in range(len(b_res)):
        out_file.write('%d\n'%b_res[i])
out_file.close()
with open('new_filec.txt', 'w') as out_file:
    for i in range(len(c_res)):
        out_file.write('%d\n'%c_res[i])
out_file.close()

#####################################################
import numpy as np
x_axis=[]
for i in range(len(a_res)):
    x_axis.append(i)

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
