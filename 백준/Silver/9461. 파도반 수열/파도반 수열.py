dp = [1, 1, 1, 2, 2]
def solution(n):
  for i in range(len(dp) - 1, n - 1):
    dp.append(dp[i - 4] + dp[i])

  return dp[n - 1]

t = int(input())
for _ in range(t): 
  n = int(input())
  print(solution(n))
