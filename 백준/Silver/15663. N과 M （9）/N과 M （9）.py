n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()

visited = [False] * n
def permutations(selected = []):  
    if len(selected) == m:
        print(" ".join(map(str, selected)))

    prev = 0
    for i in range(n):
        if visited[i] or arr[i] == prev:
            continue

        prev = arr[i]
        selected.append(arr[i])
        visited[i] = True
        permutations(selected)
        selected.pop()
        visited[i] = False

permutations()
