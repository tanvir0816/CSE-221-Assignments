inp=input()
sp=inp.split()
n=int(sp[0])
s=int(sp[1])
list=input()
lis=[]
tem=list.split()
for i in tem:
    lis.append(int(i))
i=0
j=len(lis)-1
while i<j:
    cur_sum=lis[i]+lis[j]
    if cur_sum<s:
        i+=1
    elif cur_sum>s:
        j-=1
    elif cur_sum==s:
        print(i+1,j+1)
        break
if cur_sum!=s:
    print(-1)