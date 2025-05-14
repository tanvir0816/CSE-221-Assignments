def solve(inorder,preorder):
    if not inorder:
        return []
    root=preorder[0]
    x=inorder.index(root)
    Lpost=solve(inorder[0:x],preorder[1:x+1])
    Rpost=solve(inorder[x+1:],preorder[x+1:])
    return Lpost+Rpost+[root]
N=int(input())
iin = list(map(int, input().split()))
pre = list(map(int, input().split()))
post=solve(iin,pre)
for i in post:
    print(i,end=" ")
