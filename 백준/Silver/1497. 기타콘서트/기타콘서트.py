import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
guitars = []
for i in range(n):
    name, songs = input().rstrip().split(" ")
    guitars.append(int("0b" + "".join("1" if x == "Y" else "0" for x in songs), 2))

mx = 0
ans = -1
for com in range(1, 2 ** n):
    tmp = 1
    curAns = 0
    curSongs = 0
    for i in range(n):
        if com & tmp:
            curAns += 1
            curSongs |= guitars[i]
        tmp <<= 1
    
    tmp = 1
    curMx = 0
    for i in range(m):
        if curSongs & tmp:
            curMx += 1
        tmp <<= 1
        
    if curMx > mx or (curMx == mx and curAns < ans):
        mx = curMx
        ans = curAns 

print(ans)