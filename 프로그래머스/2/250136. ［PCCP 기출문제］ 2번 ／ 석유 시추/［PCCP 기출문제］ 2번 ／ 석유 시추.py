from collections import deque

def solution(land):
    LEN_X = len(land[0]);
    LEN_Y = len(land);
    
    d = dict();
    for y in range(LEN_Y):
        for x in range(LEN_X):
            if land[y][x]:
                cols, cnt = bfs(x, y, land);
                for col in cols: 
                    if col not in d:
                        d[col] = cnt;
                    else: 
                        d[col] += cnt;
    
    return max(d.values());

def bfs(x, y, land):    
    LEN_X = len(land[0]);
    LEN_Y = len(land);
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)];
    
    # bfs init
    q = deque();
    q.append((x, y));
    
    # 초기화 
    cnt = 1;
    cols = {x};
    land[y][x] = 0;
    while q:
        x, y = q.popleft();
        
        for dx, dy in DIRS:
            nextX, nextY = x + dx, y + dy;
            if not (0 <= nextX < LEN_X) or not (0 <= nextY < LEN_Y):
                continue;
            if land[nextY][nextX] == 0:
                continue;
                
            land[nextY][nextX] = 0;
            cnt += 1;
            cols.add(nextX);
            q.append((nextX, nextY));
        
    return cols, cnt;