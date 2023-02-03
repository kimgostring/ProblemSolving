from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())

arr = [0] * n
for i in range(n):
    arr[i] = input()

# 맨 위가 B라고 가정하고 구간합 구하기
# 인덱스가 0인 라인은 비워두기 -> 왼쪽 위 끝에 붙은 부분의 식도 다른 식과 동일하게 만들기 위해
prefixSum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        prefixSum[i + 1][j + 1] += prefixSum[i + 1][j]
        if ((i + j) % 2 == 0 and arr[i][j] == 'W') or ((i + j) % 2 == 1 and arr[i][j] == 'B'):
            prefixSum[i + 1][j + 1] += 1
    for j in range(m):
        prefixSum[i + 1][j + 1] += prefixSum[i][j + 1]

# 구간합 활용해서 구하기
minNum = k * k // 2
for i in range(n - k + 1):
    for j in range(m - k + 1):
        # 맨 위 왼쪽 모서리가 i, j인 위치
        temp = prefixSum[i + k][j + k] - prefixSum[i][j + k] - \
            prefixSum[i + k][j] + prefixSum[i][j]

        # 반대로 칠해야 더 수가 작은 경우
        if temp > k * k // 2:
            temp = k * k - temp

        if temp < minNum:
            minNum = temp

print(minNum)
