n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
dic={i:sorted([]) for i in range(1,n+1)}
for i in range(m):
    dic[u[i]].append(v[i])
    dic[v[i]].append(u[i])
color = {i: 0 for i in range(1, n + 1)}
a = []
stak=[1]
while stak:
    x = stak.pop()
    if not color[x]:
        color[x]=1
        a.append(x)
        for aa in reversed(dic[x]):
            if not color[aa]:
                stak.append(aa)
print(' '.join(map(str, a)))