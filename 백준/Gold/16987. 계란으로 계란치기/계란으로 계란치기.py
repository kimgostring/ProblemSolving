import sys
input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
broken_eggs = set()

ans = 0 
def backtracking(start):
    global ans

    if start >= N or len(broken_eggs) >= N - 1:
        ans = max(ans, len(broken_eggs))
        return
    if start in broken_eggs:
        backtracking(start + 1)
        return

    # 계란 부수기
    for i in range(N):
        if i == start or i in broken_eggs:
            continue

        eggs[start][0] -= eggs[i][1]
        eggs[i][0] -= eggs[start][1]
        if eggs[start][0] <= 0:
            broken_eggs.add(start)
        if eggs[i][0] <= 0:
            broken_eggs.add(i)

        backtracking(start + 1)

        if eggs[start][0] <= 0:
            broken_eggs.remove(start)
        if eggs[i][0] <= 0:
            broken_eggs.remove(i)
        eggs[start][0] += eggs[i][1]
        eggs[i][0] += eggs[start][1]

backtracking(0)
print(ans)
