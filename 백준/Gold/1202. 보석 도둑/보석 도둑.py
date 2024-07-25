from bisect import bisect_left; 
import sys;
input = sys.stdin.readline;

n, k = map(int, input().split());
gems = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(-x[1], -x[0]));
bags = sorted([int(input()) for _ in range(k)]);
notUsedBagInds = [i for i in range(k)];
notUsedCnt = k;

answer = 0;
for gem in gems:
    bagInd = bisect_left(bags, gem[0]);
    
    shouldChanged = [];
    while bagInd < k and bagInd != notUsedBagInds[bagInd]:
        shouldChanged.append(bagInd)
        bagInd = notUsedBagInds[bagInd];    
    shouldChanged.append(bagInd);
    
    if bagInd >= k:
        continue;

    answer += gem[1];

    changedVal = notUsedBagInds[bagInd + 1] if bagInd != k - 1 else k;
    for i in shouldChanged: 
        notUsedBagInds[i] = changedVal;
        
    notUsedCnt -= 1;
    if not notUsedCnt:
        break;

print(answer);