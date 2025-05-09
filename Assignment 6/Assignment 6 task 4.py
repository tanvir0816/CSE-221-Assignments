n, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
subtree_size = [0] * (n + 1)
visited = [False] * (n + 1)
def iterative_dfs(start):
    stack = [(start, 0)]
    parent = [0] * (n + 1)
    while stack:
        node, state = stack.pop()
        if state == 0:
            visited[node] = True
            stack.append((node, 1))
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    parent[neighbor] = node
                    stack.append((neighbor, 0))
        else:
            size = 1
            for neighbor in tree[node]:
                if neighbor != parent[node]:
                    size += subtree_size[neighbor]
            subtree_size[node] = size
iterative_dfs(r)
final=[]
q = int(input())
for _ in range(q):
    x = int(input())
    final.append(subtree_size[x])
for i in final:
    print(i)