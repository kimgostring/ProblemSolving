from collections import deque;

m, n, h = map(int, input().split());
boxes = [];
start = [];
zeroCnt = 0;
lastDay = 0;
for z in range(h):
    box = [];
    for y in range(n):
        box.append(list(map(int, input().split())));
        start += [(x, y, z) for x, val in enumerate(box[y]) if val == 1];
        zeroCnt += box[y].count(0);
    boxes.append(box);
    
q = deque(start);
d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)];
while zeroCnt != 0 and q:
    x, y, z = q.popleft();
    lastDay = boxes[z][y][x];
    
    for nextX, nextY, nextZ in [(x + dx, y + dy, z + dz) for dx, dy, dz in d]:
        if not (0 <= nextX < m) or not (0 <= nextY < n) or not (0 <= nextZ < h):
            continue;
        if boxes[nextZ][nextY][nextX]:
            continue;
        
        boxes[nextZ][nextY][nextX] = lastDay + 1;
        zeroCnt -= 1;
        q.append((nextX, nextY, nextZ));

print(-1 if zeroCnt else lastDay);