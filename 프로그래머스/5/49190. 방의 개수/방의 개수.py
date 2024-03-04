def solution(arrows):
    DIRS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)];
    
    answer = 0;
    x, y = 0, 0;
    board = dict();
    for d in arrows:
        # x <-> x <-> x 와 같은 식으로 2배수해서 edge를 이을 것
        # 이때, 첫/끝 지점에는 edge 하나 
        # 중간 지점에는 edge 두 개가 이어지게 됨
        # 이미 있는 edge가 아닌 edge가 해당 점에 생기는 case = 방 하나 생김   
        revD = (d + 4) % 8;
        dx, dy = DIRS[d];
        
        if (x, y) in board and d in board[(x, y)]:
            # 이미 방문한 길인 경우, 고려 X
            x += dx * 2;
            y += dy * 2;
            continue;
        
        for i in range(2):
            # i번째 - i+1번째 점 연결
            tempX = x + (dx * (i + 1));
            tempY = y + dy * (i + 1);
            addLineToBoard(tempX - dx, tempY - dy, d, board);
            addLineToBoard(tempX, tempY, revD, board);
        
        notRoomDirs = [[d, revD], [revD]];
        for i in range(2):
            # i번째 점에서 다른 방향으로 그었던 선이 있는지 check
            tempX = x + dx * (i + 1);
            tempY = y + dy * (i + 1);
            for j in board[(tempX, tempY)]: 
                if j not in notRoomDirs[i]:
                    answer += 1;
                    break;
        
        x += dx * 2;
        y += dy * 2;
    
    return answer;

def addLineToBoard(x, y, d, board):
    if (x, y) not in board:
        board[(x, y)] = [d];
    else:
        board[(x, y)].append(d);
            
            
    