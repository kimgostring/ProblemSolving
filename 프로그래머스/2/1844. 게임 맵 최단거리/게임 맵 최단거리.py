from collections import deque

def solution(maps):
    return bfs(maps);
    
def bfs(maps):
    Y_MAX = len(maps);
    X_MAX = len(maps[0])
    q = deque([(0, 0, 1)]);
    
    while q:
        now = q.popleft();
        
        # 탐색 성공 
        if now[0] == X_MAX - 1 and now[1] == Y_MAX - 1:
            return now[2];

        for [dx, dy] in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next = (now[0] + dx, now[1] + dy, now[2] + 1);
            
            if not 0 <= next[0] < X_MAX or not 0 <= next[1] < Y_MAX:
                continue;
            if maps[next[1]][next[0]]:
                maps[next[1]][next[0]] = 0;
                q.append(next);
                
    return -1; # 탐색 실패
    