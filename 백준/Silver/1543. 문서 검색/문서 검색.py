import sys
input = sys.stdin.readline

s = input().rstrip()
subs = input().rstrip()
L = len(subs)

i = 0
cnt = 0
while True:
    i = s.find(subs, i)
    if i == -1:
        break
    cnt += 1
    i += L
    

print(cnt)