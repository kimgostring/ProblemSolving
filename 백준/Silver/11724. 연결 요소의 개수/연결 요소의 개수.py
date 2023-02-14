from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]

for i in range(m):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start) # 방향 없는 그래프이므로!


def bfs(node):
    q = deque([node])

    while q:
        start = q.popleft()

        for end in edges[start]:
            if not visited[end]:
                visited[end] = True
                q.append(end)


result = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)
