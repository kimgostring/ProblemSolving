n, k = map(int, input().split(" "));

c = [[1] * (n + 1) for _ in range(n + 1)];
for i in range(2, n + 1):
    for j in range(1, min(i, k + 1)):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % 10007;

print(c[n][k]);