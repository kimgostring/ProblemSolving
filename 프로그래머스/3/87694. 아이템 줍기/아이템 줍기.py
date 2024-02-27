from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1. 판 만들기
    board = [[0] * 102 for _ in range(102)];
    for rec in rectangle:
        minX, minY, maxX, maxY = map(lambda x: x << 1, rec);
        
        for i in range(minX, maxX + 1):
            for j in range(minY, maxY + 1):
                board[j][i] = 1;
    
    # 2. bfs     
    return bfs(board, characterX << 1, characterY << 1, itemX << 1, itemY << 1);

def bfs(board, charX, charY, itemX, itemY): 
    DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    DIR_8 = DIR + [(1, 1), (1, -1), (-1, 1), (-1, -1)];
    
    q = deque([(charX, charY, 0)]);
    board[charY][charX] = 0; # visited
    
    while q:
        x, y, answer = q.popleft();
        
        # 종료 조건
        if x == itemX and y == itemY:
            return answer;
        
        # 4방면 이동
        for dx, dy in DIR:
            newX = x + (dx << 1);
            newY = y + (dy << 1);
            
            if not (2 <= newX <= 100) or not (2 <= newY <= 100):
                continue;
            if board[newY][newX]: # not visited
                midX = x + dx;
                midY = y + dy;
                if not board[midY][midX]: # 다각형의 둘레가 아닌 경우 
                    continue;
                if sum([board[midY + dy][midX + dx] for dx, dy in DIR_8]) >= 7: # 테두리가 아닌 경우 (지나온 길 제외, 다 1일 경우)
                    continue;
                board[newY][newX] = 0;
                q.append((newX, newY, answer + 1));
            
            