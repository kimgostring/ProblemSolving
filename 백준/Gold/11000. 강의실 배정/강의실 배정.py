from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

# 정렬
arr.sort()

# 강의실 하나에서 최대한 많은 강의 진행해 보기
# = 남은 강의들 중 가장 빨리 시작하는 강의를 가장 일찍 끝나는 곳에다 넣어보기
# 여기다 못 넣으면, 어차피 다른 강의실에도 못 넣으니 새 강의실 생성
cnt = 1
lastTimes = [0]
for i in range(n):
    last = lastTimes[0]
    if arr[i][0] >= last:
        heappop(lastTimes)
        heappush(lastTimes, arr[i][1])
    else:
        cnt += 1
        heappush(lastTimes, arr[i][1])

print(cnt)
