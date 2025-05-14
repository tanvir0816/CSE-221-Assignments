from collections import deque
def dijkstramodified(N, graph, start=1):
    danger = [float('inf')] * (N + 1)
    danger[start] = 0
    q = deque()
    q.append(start)

    while q:
        u = q.popleft()
        for v, w in graph[u]:
            maxi = max(danger[u], w)
            if maxi < danger[v]:
                danger[v] = maxi
                q.append(v)
    return danger
N, M = map(int, input().split())
dic = {i: [] for i in range(1, N + 1)}
for i in range(M):
    a, b, c = map(int, input().split())
    dic[a].append((b, c))
    dic[b].append((a, c))
res = dijkstramodified(N, dic, 1)
for i in range(1, N + 1):
    if i == 1:
        print(0, end=' ')
    elif res[i] == float('inf'):
        print(-1, end=' ')
    else:
        print(res[i], end=' ')
