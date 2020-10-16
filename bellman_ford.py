import numpy as np


def bellman_ford(g, s):
    V = len(g)

    dist = [np.inf] * V
    dist[s] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                w = g[u][v]
                if w == 0:
                    continue
                if dist[u] != np.inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in range(V):
        for v in range(V):
            w = g[u][v]
            if w == 0:
                continue

    return dist