t = int(input())

dp = [0] * 12
for _ in range(t):
    n = int(input())

    # dp
    dp[1] = 1  # 1
    dp[2] = 2  # 1 + 1, 2
    dp[3] = 4  # 1 + 1 + 1, 1 + 2, 2 + 1, 3

    for i in range(4, n + 1):
        # 걍 dp[i - 1], dp[i - 2], dp[i - 3]의 맨 뒤에 1, 2, 3을 덧붙이는 모습 상상
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    print(dp[n])
