N, M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums.sort()

selected = []
def backtracking(start):
  if len(selected) == M: 
    print(*selected, sep=" ")
    return

  for i in range(start, N):
    selected.append(nums[i])
    backtracking(i + 1)
    selected.pop()

backtracking(0)