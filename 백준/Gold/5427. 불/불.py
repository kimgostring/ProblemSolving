from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

EMPTY = 0
FIRE = 1
WALL = 2
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def checkIsInside(px, py, w, h):
    return (0 <= px < h) and (0 <= py < w)

def checkIsBoundary(px, py, w, h):
    return px == 0 or px == h - 1 or py == 0 or py == w - 1

def moveFires(board, fq):
    nFq = deque()
    while fq:
        fx, fy = fq.popleft()

        for dx, dy in DIRS:
            nx, ny = fx + dx, fy + dy
            if checkIsInside(nx, ny, w, h) and board[nx][ny] == EMPTY:
                # 불 이동 가능
                nFq.append((nx, ny))
                board[nx][ny] = FIRE

    return nFq

def simulation(w, h, board, fires, px, py):
    fq = moveFires(board, deque(fires))
    stepOfBoard = 1

    # 사람 이동
    q = deque([(px, py, 1)])
    visited = [[False] * w for _ in range(h)]
    visited[px][py] = True

    while q:
        px, py, step = q.popleft()

        # 불 이동
        if step > stepOfBoard:
            fq = moveFires(board, fq)
            stepOfBoard += 1

        # 탈출 가능 여부 확인
        if checkIsBoundary(px, py, w, h):
            return step

        # 가능한 위치로 상근이 움직이기
        for dx, dy in DIRS:
            nx, ny = px + dx, py + dy
            if board[nx][ny] == EMPTY and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, step + 1))

    # 탈출 실패
    return False

tc = int(input())
for _ in range(tc):
    w, h = map(int, input().rstrip().split(" "))

    px, py = -1, -1
    board = [[EMPTY] * w for __ in range(h)]
    fires = []
    for i in range(h):
        line = input().rstrip()
        for j, char in enumerate(line):
            if char == "*":
                board[i][j] = FIRE
                fires.append((i, j))
            elif char == "#":
                board[i][j] = WALL
            elif char == "@":
                px, py = i, j

    ans = simulation(w, h, board, fires, px, py)
    print(ans if ans else "IMPOSSIBLE")
