from collections import deque
from itertools import combinations

SELECT_NUM = 7
SIDE_OF_SQUARE = 5
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

board = []
for _ in range(5):
  board.append(input())

def is_d_more(coords):
    d_cnt = 0
    for x, y in coords:
        if board[x][y] == "S":
            d_cnt += 1
        if d_cnt > SELECT_NUM / 2:
            return True
    return False

def is_adjacent(coords): # BFS
    sx, sy = coords.pop()
    q = deque([(sx, sy)])
    
    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in coords:
                continue
            
            coords.remove((nx, ny))
            q.append((nx, ny))

    if len(coords) == 0:
        return True
    return False

ans = 0
map_num_to_coord = lambda x: (x // SIDE_OF_SQUARE, x % SIDE_OF_SQUARE)
for nums in combinations(range(SIDE_OF_SQUARE * SIDE_OF_SQUARE), SELECT_NUM):
    coords = set(map(map_num_to_coord, nums))
    if is_d_more(coords) and is_adjacent(coords):
        ans += 1

print(ans)
