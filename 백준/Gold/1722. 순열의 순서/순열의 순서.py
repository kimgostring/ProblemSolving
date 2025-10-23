import math

n = int(input())
prob, *perm = map(int, input().split(" "))
nums = [i for i in range(1, n + 1)]

if prob == 1: # 순열 계산
  k = perm[0] - 1
  answer = [] 
  
  n -= 1
  divider = math.factorial(n)
  while k != 0:
    i, k = divmod(k, divider)
    answer.append(nums[i])
    nums.pop(i)

    if n == 1:
      break

    divider //= n
    n -= 1

  answer += nums # 남은 숫자 붙여서 연결 
  print(*answer)

elif prob == 2: # 몇 번째 순열인지 계산
  answer = 1

  n -= 1
  factor = math.factorial(n)
  for p in perm:
    i = nums.index(p)
    answer += i * factor
    nums.pop(i)
    
    if n == 1:
      break

    factor //= n
    n -= 1

  print(answer)