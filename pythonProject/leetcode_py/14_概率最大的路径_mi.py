# def maxProbability(n, edges, succProb, start_node, end_node):
#     """
#     :type n: int
#     :type edges: List[List[int]]
#     :type succProb: List[float]
#     :type start_node: int
#     :type end_node: int
#     :rtype: float
#     """

n = 3
edges = [[0, 1]]
succProb = [0.5]
start = 0
end = 2
dist = [[float(0)] * n for _ in range(n)]
print(dist)
for i in range(n):
    dist[i][i] = 0
for i, (x, y) in enumerate(edges):
    dist[x][y] = dist[y][x] = succProb[i]
print(dist)
for k in range(n):
    print('     0    1   2')
    j = 0
    for i in dist:
        print(j, ':', i)
        j = j + 1
    for i in range(n):
        for j in range(n):
            if dist[i][j] < dist[i][k] * dist[k][j]:
                dist[i][j] = dist[i][k] * dist[k][j]
    # print(dist)
# 1 2 1 0 0 2
# print(dist[start][end])



