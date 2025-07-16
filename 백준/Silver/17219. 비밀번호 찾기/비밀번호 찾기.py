import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))
pws = dict((input().rstrip().split(" ") for _ in range(n)))
print(*(pws[input().rstrip()] for _ in range(m)), sep="\n")