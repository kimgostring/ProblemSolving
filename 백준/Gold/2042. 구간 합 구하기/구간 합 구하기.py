import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] * (n + 1)
bit = [0] * (n + 1)


def update(i, now):  # i번째 인덱스의 값을 now로 바꾸기
    diff = now - arr[i]
    arr[i] = now

    while i <= n:
        bit[i] += diff
        i += i & -i


def prefix_sum(i):  # i번째 인덱스까지의 구간합 계산
    result = 0

    while i >= 1:
        result += bit[i]
        i -= i & -i

    return result


# arr 입력받기 및 BIT 계산
for i in range(1, n + 1):
    now = int(input())
    arr[i] = now

    length = i & -i
    for j in range(length):
        bit[i] += arr[i - j]


# update & print sum
for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        # b번째 수를 c로 변경
        update(b, c)
    else:
        # b ~ c의 합을 구하여 출력
        print(prefix_sum(c) - prefix_sum(b - 1))
