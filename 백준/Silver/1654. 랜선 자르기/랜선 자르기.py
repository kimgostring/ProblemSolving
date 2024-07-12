import sys;
input = sys.stdin.readline;

k, n = map(int, input().split());
ls = sorted([int(input()) for _ in range(k)]);

lo, hi = 1, ls[-1];
answer = ls[0];
while lo <= hi:
    mid = (lo + hi) // 2;
    cnt = sum((l // mid for l in ls));
    
    if cnt < n:
        hi = mid - 1;
    else:
        answer = mid;
        lo = mid + 1;

print(answer);