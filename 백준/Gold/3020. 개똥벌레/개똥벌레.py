import sys
from bisect import bisect_right

input = sys.stdin.readline

n, h = map(int, input().split())

# 종유석, 석순 입력 받기
startAtBottom = [0] * (h + 1)
startAtTop = [0] * (h + 1)
for i in range(n):
    num = int(input())

    if i % 2 == 0:  # 석순
        startAtBottom[num - 1] += 1
    else:  # 종유석
        startAtTop[h - num] += 1

# 석순, 종유석끼리 각각 prefix sum
for i in range(1, h):
    startAtTop[i] += startAtTop[i - 1]
    startAtBottom[h - i - 1] += startAtBottom[h - i]

# 두 배열 합치면서 최소 찾기
minNum = n + 1
cnt = 0
for i in range(0, h):
    now = startAtBottom[i] + startAtTop[i]
    if now < minNum:
        minNum = now
        cnt = 1
    elif now == minNum:
        cnt += 1

print(minNum, cnt)
