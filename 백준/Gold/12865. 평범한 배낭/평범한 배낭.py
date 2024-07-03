from collections import defaultdict;
import sys;
input = sys.stdin.readline;

n, k = map(int, input().split(" "));
items = [0] * n;
for i in range(n):
    items[i] = tuple(map(int, input().split(" ")));
    
dp = defaultdict(int);
dp[0] = 0;
for w, v in items:
    for totW, totV in sorted(dp.items()):
        if w + totW <= k:
            dp[w + totW] = max(dp[w + totW], totV + v);

    if w <= k:
        dp[w] = max(dp[w], v); 
    
print(max(dp.values()));