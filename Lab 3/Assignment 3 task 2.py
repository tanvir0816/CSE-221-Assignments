def x(arr,l,r):
    if l >= r:
        return float('-inf')
    if r-l==1: 
        return arr[l]+arr[r]**2
    mid=(l+r)//2
    left=x(arr,l,mid)
    right=x(arr,mid+1,r)
    exception=cross(arr,l,r,mid)
    return(max(left,right,exception))
def cross(arr,l,r,mid):
    
    lemax=float('-inf')
    for i in range(l,mid+1):
        lemax=max(lemax,arr[i])
    sum=float('-inf')
    for j in range(mid+1,r+1):
        sum=max(sum,(lemax+arr[j]**2))
    return sum
N=int(input())
arr = list(map(int, input().split()))
print(x(arr,0,N-1))
