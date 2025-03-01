import sys
input = sys.stdin.readline

N = int(input())

class Node:
    def __init__(self, word, depth = 1):
        self.word = word
        self.depth = depth
        self.children = dict()

    def createChild(self, word):
        # 기존 자식이 있는 경우 그대로 리턴
        if word in self.children:
            return self.children[word]
        
        new = Node(word, self.depth + 1)
        self.children[word] = new
        return new
      
    def print(self):
        if self.word:
            print(("--" * (self.depth - 1)) + self.word)    
        
        keys = list(self.children.keys())
        keys.sort()
        for key in keys:
            self.children[key].print()

root = Node(0, False)
for _ in range(N):
  words = input().rstrip().split(" ")[1:]
  node = root
  for word in words:
    node = node.createChild(word)

root.print()