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

    for i in range(k):
        x, y = map(int, input().split())

        arr[y + 1][x + 1] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr[j][i] == 1:
                bfs(arr, i, j)
                result += 1

    print(result)
