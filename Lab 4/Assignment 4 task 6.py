n=int(input())
w=list(map(int,input().split()))
available=[[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
final=[]
for dx, dy in available:
    x = w[0] + dx
    y = w[1] + dy
    if 1 <= x <= n and 1 <= y <= n:
        final.append([x, y])
print(len(final))
for x, y in sorted(final):
    print(x, y)