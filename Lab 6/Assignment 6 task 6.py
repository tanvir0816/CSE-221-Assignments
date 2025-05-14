from queue import PriorityQueue 
q = PriorityQueue()
n=int(input())
words=[]
graph={}
indegree={}
final=[]
for i in range(n):
    words.append(input())
for i in words:
    for j in i:
        if j not in graph:
            graph[j]=[]
            indegree[j]=0
inv=False
for i in range(len(words)-1):
    w1=words[i]
    w2=words[i+1]
    mini=min(len(w1),len(w2))
    diff=False
    for i in range(mini):
        if w1[i]==w2[i]:
            pass
        else:
            if w2[i] not in graph[w1[i]]:
                graph[w1[i]].append(w2[i])
                indegree[w2[i]]+=1
            diff=True
            break
    if not diff and len(w1)>len(w2):
        inv=True
        break
if inv:
    print(-1)
else:
    for x in indegree:
        if indegree[x]==0:
            q.put(x)
    while not q.empty():
        xx=q.get()
        final.append(xx)
        for i in graph[xx]:
            indegree[i]-=1
            if indegree[i]==0:
                q.put(i)
    if len(final) == len(indegree):
        print(''.join(map(str, final)))
    else:
        print(-1)
