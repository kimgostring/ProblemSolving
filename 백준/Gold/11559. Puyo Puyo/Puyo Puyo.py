from collections import deque
import sys
input = sys.stdin.readline

# x, y 뒤집어서 입력받음 (중력 적용 쉽게 하기 위해)
field = [deque() for _ in range(6)]
for _ in range(12):
    line = input().rstrip()
    for i in range(6):
        if line[i] != ".":
            field[i].appendleft(line[i])

def bfs(x, y, visited):
    global field
    
    color = field[x][y]
    delPuyos = {(x, y)}
    visited[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        
        for [dx, dy] in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < 6) or not (0 <= ny < len(field[nx])):
                continue
            if field[nx][ny] != color or visited[nx][ny]:
                continue
            
            delPuyos.add((nx, ny))
            visited[nx][ny] = True
            q.append((nx, ny))
    
    return delPuyos
    
def findChainAndPop():
    global field
    
    found = False
    visited = [[False] * 12 for _ in range(6)]
    delPuyos = set()
    for x in range(6):
        for y in range(len(field[x])):
            if visited[x][y]:
                continue
            
            chainPuyos = bfs(x, y, visited)
            if len(chainPuyos) >= 4:
                found = True
                delPuyos = delPuyos | chainPuyos
            
    if not found:
        return False 
    
    for x in range(6):
        delCnt = 0
        newLine = []
        for y in range(len(field[x])):
            if (x, y) not in delPuyos:
                newLine.append(field[x][y])
        field[x] = newLine
            
    return True

ans = 0
while findChainAndPop():
    ans += 1

print(ans)