__author__ = 'Amras'

import random

def make_complete_graph(num_nodes):
    '''return a complete graph if num_nodes is positive
        else return an empty graph'''
    if(num_nodes>0):
        completegraph={}
        for iume in range(0,num_nodes):
            completegraph[iume]=set([])
            for jexe in range(0,num_nodes):
                    if jexe!=iume:
                        completegraph[iume].add(jexe);
    return completegraph

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm

    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that each node number
        appears in correct ratio

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def preferential_attachment(total,piece):
    #the preferential attachement principle
    initial_graph=make_complete_graph(piece)
    inst=UPATrial(piece)
    for i in range(piece,total):
        retu_node=inst.run_trial(piece)
        initial_graph[i]=retu_node
    return initial_graph

