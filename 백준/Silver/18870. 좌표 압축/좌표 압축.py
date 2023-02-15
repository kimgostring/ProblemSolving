n = int(input())
arr = list(map(int, input().split()))

# 좌표 압축 = 해당 점보다 작은 서로 다른 좌표의 개수
values = sorted(list(set(arr)))
result = dict(zip(values, range(len(values))))

for i in range(n):
    print(result[arr[i]], end=' ')
