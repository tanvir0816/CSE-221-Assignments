n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
dic={i:0 for i in range(1,n+1)}
for i in range(m):
    dic[u[i]]-=1
    dic[v[i]]+=1
for i,j in dic.items():
    print(j,end=" ")