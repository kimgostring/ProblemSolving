from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split(" "))
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split(" "))
    arr[s].append(e)
    arr[e].append(s)
for i in range(1, n + 1):
    arr[i].sort()

def dfs(v):
    visited = [False] * (n + 1)
    res = []
    s = [v]
    
    while s:
        now = s.pop()
        if visited[now]: 
            continue
        
        visited[now] = True
        res.append(now)
                
        for nx in reversed(arr[now]):
            if visited[nx]:
                continue
            s.append(nx)
    
    return res

def bfs(v):
    visited = [False] * (n + 1)
    res = [v]
    q = deque([v])
    visited[v] = True
    
    while q:
        now = q.popleft()
        
        for nx in arr[now]:
            if visited[nx]:
                continue    
            q.append(nx)
            
            visited[nx] = True
            res.append(nx)
            
    return res
    
print(*dfs(v), sep=" ")
print(*bfs(v), sep=" ")