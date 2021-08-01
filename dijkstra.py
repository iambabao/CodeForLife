# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/3/28
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/3/28
"""

from queue import PriorityQueue


def dijkstra(graph, src):
    num_nodes = len(graph)
    dist = [-1] * num_nodes
    visited = [False] * num_nodes
    pq = PriorityQueue()

    dist[src] = 0
    pq.put((0, src))
    while pq.qsize() != 0:
        d, u = pq.get()
        visited[u] = True

        for v in range(num_nodes):
            if not visited[v] and graph[u][v] != -1:
                if dist[v] == -1 or d + graph[u][v] < dist[v]:
                    dist[v] = d + graph[u][v]
                    pq.put((dist[v], v))

    return dist


def main():
    n, m, s = list(map(int, input().strip().split()))
    graph = [[-1] * n for _ in range(n)]
    for v in range(n):
        graph[v][v] = 0

    for _ in range(m):
        u, v, w = list(map(int, input().strip().split()))
        graph[u - 1][v - 1] = w
    print(dijkstra(graph, s - 1))


if __name__ == '__main__':
    main()
