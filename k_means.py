# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/9/2
@Desc               : 2D nodes
@Last modified by   : Bao
@Last modified date : 2021/9/2
"""

import math

def calc_dist(src, dst):
    return math.sqrt((src[0] - dst[0]) ** 2 + (src[1] - dst[1]) ** 2)


def get_cluster_id(node, cores):
    cluster_id, min_dist = 0, -1

    for i, core in enumerate(cores):
        dist = calc_dist(node, cores)
        if min_dist == -1 or dist < min_dist:
            cluster_id, min_dist = i, dist

    return cluster_id


def get_cluster_core(cluster):
    # TODO
    return cluster[0]


def k_means(nodes, k, step=1000):
    cores = list(nodes.values())[:k]

    for _ in range(step):
        clusters = [[core] for core in cores]
        for node_id, value in nodes.items():
            cluster_id = get_cluster_id(nodes[node_id], cores)
            clusters[cluster_id].append(value)
        cores = [get_cluster_core(c) for c in clusters]

    return cores
