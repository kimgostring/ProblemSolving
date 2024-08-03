import sys
input = sys.stdin.readline

n = int(input())

ls = dict()
rs = dict()
for _ in range(n):
    v, l, r = input().rstrip().split(" ")
    ls[v], rs[v] = l, r

def preorder(s):
    if s == ".": return ""
    return s + preorder(ls[s]) + preorder(rs[s])

def inorder(s):
    if s == ".": return ""
    return inorder(ls[s]) + s + inorder(rs[s])
    
def postorder(s):
    if s == ".": return ""
    return postorder(ls[s]) + postorder(rs[s]) + s

print(preorder("A"), inorder("A"), postorder("A"), sep="\n")