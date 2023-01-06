n = int(input())

# 5의 배수면 게임 끝
# 5의 배수가 아니면, 5의 배수가 될 때까지 2로 빼 보기

result = 0
while n > 1:
    if n % 5 == 0:
        result += n // 5
        n = 0
        break
    result += 1
    n -= 2

if n != 0:
    result = -1

print(result)
