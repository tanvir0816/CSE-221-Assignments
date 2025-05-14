def merge(a, b):
    # write your code here
    # a and b are two sorted list
    # merge function will return a sorted list after merging a and b
    i,j=0,0
    temp=[]
    inv=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            temp.append(a[i])
            i+=1
        else:
            temp.append(b[j])
            inv+=len(a)-i
            j+=1
    while i<len(a):
        temp.append(a[i])
        i+=1
    while j<len(b):
        temp.append(b[j])
        j+=1
    
    return temp,inv
        
def mergeSort(arr):
    if len(arr) <= 1:
        return arr,0
    else:
        mid = len(arr)//2
        a1,q = mergeSort(arr[:mid]) 
        a2,w = mergeSort(arr[mid:])
        merg,qw= merge(a1, a2)
        z=q+w+qw
    return merg,z
N=int(input())
y=input()
tem=y.split()
arr=[]
for i in tem:
    arr.append(int(i))
sorted, inversion= mergeSort(arr)

print(inversion)
print(" ".join(map(str, sorted)))