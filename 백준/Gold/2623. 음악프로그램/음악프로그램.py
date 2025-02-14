from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))

edges = [[] for _ in range(N + 1)]
inDegrees = [0] * (N + 1)
for i in range(M):
    subOrders = map(int, input().split(" "))
    subOrders.__next__() # 가수의 수 날리기
    
    prev = subOrders.__next__() 
    for now in subOrders:
        edges[prev].append(now)
        inDegrees[now] += 1
        prev = now

# 처음부터 inDegree = 0인 애들 queue에 넣기
candidates = deque()
for i, inDegree in enumerate(inDegrees):
    if i != 0 and inDegree == 0:
        candidates.append(i)

ans = []
while candidates:
    now = candidates.popleft()
    ans.append(now)

    for next in edges[now]:
        inDegrees[next] -= 1
        if inDegrees[next] == 0:
            candidates.append(next)

if len(ans) < N:
  print(0)
else:
  print("\n".join(map(str, ans)))
