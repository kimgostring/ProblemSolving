a = input()
b = input()

# len(a) >= len(b)
if len(a) < len(b):
  a, b = b, a
lenA = len(a)
lenB = len(b)

# LCS
dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
for i in range(lenA):
  for j in range(lenB):
    if a[i] == b[j]:
      dp[i + 1][j + 1] = dp[i][j] + 1
    else:
      dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(max(dp[-1]))