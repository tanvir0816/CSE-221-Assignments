def bst(arr,res):
    l=0
    r=len(arr)-1
    if not arr:
        return
    mid=(l+r)//2
    res.append(arr[mid])
    bst(arr[:mid],res)
    bst(arr[mid+1:],res)
N = int(input())
A = list(map(int, input().split()))
    
result = []
bst(A,result)
for i in result:
    print(i,end=" ")
    
