import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * (n + 1)
days = [0] * (n + 1)

for i in range(1, n + 1):
    days[i], arr[i] = map(int, input().split())

result = [0] * (n + 2)
for i in range(n, 0, -1):
    # 역순 더하기
    # result[k] = max(result[i + d] + arr[i], result[i + 1]) # d = 상담에 걸리는 시간

    now = 0 if i + days[i] - 1 > n else result[i + days[i]] + arr[i]
    result[i] = max(now, result[i + 1])

print(result[1])
