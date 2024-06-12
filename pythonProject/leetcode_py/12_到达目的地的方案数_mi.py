from collections import defaultdict
from functools import cache
# def countPaths(n, roads):
#     """
#     :type n: int
#     :type roads: List[List[int]]
#     :rtype: int
#     """


from fontTools.misc import vector

n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
mod = 10 ** 9 + 7

dist = [[float("inf")] * n for _ in range(n)]
# print(dist)
path = [[-1 for _ in range(n)] for _ in range(n)]
# print(path)
for i in range(n):
    dist[i][i] = 0

for x, y, z in roads:
    dist[x][y] = dist[y][x] = z
    path[x][y] = path[y][x] = 0
# for k in range(n):
#     print('     0    1   2   3   4   5   6')
#     j = 0
#     for i in dist:
#         print(j, ':', i)
#         j = j + 1
#     for i in range(n):
#         for j in range(n):
#             if dist[i][j] > dist[i][k] + dist[k][j]:
#                 dist[i][j] = dist[i][k] + dist[k][j]
#                 path[i][j] = k


seen = set()
for _ in range(n - 1):
    u = None
    for i in range(n):
        # print('u is ', u)
        if i not in seen and (not u or dist[0][i] < dist[0][u]):
            u = i
            # print(i)
    seen.add(u)
    for i in range(n):
        dist[0][i] = min(dist[0][i], dist[0][u] + dist[u][i])

print(dist[0])

g = defaultdict(list)
# print(g)
for x, y, z in roads:
    if dist[0][y] - dist[0][x] == z:
        g[x].append(y)
    elif dist[0][x] - dist[0][y] == z:
        print(x, y, z, dist[0][x], dist[0][y])
        g[y].append(x)
print(g)


# @cache
def dfs(u):
    if u == n - 1:
        return 1
    ret = 0
    for v in g[u]:
        print(v, ret)
        ret += dfs(v)
    return ret % mod


ans = dfs(0)
print(ans)
# dfs.cache_clear()



# def try1():
#     for i in h:
#         print(i)
#         if i ==2:
#             break
#
# try1()
