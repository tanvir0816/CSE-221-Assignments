n=input()
x,y=n.split()
x=int(x)
y=int(y)
z=input()
tem=z.split()
arr=[]
for i in tem:
    arr.append(int(i))
oup=[]
for i in range(y):
    l=input()
    yo,da=l.split()
    yo=int(yo)
    da=int(da)
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= yo:
            right = mid
        else:
            left = mid + 1
    lower = left  
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > da:
            right = mid
        else:
            left = mid + 1
    upper = left
    
    oup.append(upper-lower)

for i in oup:
    print(i)
