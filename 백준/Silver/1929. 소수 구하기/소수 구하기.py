m, n = map(int, input().split(" "));

arr = [True] * (n + 1);
answer = [];
for i in range(2, n + 1):
    if not arr[i]:
        continue;
    
    if i >= m:
        answer.append(i);
    j = i << 1;
    while j < n + 1:
        arr[j] = False;
        j += i;    
    
print(*answer, sep="\n");