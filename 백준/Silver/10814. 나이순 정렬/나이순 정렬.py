n = int(input())

arr = [0] * n
for i in range(n):
    arr[i] = list(input().split())
    arr[i][0] = int(arr[i][0])

arr.sort(key=lambda x: x[0])

for i in range(n):
    print(arr[i][0], arr[i][1])
