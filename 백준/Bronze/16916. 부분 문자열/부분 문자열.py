s = input()
p = input()

sl, pl = len(s), len(p)
failP = [0] * pl
i, j = 1, 0
while i < pl:
    if p[i] == p[j]:
        failP[i] = j + 1
        i += 1
        j += 1
    else:
        if j != 0:
            j = failP[j - 1]
        else:
            i += 1

answer = 0
i, j = 0, 0
while i < sl:
    if s[i] == p[j]: 
        i += 1
        j += 1
        if j == pl:
            answer = 1
            break
    else:
        if j != 0:
            j = failP[j - 1]
        else:
            i += 1

print(answer)