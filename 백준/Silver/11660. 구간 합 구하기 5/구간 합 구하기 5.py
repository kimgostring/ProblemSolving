import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
table = [[0] * (n + 1)]
for _ in range(n):
    table.append([0, *map(int, input().rstrip().split(" "))])

# 구간합
for i in range(1, n + 1):
    for j in range(1, n + 1):
        table[i][j] += table[i][j - 1]
    for j in range(n, 0, -1):
        table[i][j] += table[i - 1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split(" "))
    print(
        table[x2][y2]
        - table[x2][y1 - 1]
        - table[x1 - 1][y2]
        + table[x1 - 1][y1 - 1]
    )
