from collections import deque

def bfs(start, goal, graph, n):
    color = {i: 0 for i in range(1, n + 1)}
    parent = {i: None for i in range(1, n + 1)}
    q = deque()
    q.append(start)
    color[start] = 1
    parent[start] = -1

    while q:
        x = q.popleft()
        if x == goal:
            break
        for child in graph[x]:
            if color[child] == 0:
                q.append(child)
                color[child] = 1
                parent[child] = x

    if parent[goal] is None:
        return None

    path = []
    cur = goal
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

n, m, S, D, K = map(int, input().split())
dic = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    dic[u].append(v)

for i in dic:
    dic[i].sort()
path1 = bfs(S, K, dic, n)
path2 = bfs(K, D, dic, n)
if not path1 or not path2:
    print(-1)
else:
    full_path = path1 + path2[1:]
    print(len(full_path) - 1)
    print(' '.join(map(str, full_path)))
