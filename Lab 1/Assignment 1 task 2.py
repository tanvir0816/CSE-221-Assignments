x=int(input())
y=[]
for i in range(x):
    k=input()
    temp=k.split()
    if temp[2]=="+":
        a=round((int(temp[1])+int(temp[3])),6)
    elif temp[2]=="-":
        a=round((int(temp[1])-int(temp[3])),6)
    elif temp[2]=="*":
        a=round((int(temp[1])*int(temp[3])),6)
    else:
        a=round((int(temp[1])/int(temp[3])),6)
    y.append(a)
for i in y:
    print(i)