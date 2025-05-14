N=int(input())
Alice=input()
tem1=Alice.split()
l1=[]
for i in tem1:
    l1.append(int(i))
M=int(input())
Bob=input()
tem2=Bob.split()
l2=[]
fin=[]
for i in tem2:
    l2.append(int(i))
ali=0
bo=0
while ali<N and bo<M:
    if l1[ali]<=l2[bo]:
        fin.append(l1[ali])
        ali+=1
    else:
        fin.append(l2[bo])
        bo+=1
while ali<N:
    fin.append(l1[ali])
    ali+=1
while bo<M:
    fin.append(l2[bo])
    bo+=1    
for i in fin:
    print(i,end=" ")
