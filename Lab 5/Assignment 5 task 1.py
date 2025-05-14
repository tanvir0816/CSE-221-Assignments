n, m = map(int, input().split())
dic = {i: sorted([]) for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)
color = {i: 0 for i in range(1, n + 1)}
q = []
a = []
q.append(1)
color[1] = 1

while q:
    x = q.pop(0)
    a.append(x)
    for chil in dic[x]:
        if color[chil] == 0:
            q.append(chil)
            color[chil] = 1
print(' '.join(map(str, a)))
