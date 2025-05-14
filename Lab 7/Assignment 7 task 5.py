from queue import PriorityQueue

def shortest_path(N, M, u, v, w):
    graph = [[] for _ in range(N + 1)]

    for i in range(M):
        graph[u[i]].append((v[i], w[i]))

    INF = float('inf')
    dist = [[INF] * 2 for _ in range(N + 1)]
    pq = PriorityQueue()
    dist[1][0] = 0
    dist[1][1] = 0
    for to, weight in graph[1]:
        parity = weight % 2
        if dist[to][parity] > weight:
            dist[to][parity] = weight
            pq.put((weight, to, parity))

    while not pq.empty():
        cost, node, prev_parity = pq.get()

        if dist[node][prev_parity] < cost:
            continue

        for to, weight in graph[node]:
            curr_parity = weight % 2
            if curr_parity != prev_parity:
                new_cost = cost + weight
                if dist[to][curr_parity] > new_cost:
                    dist[to][curr_parity] = new_cost
                    pq.put((new_cost, to, curr_parity))

    ans = min(dist[N][0], dist[N][1])
    if ans!=INF:
        print(ans)
    else:
        print(-1)
N, M= map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
w=list(map(int, input().split()))
shortest_path(N, M, u, v, w)