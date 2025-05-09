def bubbleSort(arr):                                                   
    for i in range(len(arr)-1):
        flag=0 
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag=1
        if not flag:
            break
x=int(input())
y=input()
temp=y.split()
arr=[int(i) for i in temp]
bubbleSort(arr)
for i in arr:
    print(i,end=" ")