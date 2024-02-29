from collections import deque
import copy

def solution(game_board, table):
    rotate(table)
    blanks = findBlanks(game_board);
    return putBlocks(table, blanks);

# bfs로 모든 blanks들 탐색
def findBlanks(board):
    LEN = len(board);
    blanks = [];
    
    for i in range(LEN):
        for j in range(LEN):
            if not board[i][j]:
                blank, visited = bfs(board, j, i);
                board = visited;
                blanks.append(blank);
            
    return blanks;
    
def putBlocks(board, blanks):
    LEN = len(board);
    answer = 0;

    for rotationCnt in range(4):
        for i in range(LEN):
            for j in range(LEN):
                if board[i][j]:
                    block, visited = bfs(board, j, i, findKey=1);
                    
                    if block in blanks:
                        board = visited;
                        blanks.remove(block);
                        print(len(block))
                        answer += len(block);
                            
        # board를 회전시켜서 확인
        if rotationCnt != 3:
            board = rotate(board);
            
    return answer;
    
def bfs(board, startX, startY, findKey=0):
    LEN = len(board);
    DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    
    answer = [];
    q = deque([(startX, startY)]);
    visited = copy.deepcopy(board);
    visited[startY][startX] = 1 if findKey == 0 else 0;
    
    while q:
        x, y = q.popleft();
        answer.append((x - startX, y - startY));
        
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
        
    return answer, visited;
    
# 반시계방향 회전
def rotate(board): 
    rotatedBoard = list(map(list, zip(*board)));
    rotatedBoard.reverse();
    return rotatedBoard;
    
    