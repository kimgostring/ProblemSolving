from collections import deque  # deque 추가해봄

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

arr = [0] * n
dirrection = [[0, 1], [0, -1], [1, 0], [-1, 0]]
totalCnt = 0  # 0이 아닌 경우(익은 토마토 혹은 빈 공간)의 개수
roots = deque()  # 탐색에 사용됨

for i in range(n):
    arr[i] = list(map(int, input().split()))

    for j in range(m):
        if arr[i][j] == 1:
            roots.append([i, j])
            totalCnt += 1
        elif arr[i][j] == -1:
            totalCnt += 1

result = 0
while totalCnt < n * m:
    cnt = 0
    newRoots = deque()

    for root in roots:
        i, j = root

        # 익은 토마토, 옆의 안 익은 애들을 익힐 수 있음
        for k in range(4):
            nowX, nowY = dirrection[k][0] + \
                i, dirrection[k][1] + j

            if nowX < 0 or nowY < 0 or nowX >= n or nowY >= m:
                continue
            elif arr[nowX][nowY] == 0:
                arr[nowX][nowY] = 1
                newRoots.append([nowX, nowY])
                cnt += 1

    if cnt == 0:
        # 더 이상 토마토가 익을 수 없음
        result = -1
        break

    totalCnt += cnt
    result += 1

    roots = newRoots

print(result)
