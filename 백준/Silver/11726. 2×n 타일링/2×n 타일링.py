n = int(input())

if n <= 2:
    print(n)
    exit(0)

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    # dp[i - 1], dp[i - 2]에 각각 |, = 모양의 블럭을 덧붙인다고 생각
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)
