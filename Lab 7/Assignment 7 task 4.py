from collections import deque
def find_min_cost_path(N, M, S, D, weights, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v)
    queue = deque()
    queue.append(S)
    min_cost = [float('inf')] * (N + 1)
    min_cost[S] = weights[S - 1] 
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            new_cost = min_cost[node] + weights[neighbor - 1]
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                queue.append(neighbor)
    return min_cost[D] if min_cost[D] != float('inf') else -1
N, M, S, D = map(int, input().split())
weights = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]
result = find_min_cost_path(N, M, S, D, weights, edges)
print(result)
