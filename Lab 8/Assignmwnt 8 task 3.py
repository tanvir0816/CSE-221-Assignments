from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def unite(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.size[xr] > self.size[yr]:
            xr, yr = yr, xr
        self.parent[xr] = yr
        self.size[yr] += self.size[xr]
        return True
def dfs(u, target, parent, max_weight, graph, visited):
    if u == target:
        return max_weight
    visited[u] = True
    for v, w in graph[u]:
        if not visited[v] and v != parent:
            res = dfs(v, target, u, max(max_weight, w), graph, visited)
            if res != -1:
                return res
    return -1
def second_best_mst(n, edge_list):
    edge_list.sort()
    dsu = DisjointSet(n)
    mst_cost = 0
    count = 0
    graph = defaultdict(list)
    used = [False] * len(edge_list)
    for i, (w, u, v) in enumerate(edge_list):
        if dsu.unite(u, v):
            mst_cost += w
            used[i] = True
            count += 1
            graph[u].append((v, w))
            graph[v].append((u, w))
        if count == n - 1:
            break
    if count != n - 1:
        return -1 
    second_best = float('inf')
    for i, (w, u, v) in enumerate(edge_list):
        if used[i]:
            continue
        visited = [False] * n
        max_w = dfs(u, v, -1, -1, graph, visited)
        if max_w != -1 and w > max_w:
            new_cost = mst_cost - max_w + w
            if new_cost > mst_cost:
                second_best = min(second_best, new_cost)
    return -1 if second_best == float('inf') else second_best
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))
print(second_best_mst(n, edges))
