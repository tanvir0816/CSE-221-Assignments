n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
dic={i:[] for i in range(1,n+1)}
for i in range(m):
    dic[u[i]].append((v[i],w[i]))
for i in range(1,n+1):
    k=" ".join(f"({a},{b})" for a,b in dic[i])
    print(f"{i}: {k}")