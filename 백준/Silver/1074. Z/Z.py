import sys
sys.setrecursionlimit(10 ** 6)


def z(num, N, x, y):
    length = (2 ** (N - 1))
    dirs = [(0, 0), (length, 0), (0, length), (length, length)]

    if N >= 1:
        for dx, dy in dirs:
            newX, newY = x + dx, y + dy

            if newX <= c < newX + length and newY <= r < newY + length:
                # 이 범위 안에 존재
                num = z(num, N - 1, newX, newY)
                break
            else:
                # 자세히 계산할 필요 X
                num += length * length

    return num


N, r, c = map(int, input().split())

result = z(0, N, 0, 0)
print(result)
