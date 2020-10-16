import numpy as np
import time
from dijkstra import dijkstra
from bellman_ford import bellman_ford

V = 100
E = 500

m = [[0 for x in range(V)] for y in range(V)]

for i in range(E):
    f, t = [0, 0]
    while m[f][t] == 1 or f == t:
        f = np.random.randint(0, V, 1)[0]
        t = np.random.randint(0, V, 1)[0]
    w = np.random.randint(1, 25, 1)[0]
    m[f][t] = w
    m[t][f] = w

s = np.random.randint(0, V, 1)[0]
d_result = 0
be_result = 0

for _ in range(10):
    s_i = time.time()
    res_i = dijkstra(m, s)
    f_i = time.time()

    s_ii = time.time()
    res_ii = bellman_ford(m, s)
    f_ii = time.time()

    d_result += f_i - s_i
    be_result += f_ii - s_ii

print('Dijkstra average time:')
print(d_result / 10)
print()
print('Bellman Ford average time:')
print(be_result / 10)



