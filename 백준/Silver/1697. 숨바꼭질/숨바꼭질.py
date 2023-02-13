from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001


def bfs(n, k):
    cnt = 0
    q = deque([(n, cnt)])

    while q:
        x, cnt = q.popleft()

        if x == k:
            # 도착
            break

        for i in (x * 2, x - 1, x + 1):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                q.append((i, cnt + 1))

    return cnt


print(bfs(n, k))
