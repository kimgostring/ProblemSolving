from bisect import bisect_left, bisect_right

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards.sort()

for num in nums:
    print(bisect_right(cards, num) - bisect_left(cards, num), end=" ")
