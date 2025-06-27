import sys
input = sys.stdin.readline

selected = []
def backtracking(start, k, nums):
  if len(selected) == 6:
    print(*selected, sep=" ")
    return

  for i in range(start, k):
    selected.append(nums[i])
    backtracking(i + 1, k, nums)
    selected.pop()

while True:
  k, *nums = map(int, input().split(" "))
  if k == 0:
    break

  backtracking(0, k, nums)
  print()
