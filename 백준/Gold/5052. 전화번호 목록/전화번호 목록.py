import sys
input = sys.stdin.readline

class Trie:
    def __init__(self, n):
        self.cnt = 1
        self.next = [[-1] * 10 for _ in range(n * 10 + 1)]
        self.isLastChar = set()

    def add(self, value):
        prev = 0
        now = -1
        for index in map(Trie._charToInt, value):
            now = self.next[prev][index]
            if now == -1:
                self.next[prev][index] = self.cnt
                now = self.cnt
                self.cnt += 1
            elif now in self.isLastChar:
                return False

            prev = now

        for index in self.next[now]:
          if index > -1:
            return False
        
        self.isLastChar.add(now)
        return True

    @staticmethod
    def _charToInt(char):
        return ord(char) - ord("0")

t = int(input())
for _ in range(t):
    n = int(input())
    
    trie = Trie(n)
    consistent = True
    for __ in range(n):
        phoneNum = input().rstrip()
        if consistent and not trie.add(phoneNum):
            consistent = False
    
    print("YES" if consistent else "NO")
