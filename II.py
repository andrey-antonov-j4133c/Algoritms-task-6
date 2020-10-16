from a_star import a_star
import numpy as np
import time

grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

for _ in range(30):
    i = j = 0

    while i == j or grid[i][j] == 0:
        i = np.random.randint(0, 10, 1)[0]
        j = np.random.randint(0, 10, 1)[0]
    grid[i][j] = 0

print("The Grid:")
print()

for itm in grid:
    print(itm)

res = 0

print()
print('Path finding:')
print()

for _ in range(5):
    s = (0, 0)
    f = (0, 0)

    while s == f or grid[s[0]][s[1]] == 0 or grid[f[0]][f[1]] == 0:
        s = (np.random.randint(0, 10, 1)[0], np.random.randint(0, 10, 1)[0])
        f = (np.random.randint(0, 10, 1)[0], np.random.randint(0, 10, 1)[0])

    start = time.time()
    path = a_star(grid, s, f)
    finish = time.time()

    if path is None:
        print('No path between {} and {}'.format(s, f))
    else:
        print('Path between {} and {} is'.format(s, f))
        print(path)
    print()
    res += finish - start

print('A* average time:')
print(res / 5)
