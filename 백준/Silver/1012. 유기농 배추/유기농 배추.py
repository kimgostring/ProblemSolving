from collections import deque


def bfs(arr, x, y):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            newX, newY = x + dx, y + dy

            if arr[newY][newX] == 1:
                arr[newY][newX] += 1
                q.append((newX, newY))


t = int(input())

for _ in range(t):
    result = 0

    m, n, k = map(int, input().split())

    arr = [[0] * (m + 2) for _ in range(n + 2)]
    roots = [0] * k

    for i in range(k):
        x, y = map(int, input().split())
        x += 1
        y += 1

        arr[y][x] = 1
        roots[i] = (x, y)

    for x, y in roots:
        if arr[y][x] == 1:
            bfs(arr, x, y)
            result += 1

    print(result)
