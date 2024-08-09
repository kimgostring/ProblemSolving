import sys
inputInts = lambda : map(int, sys.stdin.readline().rstrip().split(" "))

V, E = inputInts()
edges = sorted((list(inputInts()) for _ in range(E)), key=lambda x: x[2])

class UnionFind:
    def __init__(self, V):
        self.parents = [i for i in range(V + 1)]

    def find(self, a):
        shouldUpdated = []
        while a != self.parents[a]:
            shouldUpdated.append(a)
            a = self.parents[a]
        for v in shouldUpdated:
            self.parents[v] = a
            
        return a

    def union(self, a, b):    
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return False
        elif pa > pb: a, pa, b, pb = b, pb, a, pa
        
        # pa < pb
        self.parents[pb] = pa
        self.find(b)
        
        return True

uf = UnionFind(V)
tw, ts = 0, 0
for a, b, w in edges:
    if uf.union(a, b):
        tw += w
        ts += 1
    if ts == V - 1:
        print(tw)
        break