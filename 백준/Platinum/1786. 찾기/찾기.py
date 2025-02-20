import sys
input = sys.stdin.readline

T = input().rstrip("\n")
P = input().rstrip("\n")
N = len(T)
M = len(P)

# 전처리
failedFn = [0] * M
k = 0 # p[i]에서 최대 접두사 = 접미사 len
for i in range(1, M):
    while P[i] != P[k] and k != 0:
        k = failedFn[k - 1]

    if P[i] == P[k]:
        k += 1
    failedFn[i] = k

# KMP
k = 0
ans = []
for i in range(N):
    while T[i] != P[k] and k != 0:
        k = failedFn[k - 1]

    if T[i] == P[k]:
        k += 1
    if k == M: # matched
        ans.append(f'{i - M + 2}') 
        k = failedFn[k - 1]

print(len(ans))
print(" ".join(ans))
