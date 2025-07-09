import sys
input = sys.stdin.readline

def is_sorted_arr(m, n, arr):
  for i in range(m - 1):
    for j in range(n - 1):
      if arr[j][i] + arr[j + 1][i + 1] > arr[j + 1][i] + arr[j][i + 1]:
        return False

  return True

t = int(input())
for _ in range(t):
  n, m = map(int, input().rstrip().split(" "))
  arr = [list(map(int, input().rstrip().split(" "))) for __ in range(n)]
  print("YES" if is_sorted_arr(m, n, arr) else "NO")
