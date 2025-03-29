from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
dest = 0 
board = [[-1] * m for _ in range(n)]  
for i in range(n):
    line = input().rstrip().split(" ")
    for j, char in enumerate(line):
        if char == "2":
            board[i][j] = 0
            dest = (i, j)
        elif char == "0":
            board[i][j] = 0

q = deque([dest])
while q:
    x, y = q.popleft()

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (0 <= nx < n) and (0 <= ny < m) and (board[nx][ny] == -1):
            # 방문 가능
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    print(*board[i])
