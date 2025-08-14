def solve(n):
  dp = [1, 1]
  for i in range(2, n + 1):
    dp.append((dp[i - 1] + 2 * dp[i - 2]) % 10007)
  return dp[n]

n = int(input())
print(solve(n))