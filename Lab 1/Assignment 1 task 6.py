x=int(input())
y=input()
z=input()
id=y.split()
mark=z.split()
tup=[]
for i in range(x):
    temp=[int(id[i]),int(mark[i])]
    tup.append(temp)
def selection(arr):
    n=len(arr)
    cou=0
    for i in range(n-1):
        temp=i
        for j in range(i+1,n):
            if arr[j][1] > arr[temp][1] or (arr[j][1] == arr[temp][1] and arr[j][0] < arr[temp][0]):
                temp = j
        if temp != i:
            arr[i], arr[temp] = arr[temp], arr[i]
            cou += 1
    return cou 
x=selection(tup)
print(f"Minimum swaps: {x}")
for i in range(len(tup)):
    print(f"ID: {tup[i][0]} Mark: {tup[i][1]}")