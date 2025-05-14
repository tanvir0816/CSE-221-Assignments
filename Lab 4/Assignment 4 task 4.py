n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
dic={i:[] for i in range(1,n+1)}
for i in range(m):
    dic[u[i]].append(v[i])
    dic[v[i]].append(u[i])
for i,j in dic.items():
    dic[i]=len(j)
x=0
for i,j in dic.items():
    if j%2==1:
        x+=1
if x==0 or (x==2):
    print("YES")
else:
    print("NO")
