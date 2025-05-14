def solve(a,b,m):
    if b==0:
        return 1
    hal=solve(a,b//2,m)
    hal=(hal*hal)%m
    if b%2==0:
        return hal
    else:
        return (hal*(a%m))%m
    

N=input()
tem=N.split()
a=int(tem[0])
b=int(tem[1])
print(solve(a,b,107))