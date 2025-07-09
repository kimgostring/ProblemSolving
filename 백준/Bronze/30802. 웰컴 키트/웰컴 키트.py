from math import ceil

n = int(input())
participants = list(map(int, input().split(" ")))
t, p = map(int, input().split(" "))

print(sum(map(lambda x: ceil(x / t), participants)))
print(n // p, n % p)
