from collections import deque;

def bfs(l, start, dest):
    answer = 0;
    
    d = [(1, -2), (1, 2), (2, 1), (2, -1), (-1, -2), (-1, 2), (-2, 1), (-2, -1)];
    visited = [[0] * l for _ in range(l)];
    visited[start[1]][start[0]] = 1;
    
    q = deque([start]);
    while q and not answer:
        x, y = q.popleft();
        if x == dest[0] and y == dest[1]:
            answer = visited[y][x] - 1;
            break;
            
        for dx, dy in d:
            nextX, nextY = x + dx, y + dy;
            
            if not (0 <= nextX < l) or not (0 <= nextY < l):
                continue;
            if visited[nextY][nextX]:
                continue;

            visited[nextY][nextX] = visited[y][x] + 1;
            q.append((nextX, nextY));

    return answer;

tc = int(input());
for _ in range(tc):
    l = int(input());
    start = tuple(map(int, input().split()));
    dest = tuple(map(int, input().split()));
    
    print(bfs(l, start, dest));