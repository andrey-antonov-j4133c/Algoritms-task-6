import numpy as np


def dijkstra(g, s):

    V = len(g)

    def min_distance(dist, sptSet):
        min = np.inf
        for v in range(V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index

    dist = [np.inf] * V
    dist[s] = 0
    sptSet = [False] * V

    for _ in range(V):
        u = min_distance(dist, sptSet)
        sptSet[u] = True

        for v in range(V):
            if g[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + g[u][v]:
                dist[v] = dist[u] + g[u][v]

    return dist