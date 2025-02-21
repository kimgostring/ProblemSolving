from heapq import heappush, heappop 
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 1e9

N, E = map(int, input().split(" "))
edges = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    start, end, dist = map(int, input().split(" "))
    edges[start].append([end, dist])
    edges[end].append([start, dist])
u, v = map(int, input().split(" "))

def dijkstra(start):
    dists = [INF] * (N + 1)
    h = [(0, start)]
    while h:
        dist, now = heappop(h)
        if dist > dists[now]:
            continue

        dists[now] = dist
        for next, nextDist in edges[now]:
            candidate = dist + nextDist
            if candidate < dists[next]:
                dists[next] = candidate
                heappush(h, (candidate, next))

    return dists

distsToU = dijkstra(u)
distsToV = dijkstra(v)
ans = min(distsToU[1] + distsToV[N], distsToV[1] + distsToU[N]) + distsToU[v]
print(ans if ans < INF else -1)
