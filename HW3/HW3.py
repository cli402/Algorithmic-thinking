"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    dis=float("inf")
    iai=-1
    jei=-1
    for ele in range(0,len(cluster_list)):
        for ele_com in range(ele+1,len(cluster_list)):
                (dis,iai,jei)=min(pair_distance(cluster_list,ele,ele_com),(dis,iai,jei))
    return (dis,iai,jei)



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    num=len(cluster_list)
    if num<3:
        return slow_closest_pair(cluster_list)
    else:
        mid=int(math.floor(num/2))
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        mid_cor=(cluster_list[mid-1].horiz_center()+cluster_list[mid].horiz_center())/2
        (dil,ieil,jeil)=fast_closest_pair(cluster_list[:mid])
        (dilr,ieir,jeir)=fast_closest_pair(cluster_list[mid:])
        (dis,iai,jei)=min((dil,ieil,jeil),(dilr,ieir+mid,jeir+mid))
        (dis,iai,jei)=min(closest_pair_strip(cluster_list,mid_cor,dis),(dis,iai,jei))
        return (dis,iai,jei)


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """
    s_list=[]
    for ele in cluster_list:
        if abs(ele.horiz_center()-horiz_center)<half_width:
            s_list.append(ele)
    dis=float("inf")
    iai=-1
    jei=-1

    if len(s_list) > 0:
        s_list.sort(key=lambda cluster: cluster.vert_center())
        k_len=len(s_list)

        for uou in range(0,k_len-1):
            for vei in range(uou+1,min(uou+3,k_len-1)+1):
                if dis > s_list[uou].distance(s_list[vei]):
                    dis=s_list[uou].distance(s_list[vei])
                    first=cluster_list.index(s_list[uou])
                    second=cluster_list.index(s_list[vei])
                    iai=min(first,second)
                    jei=max(first,second)
    return (dis,iai,jei)


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) >num_clusters:
        (dis,iei,jei)=fast_closest_pair(cluster_list)
        cluster_list[iei].merge_clusters(cluster_list[jei])
        cluster_list.pop(jei)
        print "Number of clusters is ",len(cluster_list)
    return cluster_list


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
    list_copy=[]
    for ele in cluster_list:
        list_copy.append(ele.copy())
    if len(list_copy)>0:
        list_copy.sort(key = lambda cluster: cluster.total_population() , reverse=True)
        list_copy=list_copy[:num_clusters]
    else:
        return None
    for interation in range(0,num_iterations):
        list_merge=[]
        list_container=[None]*num_clusters
        for ele in range(0,len(cluster_list)):
            jiei=-1
            dis=float("inf")
            for center in range(0,num_clusters):
                if dis>cluster_list[ele].distance(list_copy[center]):
                    dis=cluster_list[ele].distance(list_copy[center])
                    jiei=center
            list_merge.append(jiei)
            if list_container[jiei]==None:
                list_container[jiei]=cluster_list[ele].copy()
            else:
                list_container[jiei].merge_clusters(cluster_list[ele].copy())
        ##get the newly updated center to the list_copy
        for num in range(0,num_clusters):
            list_copy[num]=list_container[num].copy()
    return list_copy


