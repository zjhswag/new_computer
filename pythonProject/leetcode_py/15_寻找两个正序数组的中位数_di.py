from collections import defaultdict

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for x, y, z in roads:
            dist[x][y] = dist[y][x] = z
        seen = set()
        for _ in range(n - 1):
            u = None
            for i in range(n):
                if i not in seen and (not u or dist[0][i] < dist[0][u]):
                    u = i
            seen.add(u)
            for i in range(n):
                dist[0][i] = min(dist[0][i], dist[0][u] + dist[u][i])
        # 构造图 G
        g = defaultdict(list)
        for x, y, z in roads:
            if dist[0][y] - dist[0][x] == z:
                g[x].append(y)
            elif dist[0][x] - dist[0][y] == z:
                g[y].append(x)

        def dfs(u):
            if u == n - 1:
                return 1
            ret = 0
            for v in g[u]:
                ret += dfs(v)
            return ret % mod

        ans = dfs(0)
        return ans
