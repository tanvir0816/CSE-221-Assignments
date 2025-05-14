def find(u, parent):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u
def union(u, v, parent, size):
    aa = find(u, parent)
    bb = find(v, parent)
    if aa == bb:
        return False
    if size[aa] < size[bb]:
        aa, bb = bb, aa
    parent[bb] = aa
    size[aa] += size[bb]
    return True
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()  
parent = [i for i in range(N + 1)]
size = [1] * (N + 1)   
fin = 0
for w, u, v in edges:
    if union(u, v, parent, size):
        fin += w   
print(fin)

