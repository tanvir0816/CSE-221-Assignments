n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    u = list(map(int, input().split()))
    graph[u[0]].append(u[1])
color = {i: 0 for i in range(1, n + 1)}
def dfs(start):
    stack = [(start, 0)] 
    while stack:
        node, idx = stack[-1]
        if color[node] == 0:
            color[node] = 1 
        if idx < len(graph[node]):
            neighbor = graph[node][idx]
            stack[-1] = (node, idx + 1)
            if color[neighbor] == 0:
                stack.append((neighbor, 0))
            elif color[neighbor] == 1:
                return True
        else:
            color[node] = 2 
            stack.pop()
    return False
for i in range(1, n + 1):
    if color[i] == 0:
        if dfs(i):
            print("YES")
            break
else:
    print("NO")
