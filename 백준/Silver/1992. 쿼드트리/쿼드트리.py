def compress(x, y, n, arr):
    if n == 1:
        return arr[x][y];
    
    answer = [];
    for dx, dy in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        half = n // 2;
        nx, ny = x + dx * half, y + dy * half;
        answer.append(compress(nx, ny, half, arr));
    
    if answer.count("0") == 4:
        return "0";
    elif answer.count("1") == 4:
        return "1";
    
    return "(" + "".join(answer) + ")";
    
n = int(input());
arr = [];
for _ in range(n):
    arr.append(list(input()));
    
print(compress(0, 0, n, arr));