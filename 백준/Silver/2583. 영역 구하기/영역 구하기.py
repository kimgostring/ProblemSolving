from collections import deque
import sys
input = sys.stdin.readline

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

m, n, k = map(int, input().rstrip().split(" "))
checkIsInside = lambda x, y: (0 <= x < m) and (0 <= y < n)

board = [[False] * n for _ in range(m)]
for _ in range(k):
  sx, sy, ex, ey = map(int, input().rstrip().split(" "))
  for i in range(sy, ey):
    for j in range(sx, ex):
      board[i][j] = True

ans = []
for i in range(m):
  for j in range(n):
      if board[i][j]:
        continue

      area = 1
      board[i][j] += 1
      q = deque([(i, j)])
      while q:
        x, y = q.popleft()

        for dx, dy in DIRS:
          nx, ny = x + dx, y + dy
          if checkIsInside(nx, ny) and not board[nx][ny]:
            area += 1
            board[nx][ny] = True
            q.append((nx, ny))

      ans.append(area)

ans.sort()
print(len(ans))
print(" ".join(map(str, ans)))
