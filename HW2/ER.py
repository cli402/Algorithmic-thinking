__author__ = 'Amimras'
import random
def make_ER_graph(num_nodes,probablity):
    '''return a ER graph if num_nodes is positive
        else return an empty graph'''
    if(num_nodes>0 and probablity>=0 and probablity<=1):
        ergraph={}
        for iume in range(0,num_nodes):
            for jexe in range(iume+1,num_nodes):
                    a=float(random.randint(0,num_nodes))/float(num_nodes)
                    if a<=probablity:
                        if iume in ergraph:
                            ergraph[iume].add(jexe);
                        else :
                            ergraph[iume]=set([jexe])
                        if jexe in ergraph:
                            ergraph[jexe].add(iume);
                        else:
                            ergraph[jexe]=set([iume])
    return ergraph
