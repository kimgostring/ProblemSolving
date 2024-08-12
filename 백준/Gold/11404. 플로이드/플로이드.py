import math
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dp = [[math.inf] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0
for _ in range(m):
    a, b, p = map(int, input().rstrip().split(" "))
    dp[a][b] = min(dp[a][b], p)

for mid in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid][j])
           
print(*(" ".join(str(v) if v != math.inf else "0" for v in dp[i][1:]) for i in range(1, n + 1)), sep="\n")