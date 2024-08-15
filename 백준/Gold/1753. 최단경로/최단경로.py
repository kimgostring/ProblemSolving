import math
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

V, E = map(int, input().split(" "))
start = int(input())
edges = [dict() for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split(" "))
    if v not in edges[u] or w < edges[u][v]:
        edges[u][v] = w

weights = [math.inf] * (V + 1)
weights[start] = 0
h = [(0, start)]
while h:
    w, u = heappop(h)
    if w != weights[u]: continue

    for v, nw in edges[u].items():
        if weights[v] <= weights[u] + nw: continue
        weights[v] = weights[u] + nw
        heappush(h, (weights[v], v))

print(*(weights[i] if weights[i] != math.inf else "INF" for i in range(1, V + 1)), sep="\n")