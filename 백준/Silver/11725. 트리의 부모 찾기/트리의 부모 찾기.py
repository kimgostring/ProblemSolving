from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)    
    
def bfs(s):
    parents = [0] * (n + 1)
    q = deque([1])
    while q:
        v = q.popleft()
        
        for cv in edges[v]:
            if parents[cv]: continue
            
            q.append(cv)
            parents[cv] = v
        
    return parents

print(*bfs(1)[2:], sep="\n")