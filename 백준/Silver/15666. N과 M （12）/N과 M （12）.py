_, m = map(int, input().split(" "))
nums = sorted(set(map(int, input().split(" "))))
n = len(nums)

selected = []
def print_permutations(start):
  if len(selected) == m:
    print(*selected, sep=" ")
    return
  for i in range(start, n):
    selected.append(nums[i])
    print_permutations(i)
    selected.pop()

print_permutations(0)