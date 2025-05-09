from collections import deque
n,m=map(int,input().split())
dic={i:[] for i in range(1,n+1)}
indegree={i:0 for i in range(1,n+1)}
for i in range(m):
    u,v=map(int,input().split())
    dic[u].append(v)
    indegree[v]+=1
final=[]
q=deque([])
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
while q:
    x=q.popleft()
    final.append(x)
    for i in dic[x]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
if len(final) == n:
    print(' '.join(map(str, final)))
else:
    print(-1)
