import sys
input = sys.stdin.readline
INF = 2e10

n, m, r = map(int, input().split(" "))
items = list(map(int, input().split(" ")))
floyd = [[INF] * n for _ in range(n)]
for i in range(n):
  floyd[i][i] = 0

for _ in range(r):
  a, b, l = map(int, input().split(" "))
  a -= 1
  b -= 1
  floyd[a][b] = l
  floyd[b][a] = l

# floyd warshall
for k in range(n):
  for i in range(n):
    for j in range(n):
      floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])        

# 최종 결과 순회하며, m 이하인 거리의 노드들 계산 
ans = 0
for start, dists in enumerate(floyd):
  curAns = 0
  for i, dist in enumerate(dists):
    if dist <= m:
      curAns += items[i]
  ans = max(ans, curAns)
  
print(ans)
