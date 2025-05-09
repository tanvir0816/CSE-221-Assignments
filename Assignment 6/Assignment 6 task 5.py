from collections import deque
def bfs(s, adj):
    dist = [-1] * len(adj)
    q = deque([s])
    dist[s] = 0
    far = s
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[far]:
                    far = v
                    
    return far, dist[far], dist

def find_diameter(n, edges):
    adj = [[] for i in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    a, da, dist_a = bfs(1, adj)
    b, db, dist_b = bfs(a, adj)
    
    return db, a, b

n = int(input())
edges = [tuple(map(int, input().split())) for i in range(n - 1)]

d, u, v = find_diameter(n, edges)
print(d)
print(u, v)
