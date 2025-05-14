n, m, o, p = map(int, input().split())
dic = {i: [] for i in range(1, n + 1)}
u = list(map(int, input().split()))
v = list(map(int, input().split()))
for i in range(m):

    dic[u[i]].append(v[i])
    dic[v[i]].append(u[i])

for i in dic:
    dic[i].sort()

color = {i: 0 for i in range(1, n + 1)}
parent = {i: None for i in range(1, n + 1)}
q = []
a = []

q.append(o)
color[o] = 1
parent[o] = -1
fr=0
while fr<len(q):
    x = q[fr]
    fr+=1
    a.append(x)
    if x == p:
        break    
    for chil in dic[x]:
        if color[chil] == 0:
            q.append(chil)
            color[chil] = 1
            parent[chil] = x
if parent[p] is not None:
    path = []
    cur = p
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print(len(path) - 1)
    for i in path:
        print(i, end=" ")
    print()
else:
    print(-1)
