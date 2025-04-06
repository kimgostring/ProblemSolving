import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())

    dp = []
    for i in range(2):
        dp.append(list(map(int, input().rstrip().split(" "))))

    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + dp[0][i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] + dp[1][i])

    print(max(dp[0][n - 1], dp[1][n - 1]))