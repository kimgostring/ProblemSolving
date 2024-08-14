import math
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dp = [[math.inf] * (n + 1) for _ in range(n + 1)]
path = [[math.inf] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][i] = 0
    path[i][i] = i

for _ in range(m):
    a, b, price = map(int, input().rstrip().split(" "))
    if price >= dp[a][b]: continue
    
    dp[a][b] = price
    path[a][b] = b
    
for mid in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            price = dp[i][mid] + dp[mid][j]
            if price >= dp[i][j]: continue
            
            dp[i][j] = price
            path[i][j] = path[i][mid]
            
def mkPathStr(i, j):
    if i == j or dp[i][j] == math.inf:
        return "0"
    
    s = f'{i}'
    cnt = 1
    while i != j:
        i = path[i][j]
        s += f' {i}'
        cnt += 1
    return f'{cnt} {s}'
            
print(*(" ".join(str(v) if v != math.inf else "0" for v in dp[i][1:]) for i in range(1, n + 1)), sep="\n")
print(*(mkPathStr(i, j) for i in range(1, n + 1) for j in range(1, n + 1)), sep="\n")