n, m = map(int, input().split(" ")) 

def permutations_with_replacement(last, selected):
    if len(selected) == m:
        print(*selected)
        return

    for i in range(last, n + 1):
        selected.append(i)
        permutations_with_replacement(i, selected)
        selected.pop()

permutations_with_replacement(1, [])