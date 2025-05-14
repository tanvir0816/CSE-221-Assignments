k=int(input())
N=[]
for i in range(k):
    n=int(input())
    N.append(n)
for i in N:
    if i%2==0:
        print (i,"is an Even number.")
    else:
        print(i,"is an Odd number.")