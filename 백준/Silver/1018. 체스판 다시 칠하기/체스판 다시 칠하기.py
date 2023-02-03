n, m = map(int, input().split())

# 입력
arr = [0] * n
for i in range(n):
    arr[i] = input()

minNum = 8 * 8 // 2

# bf
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        temp = 0

        # 맨 왼쪽 위가 무조건 B라고 가정
        for dx in range(8):
            for dy in range(8):
                if ((i + dx + j + dy) % 2 == 0 and arr[i + dx][j + dy] == 'W') or ((i + dx + j + dy) % 2 == 1 and arr[i + dx][j + dy] == 'B'):
                    temp += 1

        if temp > 8 * 8 // 2:
            # 반대로 칠하는 게 최소일 경우 check
            temp = 8 * 8 - temp

        if temp < minNum:
            minNum = temp

print(minNum)
