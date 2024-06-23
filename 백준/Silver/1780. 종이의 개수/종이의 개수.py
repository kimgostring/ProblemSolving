def cntPaper(x, y, n, arr):
    if n == 0:
        return [1 if arr[x][y] == val else 0 for val in [-1, 0, 1]];
    
    answer = [0, 0, 0];
    for dx, dy in [(i * n, j * n) for i in range(3) for j in range(3)]:
        nx, ny = x + dx, y + dy;    
        answer = [acc + cur for acc, cur in zip(answer, cntPaper(nx, ny, n // 3, arr))];
    if sum(answer) == 9 and 9 in answer:
        answer[answer.index(9)] = 1;
    return answer;
    
n = int(input());
arr = [];
for _ in range(n):
    arr.append(list(map(int, input().split())));

print(*cntPaper(0, 0, n // 3, arr), sep="\n");