from queue import PriorityQueue
def second_shortest_path(N, M, S, D, u, v, w):
    graph = [[] for _ in range(N + 1)]

    for i in range(M):
        graph[u[i]].append((v[i], w[i]))
        graph[v[i]].append((u[i], w[i]))
    INF = float('inf')
    dist1 = [INF] * (N + 1)
    dist2 = [INF] * (N + 1)
    pq = PriorityQueue()
    dist1[S] = 0
    pq.put((0, S))
    while not pq.empty():
        cost, node = pq.get()
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist1[neighbor]:
                dist2[neighbor] = dist1[neighbor]
                dist1[neighbor] = new_cost
                pq.put((new_cost, neighbor))
            elif dist1[neighbor] < new_cost < dist2[neighbor]:
                dist2[neighbor] = new_cost
                pq.put((new_cost, neighbor))
    if dist2[D] != INF:
        print(dist2[D])
    else:
        print(-1)
N, M, S, D = map(int, input().split())
u = []
v = []
w = []
for _ in range(M):
    a, b, c = map(int, input().split())
    u.append(a)
    v.append(b)
    w.append(c)
second_shortest_path(N, M, S, D, u, v, w)
