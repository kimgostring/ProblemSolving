import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
strs = set(input().rstrip() for _ in range(N))

answer = 0
for _ in range(M):
    s = input().rstrip()
    if s in strs:
        answer += 1
            
print(answer)