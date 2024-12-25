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
    
    # n(n + 1) < y - x <= (n + 1)^2일 경우, 이동횟수 2n + 1번
    # n^2 < y - x <= n(n + 1)일 경우, 이동횟수 2n번
    n = math.ceil(math.sqrt(y - x)) - 1
    if n ** 2 + n < y - x:
        print(2 * n + 1)
    else:
        print(2 * n)
    