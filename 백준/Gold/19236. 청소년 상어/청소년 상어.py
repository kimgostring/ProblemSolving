import copy 
import sys
input = sys.stdin.readline

# 전역 변수 
DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
board = [[0] * 4 for _ in range(4)]
fishes = [False] * 17
shark = [0, 1, 0] # x, y, d 
ans = 0 # backtracking으로 갱신 

# input 받기 
for y in range(4):
    line = map(int, input().rstrip().split(" "))
    for x in range(4):
        n, d = line.__next__(), line.__next__() - 1
        board[y][x] = (n, d) 
        fishes[n] = (x, y)

def isFishMovable(nx, ny):
    return (0 <= nx < 4 and 0 <= ny < 4) and not (nx == shark[0] and ny == shark[1])

def swap(x, y, nx, ny):
    global board
    global fishes
    
    if not board[ny][nx]:
        board[ny][nx] = board[y][x]
        fishes[board[y][x][0]] = (nx, ny)
        board[y][x] = False
    else:
        n, nn = board[y][x][0], board[ny][nx][0]
        
        board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
        fishes[n], fishes[nn] = fishes[nn], fishes[n]

def rotate(d): 
    return (d + 1) % 8

def moveFish(x, y):
    n, d = board[y][x]
    for _ in range(8):
        nx, ny = x + DIR[d][0], y + DIR[d][1]
        if isFishMovable(nx, ny):
            board[y][x] = (n, d)
            swap(x, y, nx, ny)
            break
        else:
            d = rotate(d)

def isSharkMovable(nx, ny):
    return (0 <= nx < 4 and 0 <= ny < 4) and board[ny][nx]
    
def eatFish(x, y):
    global board
    global fishes
    global shark

    n, d = board[y][x]
    shark = [x, y, d]
    fishes[n] = False
    board[y][x] = False
    
    return n
    
def simulate(nowAns):
    global ans
    global board
    global fishes
    global shark
    
    for mul in range(1, 4):
        # 0. 상어 이동 가능 여부 확인
        d = shark[2]
        x, y = shark[0] + DIR[d][0] * mul, shark[1] + DIR[d][1] * mul
        if not isSharkMovable(x, y):
            continue
        
        # 1. 기존 상태 저장
        oldBoard = copy.deepcopy(board)
        oldFishes = copy.deepcopy(fishes)
        oldShark = shark[:]
        
        # 2. 상어 이동
        eatenNum = eatFish(x, y)
        
        # 3. 작은 물고기부터 이동
        for cords in fishes:
            if not cords:
                continue
            fx, fy = cords
            moveFish(fx, fy)
        
        # 4. 최댓값 갱신 후 계속 진행
        ans = max(ans, nowAns + eatenNum)
        simulate(nowAns + eatenNum)
        
        # 5. 복구
        board = oldBoard
        fishes = oldFishes
        shark = oldShark

simulate(0)
print(ans)