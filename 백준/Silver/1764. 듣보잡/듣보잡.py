import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(n):
    set1.add(input())

for _ in range(m):
    set2.add(input())

result = sorted(set1.intersection(set2))

print(len(result))
print(''.join(result))
