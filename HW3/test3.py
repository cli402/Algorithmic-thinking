import time
from random import *

from HW3 import *
from ClusterClass import *
import matplotlib.pyplot as plt

def gen_random_clusters(num_clusters):
    list_cluster=[]
    for i in range(0,num_clusters):
        list_cluster.append(Cluster(set([]),random()*2-1,random()*2-1,1,0))
    return list_cluster

x=[]
slow=[]
fast=[]

def experiment():
    for i in range(2,201):
        list_to_compare=gen_random_clusters(i)
        start=time.clock()
        result=slow_closest_pair(list_to_compare)
        end=time.clock()
        slow.append(end-start)
        start=time.clock()
        result=fast_closest_pair(list_to_compare)
        end=time.clock()
        fast.append(end-start)
        x.append(i)
        print "done",i,"Number"
#experiment()


#
# plt.plot(x,slow)
# plt.plot(x,fast)
#
# plt.xlabel('Number of the clusters ')
# plt.ylabel('Running time')
# plt.legend(['Slow_closest_pair','Fast_closest_pari'])
# plt.title('running times for two method')
# plt.grid(True)
# plt.savefig("HW3_1.png")
# plt.show()

