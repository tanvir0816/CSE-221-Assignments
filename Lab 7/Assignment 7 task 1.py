from collections import deque
def dijkstra(N, S, D, u, v, w):
    graph ={i:[] for i in range(1,N+1)}
    for u, v, w in zip(u, v, w):
        graph[u].append((v, w))
    dist = [float('inf')] * (N + 1)
    parent = [-1] * (N + 1)
    dist[S] = 0
    q = deque()
    q.append(S)
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                q.append(v)
    if dist[D] == float('inf'):
        print(-1)
        return
    path = []
    curr = D
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(dist[D])
    print(" ".join(map(str, path)))
N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
dijkstra(N, S, D, u, v, w)
