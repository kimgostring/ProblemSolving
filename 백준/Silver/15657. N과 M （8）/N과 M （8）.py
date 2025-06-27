n, m = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums.sort()

selected = []
def backtracking(start):
  if len(selected) == m:
    print(*selected, sep=" ")
    return
  
  for i in range(start, n):
    selected.append(nums[i])
    backtracking(i)
    selected.pop()

backtracking(0)