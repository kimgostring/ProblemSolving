n = int(input());
arr = [];
biggest = 0;
for i in range(n):
    arr.append(list(map(int, input().split())));
    biggest = max(biggest, *arr[i]);

def rotate(arr, d):    
    new = [[0] * n for _ in range(n)];
    if d == 0:
        for i in range(n):
            for j in range(n):
                new[i][j] = arr[i][j];
    elif d == 1:
        for i in range(n):
            for j in range(n):
                new[i][j] = arr[j][n - 1 - i];
    elif d == 2:
        for i in range(n):
            for j in range(n):
                new[i][j] = arr[n - 1 - i][n - 1 - j];
    elif d == 3:
        for i in range(n):
            for j in range(n):
                new[i][j] = arr[n - 1 - j][i];
    
    return new;
        
def move(arr, d):
    global biggest;
    new = rotate(arr, d);
    cntNum = 0;
    isChanged = False;
    
    for i in range(n):
        orig = new[i][:];
        new[i] = [x for x in new[i] if x != 0];
        
        l = len(new[i]);
        j = 0;
        tmp = [];
        while j <= l - 1:
            if j < l - 1 and new[i][j] == new[i][j + 1]:
                tmp.append(new[i][j] << 1);
                if tmp[-1] > biggest:
                    biggest = tmp[-1];
                j += 2;
            else:
                tmp.append(new[i][j]);
                j += 1;
        
        new[i] = tmp + [0] * (n - len(tmp));
        cntNum += len(tmp);
        isChanged = isChanged or orig != new[i];
            
    hasPossibility = cntNum > 1 and isChanged;
    return new, hasPossibility;

def backtracking(arr, moveCnt):
    if moveCnt == 5:
        return;
    
    for d in range(4):
        new, hasPossibility = move(arr, d);
        if hasPossibility:
            backtracking(new, moveCnt + 1);
    
backtracking(arr, 0);
print(biggest);