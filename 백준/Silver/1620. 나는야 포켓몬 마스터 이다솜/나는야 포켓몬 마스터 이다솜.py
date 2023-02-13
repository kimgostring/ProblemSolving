# 빠른 입력
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = dict()
arr = [0] * n

for i in range(n):
    name = input().strip()
    dic[name] = i
    arr[i] = name

for _ in range(m):
    question = input().strip()

    if question.isalpha():
        print(dic[question] + 1)
    else:
        print(arr[int(question) - 1])
