n, m = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))

def calcMaxH(m, trees):
    ans = 0 
    l, r = 0, max(trees)
    
    while l <= r:
        mid = (l + r) // 2
        sumOfTrees = sum(map(lambda x: max(x - mid, 0), trees))

        if sumOfTrees < m:  # 조건 미충족, h 줄여야 함
            r = mid - 1
        else:  # 조건 충족
            l = mid + 1
            ans = mid

    return ans

print(calcMaxH(m, trees))
