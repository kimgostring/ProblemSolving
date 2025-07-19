from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  n = int(input())

  clothes = defaultdict(int)
  for _ in range(n):
    _, kind = input().rstrip().split(" ")
    clothes[kind] += 1

  ans = 1
  for kind in clothes:
    ans *= (clothes[kind] + 1)
  ans -= 1

  print(ans)
