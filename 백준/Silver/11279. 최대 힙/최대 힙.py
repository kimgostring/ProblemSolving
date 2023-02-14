from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x > 0:  # push
        heappush(heap, -x)

    else:  # x == 0, pop
        if len(heap) > 0:
            x = -heappop(heap)
        else:  # empty
            x = 0

        print(x)
