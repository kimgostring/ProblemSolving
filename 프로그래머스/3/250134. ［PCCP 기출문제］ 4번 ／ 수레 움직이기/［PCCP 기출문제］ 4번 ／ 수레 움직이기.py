def solution(maze):
    RED = 0
    BLUE = 1
    WALL = 5
    DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    n = len(maze)
    m = len(maze[0])
    
    start = [0, 0]
    end = [0, 0]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: start[RED] = (i, j)
            elif maze[i][j] == 2: start[BLUE] = (i, j)
            elif maze[i][j] == 3: end[RED] = (i, j)
            elif maze[i][j] == 4: end[BLUE] = (i, j)
        
    ans = 0
    visited = [[[0] * m for _ in range(n)], [[0] * m for _ in range(n)]]
    visited[RED][start[RED][0]][start[RED][1]] = 1
    visited[BLUE][start[BLUE][0]][start[BLUE][1]] = 1
    
    def out_of_maze(x, y):
        return not (0 <= x < n) or not (0 <= y < m)
    def is_same(rx, ry, bx, by):
        return (rx == bx) and (ry == by)
    def is_interchanged(rx, ry, rnx, rny, bx, by, bnx, bny):
        return ((rx, ry) == (bnx, bny)) and ((bx, by) == (rnx, rny))
    def dfs(r, b):        
        nonlocal ans 
        if is_same(*r, *end[RED]) and is_same(*b, *end[BLUE]):
            (rx, ry) = r
            (bx, by) = b
            candidate = max(visited[RED][rx][ry] - 1, visited[BLUE][bx][by] - 1)
            if ans == 0 or ans > candidate:
                ans = candidate
        elif is_same(*r, *end[RED]):
            (x, y) = b
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if out_of_maze(nx, ny) or visited[BLUE][nx][ny] or \
                maze[nx][ny] == WALL or \
                is_same(nx, ny, *r):
                    continue

                visited[BLUE][nx][ny] = visited[BLUE][x][y] + 1
                dfs(r, (nx, ny))
                visited[BLUE][nx][ny] = 0
        elif is_same(*b, *end[BLUE]):
            (x, y) = r
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if out_of_maze(nx, ny) or visited[RED][nx][ny] or \
                maze[nx][ny] == WALL or \
                is_same(nx, ny, *b):
                    continue

                visited[RED][nx][ny] = visited[RED][x][y] + 1
                dfs((nx, ny), b)
                visited[RED][nx][ny] = 0
        else:
            (rx, ry) = r
            (bx, by) = b
            for rdx, rdy in DIRS:
                rnx, rny = rx + rdx, ry + rdy
                if out_of_maze(rnx, rny) or visited[RED][rnx][rny] or \
                maze[rnx][rny] == WALL:
                    continue

                for bdx, bdy in DIRS:
                    bnx, bny = bx + bdx, by + bdy
                    if out_of_maze(bnx, bny) or visited[BLUE][bnx][bny] or \
                    maze[bnx][bny] == WALL or \
                    is_same(rnx, rny, bnx, bny) or \
                    is_interchanged(rx, ry, rnx, rny, bx, by, bnx, bny):
                        continue

                    visited[RED][rnx][rny] = visited[RED][rx][ry] + 1
                    visited[BLUE][bnx][bny] = visited[BLUE][bx][by] + 1
                    dfs((rnx, rny), (bnx, bny))
                    visited[RED][rnx][rny] = 0
                    visited[BLUE][bnx][bny] = 0
    
    dfs(start[RED], start[BLUE]) 
    return ans;