n=int(input())
matrix=[[0]*n for i in range(n)]
for j in range(n):
    tem = list(map(int, input().split()))
    for k in range(1,len(tem)):
        matrix[j][tem[k]]=1

for i in matrix:
    for j in i:
        print (j, end=" ")
    print("")