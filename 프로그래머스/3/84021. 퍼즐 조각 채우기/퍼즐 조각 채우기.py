from collections import deque
import copy

def solution(game_board, table):
    blanks = findBlanks(game_board);
    return putBlocks(table, blanks);

# bfs로 모든 blanks들 탐색
def findBlanks(board):
    LEN = len(board);
    blanks = [];
    
    for i in range(LEN):
        for j in range(LEN):
            if not board[i][j]:
                blank, size = bfs(board, j, i);
                blanks.append(blank);
            
    return blanks;
    
def putBlocks(board, blanks):
    LEN = len(board);
    answer = 0;

    for i in range(LEN):
        for j in range(LEN):
            if board[i][j]:
                block, size = bfs(board, j, i, findKey=1);

                for r in range(4):
                    # block이 blanks와 일치하는지 확인
                    if block in blanks:
                        blanks.remove(block);
                        answer += size;
                        
                        break;
                    
                    # block을 회전시켜서 확인
                    if r != 3:
                        block = rotate(block);
            
    return answer;
    
def bfs(visited, startX, startY, findKey=0):
    LEN = len(visited);
    DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    
    answer = [];
    q = deque([(startX, startY)]);
    visited[startY][startX] = 1 if findKey == 0 else 0;
    
    while q:
        x, y = q.popleft();
        answer.append((x, y));
        
        for i in range(4):
            dx, dy = DIR[i];
            nextX = x + dx;
            nextY = y + dy;
            
            if not (0 <= nextX < LEN) or not (0 <= nextY < LEN):
                continue;
            if visited[nextY][nextX] != findKey:
                continue;
                    
            visited[nextY][nextX] = 1 if findKey == 0 else 0;
            q.append((nextX, nextY));
        
    # minX, minY를 0으로 보정
    minX, minY = map(min, zip(*answer)); 
    maxX, maxY = map(max, zip(*answer));
    block = [[0] * (maxX - minX + 1) for _ in range(maxY - minY + 1)];
    for x, y in answer:
        block[y - minY][x - minX] = 1;
    
    return block, len(answer);
    
# 반시계방향 회전
def rotate(block): 
    rotatedBlock = list(map(list, zip(*block)));
    rotatedBlock.reverse();
    return rotatedBlock;