N=int(input())
fin=[]
for i in range(N):
    x=input()
    left=0
    right=(len(x))-1
    first=-1
    while left<=right:
        mid = (left + right) // 2
        if x[mid] == '1':
            first = mid 
            right = mid - 1 
        else:
            left = mid + 1
    
    if first!=-1:
        fin.append(first+1)
    else:
        fin.append(-1)
for i in fin:
    print(i)