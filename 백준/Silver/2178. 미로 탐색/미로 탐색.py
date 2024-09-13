from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, m, visited):
    q = deque([(0, 0, 1)])
    visited[0][0] = True

    while q:
        x, y, cnt = q.popleft()
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < n) or not (0 <= ny < m):
                continue
            if visited[nx][ny]:
                continue
            if nx == n - 1 and ny == m - 1:
                return cnt + 1
            
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))
        
    return -1

n, m = map(int, input().split(" "))
board = [list(map(lambda x: False if x == "1" else True, input().rstrip())) for _ in range(n)]

print(bfs(n, m, board))