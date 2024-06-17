from collections import deque;

d = [(1, 0), (-1, 0), (0, 1), (0, -1)];
r, c = map(int, input().split());
j, f, board = [], [], [];
for y in range(r):
    line = input()
    
    j += [(x, y) for x, val in enumerate(line) if val == "J"];
    f+= [(x, y) for x, val in enumerate(line) if val == "F"];
    board.append([-1 if char == "#" else 0 for char in line]);

# 불이 언제 도달하는지 board에 기록
for x, y in f:
    board[y][x] = 1;

q = deque(f);
while q:
    x, y = q.popleft();
    for nextX, nextY in [(x + dx, y + dy) for dx, dy in d]:
        if not (0 <= nextX < c) or not (0 <= nextY < r):
            continue;
        if board[nextY][nextX] != 0:
            continue;
        
        board[nextY][nextX] = board[y][x] + 1;
        q.append((nextX, nextY));

# 불타지 않고 갈 수 있는지 check
answer = False;
visited = [[0] * c for _ in range(r)];
visited[j[0][1]][j[0][0]] = 1;

q = deque(j);
while q and not answer:
    x, y = q.popleft();
    for nextX, nextY in [(x + dx, y + dy) for dx, dy in d]:
        if not (0 <= nextX < c) or not (0 <= nextY < r):
            answer = visited[y][x];
            break;
        if visited[nextY][nextX]:
            continue;
        if visited[y][x] + 1 >= board[nextY][nextX] and board[nextY][nextX] != 0:
            continue;
        
        visited[nextY][nextX] = visited[y][x] + 1;
        q.append((nextX, nextY));

print("IMPOSSIBLE" if not answer else answer);