# 2. count 사용
from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards = dict(Counter(cards))

for num in nums:
    print(cards.get(num, 0), end=" ")