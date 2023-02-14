from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input())

    if x > 0:
        # 배열에 x 넣기
        heappush(heap, x)
    else:
        # 배열에서 가장 작은 값 pop
        if len(heap) > 0 :
            x = heappop(heap)
        else :
            x = 0
        print(x)
