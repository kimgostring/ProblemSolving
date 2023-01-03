import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
arr = list(map(int, input().split()));
prefixSum = [0] * n;

prefixSum[0] = arr[0];
for i in range(1, n) :
    prefixSum[i] = prefixSum[i - 1] + arr[i];
    
for i in range(m) :
    start, end = map(int, input().split());
    if start == 1 :
        startNum = 0;
    else :
        startNum = prefixSum[start - 2];
    
    print(prefixSum[end - 1] - startNum);

