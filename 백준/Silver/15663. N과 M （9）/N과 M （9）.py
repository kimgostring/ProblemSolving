from collections import Counter

n, m = map(int, input().split(" "))
arr = map(int, input().split(" "))

cnt = Counter(arr)
arr = sorted(list(cnt.keys()))
visited = dict(((k, 0) for k in arr))

ans = []
def permutations(selected = []):  
    if len(selected) == m:
        ans.append(" ".join(map(str, selected)))

    for num in arr:
        if visited[num] >= cnt[num]:
            continue

        selected.append(num)
        visited[num] += 1
        permutations(selected)
        selected.pop()
        visited[num] -= 1

permutations()
print(*ans, sep="\n")
