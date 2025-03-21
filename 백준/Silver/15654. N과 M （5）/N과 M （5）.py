n, m = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums.sort()

def permutations(selected):
  if len(selected) == m:
    print(*(nums[i] for i in selected))
    return
  
  for i in range(n):
    if i not in selected:
      permutations([*selected, i])

permutations([])