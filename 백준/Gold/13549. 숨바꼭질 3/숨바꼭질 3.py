from collections import deque

MAX = 100000
INF = 100000

def bfs_01(n, k):
    dist = [INF] * (MAX + 1)
    q = deque()

    q.append(n)
    dist[n] = 0
    while q:
        x = q.popleft()
        if x == k:
            break

        for nx in [x - 1, x + 1]:
            if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
                dist[nx] = dist[x] + 1
                q.append(nx)

        nx = x * 2
        if 0 <= nx <= MAX and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            q.appendleft(nx)

    return dist[k]

n, k = map(int, input().split(" "))
print(bfs_01(n, k))
