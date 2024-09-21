from heapq import heappush, heappop
import sys

input = sys.stdin.readline
N = int(input())

MONTH_TO_INTS = [0] 
for prevM, d in enumerate([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]):
    MONTH_TO_INTS.append(MONTH_TO_INTS[prevM] + d)
    
convertDateToInts = lambda m, d: MONTH_TO_INTS[m] + d
S_DATE = convertDateToInts(3, 1)
E_DATE = convertDateToInts(11, 30)
    
flowers = [] # (시작일정수, 끝일정수)
for _ in range(N):
    sm, sd, em, ed = map(int, input().rstrip().split(" "))
    s = convertDateToInts(sm, sd)
    e = convertDateToInts(em, ed)
    if e > S_DATE and s < E_DATE + 1: 
        flowers.append((s, e))
flowers.sort()

i = 0
now = S_DATE
ans = 0
h = []
while now <= E_DATE:
    while i < N and flowers[i][0] <= now:
        heappush(h, -flowers[i][1])
        i += 1

    if not h:
        break
    now = -heappop(h)
    ans += 1
    
if now <= E_DATE:
    ans = 0

print(ans)