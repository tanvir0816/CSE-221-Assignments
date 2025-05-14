import math
n,q=map(int,input().split())
dic={i:[] for i in range(1,n+1)}
for i,j in dic.items():
    for k in range(1,n+1):
        if i!=k and math.gcd(i,k)==1:
            j.append(k)
tt=[]
for i in range(q):
    a=list(map(int,input().split()))
    tt.append(a)
for i in tt:
    x=i[0]
    y=i[1]
    if y<=len(dic[x]):
        print((dic[x][y-1]))
    else:
        print(-1)