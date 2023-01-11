n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = -1
result = 1  # 최소 1

cnt = [0] * 100001

while end + 1 < n:
    # end 한 칸 밀기
    end += 1
    cnt[arr[end]] += 1

    # <= k 가 될 수 있도록 start 밀기
    while cnt[arr[end]] > k:
        cnt[arr[start]] -= 1
        start += 1

    # result 갱신
    if result < end - start + 1:
        result = end - start + 1

print(result)
