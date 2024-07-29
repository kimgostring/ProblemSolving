import sys;
input = sys.stdin.readline;
from collections import deque;

n, m = map(int, input().split(" "));
pic = [list(map(int, input().split(" "))) for _ in range(n)];

def bfs(x, y):
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    d = 1;
    
    q = deque([(x, y)]);
    pic[x][y] = 0;
    while q:
        x, y = q.popleft();
        
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy;
            if not 0 <= nx < n or not 0 <= ny < m:
                continue;
            if not pic[nx][ny]:
                continue;

            q.append((nx, ny));
            pic[nx][ny] = 0;
            d += 1;
    
    return d;

c = 0;
d = 0;
for x in range(n):
    for y in range(m):
        if not pic[x][y]:
            continue;
        
        c += 1;
        d = max(d, bfs(x, y));

print(c, d, sep="\n");