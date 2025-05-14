def find(u, parent):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v, parent, size):
    aa = find(u, parent)
    bb = find(v, parent)
    if aa != bb:
        if size[aa] < size[bb]:
            aa, bb = bb, aa
        parent[bb] = aa
        size[aa] += size[bb]
    return size[aa]

N, K = map(int, input().split())
parent = [i for i in range(N + 1)]
size = [1] * (N + 1)
x=[]
for _ in range(K):
    a, b = map(int, input().split())
    res = union(a, b, parent, size)
    x.append(res)
for i in x:
    print (i)

