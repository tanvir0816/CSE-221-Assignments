N=input()
tem=N.split()
n=int(tem[0])
s=int(tem[1])
m=input()
tem=m.split()
lis=[]
for i in tem:
    lis.append(int(i))
maxlen=0
cur=0
i=0
j=0
while j < len(lis):
    cur += lis[j]
    while cur > s and i <= j:
        cur -= lis[i]
        i += 1   
    maxlen = max(maxlen, j - i + 1)
    j += 1
print(maxlen)