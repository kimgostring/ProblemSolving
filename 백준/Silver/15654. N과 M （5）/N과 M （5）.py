n, m = map(int, input().split(" "))
nums = list(map(int, input().rstrip().split(" ")))
nums.sort()

def permutations(selected):
  if len(selected) == m:
    print(*selected)
    return
  
  for i in nums:
    if i not in selected:
      selected.append(i)
      permutations(selected)
      selected.pop()

permutations([])