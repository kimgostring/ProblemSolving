n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()

ans = []
ansSet = set()
visited = [False] * n
def permutations(selected = []):  
    if len(selected) == m:
        now = " ".join(map(str, selected))
        
        if now not in ansSet:
            ans.append(now)
            ansSet.add(now)

    for i in range(n):
        if visited[i]:
            continue

        selected.append(arr[i])
        visited[i] = True
        permutations(selected)
        selected.pop()
        visited[i] = False

permutations()
print(*ans, sep="\n")
