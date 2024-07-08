m, n = map(int, input().split(" "));

arr = [True] * (n + 1);
answer = [];
for i in range(2, n + 1):
    if not arr[i]:
        continue;
    
    if i >= m:
        answer.append(i);
    for j in range(i * i, n + 1, i):
        arr[j] = False;
    
print(*answer, sep="\n");