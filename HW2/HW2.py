""" Connected components and graph resilience"""
from collections import deque
import random

def bfs_visited(ugraph, start_node):
    """    """"""Takes the undirected
    graph ugraph and the node start_node
    and returns the set consisting of all
    nodes that are visited by a breadth-first """
    for node in ugraph:
        for val in ugraph[node]:
            if node not in ugraph[val]:
                ugraph[val].add(node)
    un_queue=deque()
    visited=set([])
    visited.add(start_node)
    un_queue.append({start_node:ugraph[start_node]});
    while len(un_queue)!=0:
        jay=un_queue.pop();
        for node in jay:
            for axe in jay[node]:
                if axe not in visited:
                    visited.add(axe);
                    un_queue.append({axe:ugraph[axe]});
    return visited


def cc_visited(ugraph):
    '''Takes the undirected graph ugraph and returns
     a list of sets, where each set consists of all the nodes (and nothing else)'''
    remain_node={}
    for node in ugraph:
        remain_node[node]=ugraph[node];
    for node in remain_node:
        for val in remain_node[node]:
            if node not in remain_node[val]:
                remain_node[val].add(node)
    cic_visited=[]
    while len(remain_node)!=0:
        #start_node=random.randrange(0,remain_node_length);
        #start={start_node:remain_node[start_node]}
        start_pair=remain_node.popitem();
        start=start_pair[0]
        visited=bfs_visited(ugraph,start)
        cic_visited.append(visited)
        for axe in visited:
            if axe in remain_node.keys():
                remain_node.pop(axe)
    return cic_visited

def largest_cc_size(ugraph):
    ''' Takes the undirected graph ugraph and returns the size (an integer) of the largest connected component in ugraph'''
    imax=0
    path_length=cc_visited(ugraph)
    for lengh in path_length:
        if len(lengh)>imax:
            imax=len(lengh)
    return imax

def bfs(ugraph,startnode):
    """Print the lenght of the graph"""
    queue_node=deque();
    distence={}
    infinity=2**25
    for node in ugraph:
        distence[node]=infinity
    for key in startnode:
        distence[key]=0;
    queue_node.append(startnode)
    while len(queue_node)!=0:
        jay=queue_node.pop()
        neighbor=jay.itervalues();
        boute=neighbor.next()
        for node in boute:
            if distence[node]==infinity:
                jaykeys=jay.keys()
                distence[node]=distence[jaykeys[0]]+1
                queue_node.append({node:ugraph[node]})
    max=0
    for node in distence:
        if distence[node]!=infinity and distence[node]>max:
            max=distence[node]
    return max+1


def compute_resilience(ugraph,attack_order):
    """Compute the resileance of the network"""
    list_size=[largest_cc_size(ugraph)];
    for axe in attack_order:
        ugraph.pop(axe)
        for node in ugraph:
            if axe in ugraph[node]:
                ugraph[node].remove(axe)
        list_size.append(largest_cc_size(ugraph))
    return list_size

