n,m=map(int,input().split())
tem=[[0]*n for i in range(n)]

for x in range(m):
    u,v,w=map(int,input().split())
    tem[u-1][v-1]=w
for i in tem:
    for j in i:
        print (j, end=" ")
    print("")
    