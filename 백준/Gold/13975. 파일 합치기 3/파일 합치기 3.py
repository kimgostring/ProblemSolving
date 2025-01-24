import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  ans = 0
  
  K = int(input())
  h = list(map(int, input().split(" ")))
  heapify(h)
  
  while len(h) > 1:
    a = heappop(h)
    b = heappop(h)

    new = a + b
    ans += new
    
    heappush(h, new)
    
  print(ans)