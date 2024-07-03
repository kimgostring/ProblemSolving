import math;

n, m, l = map(int, input().split(" "));
if n != 0:
    areas = sorted([0] + list(map(int, input().split(" "))) + [l]);
    lengths = [areas[i + 1] - areas[i] for i in range(n + 1)];
else:
    lengths = [l - 0];

def calcCnt(mid):
    cnt = 0;
    for length in lengths:
        cnt += math.ceil(length / mid) - 1;
    
    return cnt;

left, right = 1, max(lengths);
answer = right;
while left <= right:
    mid = (left + right) // 2;
    cnt = calcCnt(mid);
    
    if cnt > m:
        # 개수가 너무 많음, 즉 최소 길이를 더 길게 만들어야 함
        left = mid + 1;
    else:
        # 개수가 같은 경우 중에서도 길이(mid)가 최소인 경우를 구해야 함 
        right = mid - 1;
        answer = min(answer, mid);

print(answer);