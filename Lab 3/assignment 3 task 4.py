def mod_exp(a, n, m):
    result = 1
    base = a % m
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % m
        base = (base * base) % m
        n //= 2
    return result

def sum_mod_exp(a, n, m):
    if n == 1:
        return a % m
    
    half_sum = sum_mod_exp(a, n // 2, m)
    half_pow = mod_exp(a, n // 2, m)
    
    if n % 2 == 0:
        return (half_sum * (1 + half_pow)) % m
    else:
        return (half_sum * (1 + half_pow) + mod_exp(a, n, m)) % m

def solve(a, n, m):
    return sum_mod_exp(a, n, m)

N = int(input())
arr = []
for _ in range(N):
    a, n, m = map(int, input().split())
    arr.append(str(solve(a, n, m)))

print("\n".join(arr))
