from heapq import heappush, heappop;
import sys;
input = sys.stdin.readline;

n = int(input());
inputs = (int(input()) for _ in range(n));

h = [];
answer = [];
for v in inputs:
    if v: heappush(h, (abs(v), v));
    else: answer.append(heappop(h)[1] if h else 0);
    
print(*answer, sep="\n");