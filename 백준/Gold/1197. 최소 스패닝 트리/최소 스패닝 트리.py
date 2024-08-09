import sys
inputInts = lambda : map(int, sys.stdin.readline().rstrip().split(" "))

V, E = inputInts()
edges = sorted((list(inputInts()) for _ in range(E)), key=lambda x: x[2])

class UnionFind:
    def __init__(self, V):
        self.parents = [i for i in range(V + 1)]
        self.res = [[0, 0] for _ in range(V + 1)] # weights, size

    def find(self, a):
        shouldUpdated = []
        while a != self.parents[a]:
            shouldUpdated.append(a)
            a = self.parents[a]
        for v in shouldUpdated:
            self.parents[v] = a
            
        return a

    def union(self, a, b, w):    
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return self.res[pa]
        elif pa > pb: a, pa, b, pb = b, pb, a, pa
        
        # pa < pb
        self.res[pb] = list(map(sum, zip(self.res[pa], self.res[pb], [w, 1])))
        self.res[pa] = self.res[pb]
        
        self.parents[pb] = pa
        self.find(b)
        
        return self.res[pa]

uf = UnionFind(V)
for a, b, w in edges:
    tw, ts = uf.union(a, b, w)
    
    if ts == V - 1:
        print(tw)
        break