import sys;
input = sys.stdin.readline;

n = int(input());

ropes = [];
for _ in range(n):
    ropes.append(int(input()));

print(max((x * (i + 1) for i, x in enumerate(sorted(ropes, reverse=True)))));