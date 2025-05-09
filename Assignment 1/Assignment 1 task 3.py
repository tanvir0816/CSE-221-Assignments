k=input()
x=k.split()
a=int(x[0])
b=int(x[1])
l=input()
lis=l.split()
fin=[]
for i in range(b-1,-1,-1):
    fin.append(lis[i])
for i in fin:
    print(i,end=" ")
