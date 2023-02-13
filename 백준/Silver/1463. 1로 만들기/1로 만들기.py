from collections import deque

n = int(input())


def bfs(n):
    cnt = 0
    q = deque([(n, cnt)])

    while q:
        n, cnt = q.popleft()

        if n == 1:
            break

        if n % 3 == 0:
            q.append((n // 3, cnt + 1))
        if n % 2 == 0:
            q.append((n // 2, cnt + 1))
        q.append((n - 1, cnt + 1))

    return cnt


print(bfs(n))
