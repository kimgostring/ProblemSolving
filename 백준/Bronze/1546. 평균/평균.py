n = int(input())
scores = list(map(int, input().split(" ")))

top = max(*scores, 0)
ans = sum(map(lambda x: x / top * 100, scores)) / len(scores)
print(ans)