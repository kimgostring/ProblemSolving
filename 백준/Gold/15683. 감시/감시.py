n, m = map(int, input().split());
arr = [0] * n;
cctvs = [];
total = 0;
for i in range(n):
    arr[i] = list(map(int, input().split()));
    cctvs += [(val, i, j) for j, val in enumerate(arr[i]) if 0 < val < 6];
    total += arr[i].count(0);
        
def monitor(i, x, y, dirs):
    cnt = 0;
    for dx, dy in dirs:
        nx, ny = x, y;
        while 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 6:
                break;
            elif arr[nx][ny] == 0:
                arr[nx][ny] = i + 10;
                cnt += 1;
            nx, ny = nx + dx, ny + dy;
   
    return cnt;
    
def stopMonitoring(i, x, y, dirs):
    for dx, dy in dirs:
        nx, ny = x, y;
        while 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 6:
                break;
            elif arr[nx][ny] == i + 10:
                arr[nx][ny] = 0;
            nx, ny = nx + dx, ny + dy;
    
def backtracking(i, acc):
    if i == len(cctvs):
        return acc;
    
    answer = acc;
    num, x, y = cctvs[i];
    d = [];
    if num == 1:
        d = [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]];
    elif num == 2:
        d = [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]];
    elif num == 3:
        d = [[(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)]]        
    elif num == 4:
        d = [[(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)]]   
    elif num == 5:
        d = [[(1, 0), (-1, 0), (0, 1), (0, -1)]];
        
    for dirs in d:
        cur = monitor(i, x, y, dirs);
        answer = max(answer, backtracking(i + 1, acc + cur));
        stopMonitoring(i, x, y, dirs);
        
    return answer;

print(total - backtracking(0, 0));