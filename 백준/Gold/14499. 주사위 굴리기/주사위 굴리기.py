import sys
input = sys.stdin.readline

class Dice:  
  top = 1 # 주사위 맨 윗 면의 index
  bottom = 6

  cord_diff = [0, (0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남
  next_index = [ 
    # 동서북남 이동 시, 주사위의 각 index가 다음 index로 위치 변경
    # 문제에 제시된 전개도 기준
    0, 
    [0, 4, 2, 1, 6, 5, 3],
    [0, 3, 2, 6, 1, 5, 4],
    [0, 5, 1, 3, 4, 6, 2],
    [0, 2, 6, 3, 4, 1, 5]
  ]

  def __init__(self, x, y):
    self.arr = [0] * 7 
    self.x = x
    self.y = y

  def move(self, d):
    dx, dy = Dice.cord_diff[d]
    self.x, self.y = self.x + dx, self.y + dy
    self.arr = [self.arr[i] for i in Dice.next_index[d]]

  def get_top(self):
    return self.arr[Dice.top]
  
  def get_bottom(self):
    return self.arr[Dice.bottom]

  def get_cords(self):
    return (self.x, self.y)

  def set_bottom(self, v):
    self.arr[Dice.bottom] = v

# 1. 기본 입력 
N, M, x, y, K = map(int, input().split(" "))
dice = Dice(x, y)

board = [list(map(int, input().split(" "))) for _ in range(N)]
check_is_valid_cord = lambda x, y: 0 <= x < N and 0 <= y < M  

dirs = map(int, input().split(" "))

# 2. 이동 
for d in dirs:
  dice.move(d)
  x, y = dice.get_cords()
  if not check_is_valid_cord(x, y):
    dice.move(d + 1 if d % 2 == 1 else d - 1) # 동서북남 1234, 동/북은 +1 해서 반대방향, 서/남은 -1 
    continue

  if board[x][y] == 0:
    board[x][y] = dice.get_bottom()
  else:
    dice.set_bottom(board[x][y])
    board[x][y] = 0

  print(dice.get_top())