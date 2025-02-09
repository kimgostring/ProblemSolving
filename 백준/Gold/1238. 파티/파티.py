from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = 10000000
N, M, X = map(int, input().split(" "))
data = [map(int, input().split(" ")) for _ in range(M)]

edges = [[] for _ in range(N + 1)]
reverseEdges = [[] for _ in range(N + 1)]
for s, e, w in data:
  edges[s].append((w, e))
  reverseEdges[e].append((w, s))

def dijkstra(edges, dest):
  # ans
  dist = [INF] * (N + 1)
  
  # 초기화 
  q = [(0, X)]
  cnt = 0
  
  while cnt < N - 1:
    # 최소값 선택
    w, v = heappop(q)
    if dist[v] < w: # 이미 방문한 Node
      continue
    dist[v] = w
    cnt += 1
    
    # dist 갱신
    for nextW, nextV in edges[v]:
      d = dist[v] + nextW
      if d < dist[nextV]: 
        dist[nextV] = d
        heappush(q, (dist[nextV], nextV))

  return dist
  
timeToGetX = dijkstra(reverseEdges, X)
timeToComebackFromX = dijkstra(edges, X)

ans = max([timeToGetX[i] + timeToComebackFromX[i] for i in range(1, N + 1)])
print(ans)
