import math

min_num, max_num = map(int, input().split(" "))
end = math.ceil(math.sqrt(max_num))

is_prime = [True] * (end + 2)
is_divided = [False] * (max_num - min_num + 1)
for i in range(2, end + 1):
  factor = i ** 2
  if not is_prime[i]: 
    continue
  
  # i의 배수가 등장하면 skip하기 위해 기록
  for j in range(i, end + 1, i):
    is_prime[j] = False
    
  # 제곱 ㄴㄴ수 계산 
  num = math.ceil(min_num / factor) * factor

  while num <= max_num:
    is_divided[num - min_num] = True
    num += factor

print(max_num - min_num + 1 - is_divided.count(True))