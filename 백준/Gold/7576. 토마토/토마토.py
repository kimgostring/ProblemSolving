from collections import deque  # deque 추가해봄

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = deque()  # 탐색에 사용됨

arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])

result = -1  # 토마토가 하나 이상 있는 경우만 주어지므로
while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()

        # 익은 토마토, 옆의 안 익은 애들을 익힐 수 있음
        for dx, dy in direction:
            nowX, nowY = dx + x, dy + y

            if nowX < 0 or nowY < 0 or nowX >= n or nowY >= m:
                continue
            elif arr[nowX][nowY] == 0:
                arr[nowX][nowY] = 1
                queue.append([nowX, nowY])

    result += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result = -1
            break

print(result)
