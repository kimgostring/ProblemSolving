import sys
input = sys.stdin.readline
INF = 1e12

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
bellman_ford = [INF] * (n + 1)
bellman_ford[1] = 0

for i in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

for _ in range(n - 1):  # 정점 - 1번 돌려봐야 함
    for start in range(1, n + 1):
        for next, time in graph[start]:
            if bellman_ford[start] != INF and bellman_ford[start] + time < bellman_ford[next]:
                bellman_ford[next] = bellman_ford[start] + time

# 음수 사이클이 있는 경우, 무한히 회귀할 수 있음
flag = False
for start in range(1, n + 1):
    for next, time in graph[start]:
        if bellman_ford[start] != INF and bellman_ford[start] + time < bellman_ford[next]:
            flag = True
            break
    if flag:
        break

if flag:
    print(-1)
else:
    for i in range(2, n + 1):
        if bellman_ford[i] >= INF:
            print(-1)
        else:
            print(bellman_ford[i])
