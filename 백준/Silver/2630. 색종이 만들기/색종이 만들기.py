import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def dnc(n, x, y):  # 분할 정복 -> (흰색 개수, 파란색 개수) 리턴
    cnt = 0

    if n >= 2:
        half = n // 2
        flag = False

        cnt = dnc(half, x, y)
        if cnt == (1, 0) or cnt == (0, 1):
            flag = True  # 색종이를 하나로 합칠 수 있는 가능성 존재

        dirs = [(0, half), (half, 0), (half, half)]
        for i in range(3):
            temp = dnc(half, x + dirs[i][0], y + dirs[i][1])

            if flag:
                # print(cnt, temp, cnt == temp)
                if cnt != temp:  # 색종이를 하나로 합칠 수 없다고 처음 판별된 경우
                    # 지금까지 나온 색종이의 개수를 색별로 각각 더해주어야 함
                    cnt = (cnt[0] * (i + 1) + temp[0],
                           cnt[1] * (i + 1) + temp[1])
                    flag = False
                # else -> 여전히 색종이를 하나로 합칠 수 있음
            else:
                # 색종이의 개수를 색깔별로 더함
                cnt = (cnt[0] + temp[0], cnt[1] + temp[1])

    else:  # n == 1 -> 색종이 하나의 색
        if arr[y][x] == 0:
            cnt = (1, 0)
        else:
            cnt = (0, 1)

    # print(x, y, n, cnt)
    return cnt


n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

result = dnc(n, 0, 0)

print(result[0])
print(result[1])
