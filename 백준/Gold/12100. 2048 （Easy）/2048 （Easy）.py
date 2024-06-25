import copy;
from enum import Enum;

LEFT = 0;
RIGIT = 1;
UP = 2;
DOWN = 3;

n = int(input());
arr = [];
biggest = 0;
for i in range(n):
    arr.append(list(map(int, input().split())));
    biggest = max(biggest, *arr[i]);

def move(arr, d):
    global biggest;
    new = copy.deepcopy(arr);
    
    # x, y 뒤집기
    if d == UP or d == DOWN: 
        new = list(map(list, zip(*new)));
    
    # 1. 한 방향으로 옮기기
    for i in range(n):
        new[i] = [x for x in new[i] if x != 0];

    # 2. 앞/뒤에서부터 합치기 & 부족한 길이만큼 뒤/앞에 0 추가
    if d == LEFT or d == UP:
        # 앞에서부터 합치고, 뒤쪽에 0 추가
        for i in range(n):
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
    else:
        # 뒤에서부터 합치고, 앞쪽에 0 추가
        for i in range(n):
            l = len(new[i]);
            j = l - 1;
            tmp = [];
            while j >= 0:
                if j > 0 and new[i][j] == new[i][j - 1]:
                    tmp.append(new[i][j] << 1);
                    if tmp[-1] > biggest:
                        biggest = tmp[-1];
                    j -= 2;
                else:
                    tmp.append(new[i][j]);
                    j -= 1;
                
            new[i] = [0] * (n - len(tmp)) + tmp[::-1];
    
    # x, y 뒤집기
    if d == UP or d == DOWN: 
        new = list(map(list, zip(*new)));
    
    return new;

def backtracking(arr, moveCnt):
    if moveCnt == 5:
        return;
    
    for d in range(4):
        new = move(arr, d);
        # print(moveCnt);
        # print(*new, sep="\n");
        backtracking(new, moveCnt + 1);
    
backtracking(arr, 0);
print(biggest);