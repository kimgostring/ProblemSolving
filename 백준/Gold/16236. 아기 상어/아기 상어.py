from heapq import heappush, heappop
import sys
input = sys.stdin.readline

class Simulation:
    def __init__(self, board):
        self.n = len(board)
        self.board = board
        self.fishCnt = [0] * 7
        self.eatCnt = 0
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    continue
                elif board[i][j] == 9: 
                    self.babyShark = [2, i, j]
                    board[i][j] = 0
                else:
                    self.fishCnt[board[i][j]] += 1

    def doesFishExist(self):
        return sum(self.fishCnt[1:self.babyShark[0]]) > 0
    
    def isMovable(self, x, y):
        if not (0 <= x < n) or not (0 <= y < n):
            return False
        if self.board[x][y] > self.babyShark[0]:
            return False
        
        return True
    
    def isEatable(self, x, y):
        return self.board[x][y] and self.babyShark[0] > self.board[x][y]
    
    def eatFish(self, x, y):
        self.fishCnt[self.board[x][y]] -= 1
        self.board[x][y] = 0
        self.eatCnt += 1
        
        self.babyShark[1] = x
        self.babyShark[2] = y
        if self.babyShark[0] == self.eatCnt:
            self.babyShark[0] += 1
            self.eatCnt = 0
    
    def eatNearestFish(self):
        h = [(0, self.babyShark[1], self.babyShark[2])]
        
        visited = [[False] * n for _ in range(n)]
        visited[self.babyShark[1]][self.babyShark[2]] = True
        
        while h:
            sec, x, y = heappop(h)
        
            if self.isEatable(x, y): 
                self.eatFish(x, y)                           
                return sec
            
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                
                if not self.isMovable(nx, ny) or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                heappush(h, (sec + 1, nx, ny))
                
        return 0

    def calcSec(self):
        sec = 0
        while self.doesFishExist():
            now = self.eatNearestFish()
            if not now:
                break
            sec += now
        
        return sec
        
n = int(input())
board = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]

s = Simulation(board)
print(s.calcSec())