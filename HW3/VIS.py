"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import urllib2
import matplotlib.pyplot as plt
import alg_cluster
import alg_clusters_matplotlib

# conditional imports
if DESKTOP:
    import HW3      # desktop project solution

else:
    #import userXX_XXXXXXXX as HW3   # CodeSkulptor project solution
    import codeskulptor
    codeskulptor.set_timeout(30)


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering

    Note that method may return num_clusters or num_clusters + 1 final clusters
    """

    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters)  / num_clusters

    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
           math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)

    return cluster_list


######




#####################################################################
# Code to load cancer data, compute a clustering and
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_3108_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    #cluster_list = sequential_clustering(singleton_list, 15)
    #print "Displaying", len(cluster_list), "sequential clusters"

    cluster_list = HW3.hierarchical_clustering(singleton_list, 15)
    print "Displaying", len(cluster_list), "hierarchical clusters"


    # cluster_list = HW3.kmeans_clustering(singleton_list,9, 5)
    # print "Displaying", len(cluster_list), "k-means clusters"

    #draw the clusters using matplotlib or simplegui
    if DESKTOP:
        alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
        #alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers
    # else:
    #     alg_clusters_simplegui.PlotClusters(data_table, cluster_list)   # use toggle in GUI to add cluster centers

run_example()

x=[i for i in range(20,5,-1) ]
y_111_H=[]
y_111_K=[]
y_290_H=[]
y_290_K=[]
y_896_K=[]
y_896_H=[]

def experiment_10(a):
    concatenate={}
    concatenate[111]=DATA_111_URL
    concatenate[290]=DATA_290_URL
    concatenate[896]=DATA_896_URL

    data_table = load_data_table(concatenate[a])

    ##for the hierarchical
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    for ele in x:
        singleton_list=HW3.hierarchical_clustering(singleton_list,ele)
        distortion=0
        for cluster in singleton_list:
            distortion+=cluster.cluster_error(data_table)
        if a==111:
            y_111_H.append(distortion)
        elif a==290:
            y_290_H.append(distortion)
        else:
            y_896_H.append(distortion)

    ##K-means
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    for ele in x:
        singleton_list=HW3.kmeans_clustering(singleton_list,ele,5)
        distortion=0
        for cluster in singleton_list:
            distortion+=cluster.cluster_error(data_table)
        if a==111:
            y_111_K.append(distortion)
        elif a==290:
            y_290_K.append(distortion)
        else:
            y_896_K.append(distortion)

    if a==111:
        plt.plot(x,y_111_H)
        plt.plot(x,y_111_K)
    elif a==290:
        plt.plot(x,y_290_H)
        plt.plot(x,y_290_K)
    else:
        plt.plot(x,y_896_H)
        plt.plot(x,y_896_K)

    plt.xlabel('Number of the clusters ')
    plt.ylabel('Total Distortion')
    plt.legend(['Hierarchical Clustering','K-mean clustering'])
    plt.title('Distortion comparison of two clustering method-'+str(a)+'counties')
    plt.grid(True)
    plt.savefig("HW3_"+str(a)+".png")
    plt.show()

# experiment_10(111)
# experiment_10(290)
# experiment_10(896)
#
#
#
#





