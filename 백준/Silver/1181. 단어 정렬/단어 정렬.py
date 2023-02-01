n = int(input())

arr = [0] * n
for i in range(n):
    arr[i] = input()

arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))

n = len(arr)
for i in range(n):
    print(arr[i])
