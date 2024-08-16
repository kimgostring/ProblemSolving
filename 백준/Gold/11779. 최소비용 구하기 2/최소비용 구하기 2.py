from heapq import heappush, heappop 
import math
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split(" "))
    edges[a].append((b, w))
start, end = map(int, input().split(" "))

weights = [math.inf] * (n + 1)
weights[start] = 0
prev = [math.inf] * (n + 1)
prev[start] = start
h = [(0, start)]
while h:
    w, a = heappop(h)
    if weights[a] != w: continue

    for b, bw in edges[a]:
        if weights[b] <= w + bw: continue
    
        weights[b] = w + bw
        prev[b] = a
        heappush(h, (weights[b], b))

pathStr = f'{end}'
cnt = 1
i = end
while i != start:
    i = prev[i]
    pathStr = f'{i} ' + pathStr
    cnt += 1
    
print(weights[end], cnt, pathStr, sep="\n")