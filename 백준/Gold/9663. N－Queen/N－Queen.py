n = int(input());
colVisited = [False] * n;
upDiagVisited = [False] * 2 * n;
downDiagVisited = [False] * 2 * n;

def backtracking(row):
    if row == n:
        return 1;
    
    cnt = 0;
    for col in range(n):
        if colVisited[col] or upDiagVisited[row + col] or downDiagVisited[n + row - col]:
            continue;
        
        colVisited[col] = True;
        upDiagVisited[row + col] = True;
        downDiagVisited[n + row - col] = True;
        
        cnt += backtracking(row + 1);
        
        colVisited[col] = False;
        upDiagVisited[row + col] = False;
        downDiagVisited[n + row - col] = False;
        
    return cnt;

print(backtracking(0));