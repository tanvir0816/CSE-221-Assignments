from collections import deque
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
color = {i: -1 for i in range(1, n + 1)} 
maximum = 0
for i in range(1, n + 1):
    if color[i] == -1:
        if not graph[i]:
            maximum += 1
            color[i] = 0
            continue
        queue = deque([i])
        color[i] = 0
        count = [1, 0]

        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if color[i] == -1:
                    color[i] = 1 - color[node]
                    count[color[i]] += 1
                    queue.append(i)
        maximum += max(count)

print(maximum)
