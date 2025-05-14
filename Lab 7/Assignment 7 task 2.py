from collections import deque
def dijkstra(N, graph, start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    q = deque()
    q.append(start)

    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                q.append(v)
    return dist
N, M, S, T = map(int, input().split())
dic={i:[] for i in range(1,N+1)}
for i in range(M):
    a, b, c = map(int, input().split())
    dic[a].append((b,c))
alice=dijkstra(N,dic,S)
bob=dijkstra(N,dic,T)
min_time = float('inf')
meeting_node = -1
for i in range(1, N + 1):
    if alice[i] != float('inf') and bob[i] != float('inf'):
        max_time = max(alice[i], bob[i])
        if max_time < min_time or (max_time == min_time and i < meeting_node):
            min_time = max_time
            meeting_node = i

if meeting_node == -1:
    print(-1)
else:
    print(min_time, meeting_node)


