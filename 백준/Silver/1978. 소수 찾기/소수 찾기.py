n = int(input())
nums = list(map(int, input().split()))

result = 0
for num in nums:
    if num == 1:
        continue
    else:
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

        if flag:
            result += 1

print(result)
