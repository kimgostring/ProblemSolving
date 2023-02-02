n, k = map(int, input().split())
arr = list(range(1, n + 1))
result = [0] * n

i = 0
for j in range(n):
    i = (i + k - 1) % n
    result[j] = arr.pop(i)
    n -= 1

print("<" + ", ".join(map(str, result)) + ">")
