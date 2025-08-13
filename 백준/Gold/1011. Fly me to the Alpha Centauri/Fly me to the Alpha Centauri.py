import sys
import math

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x, y = map(int, input().rstrip().split())
    
    # 가능성 없음 (x < y)
    # if x == y:
    #     print(0)
    #     continue
    if x + 1 == y:
        print(1)
        continue
    
    # n^2 < 루트 (y - x) <= (n + 1)^2 일 경우, 이동횟수 2n or 2n + 1번 
    dist = y - x
    n = math.ceil(math.sqrt(dist)) - 1
    if n ** 2 + n < dist:
        print(2 * n + 1)
    else:
        print(2 * n)
    