from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

class DoubleHeap:
    def __init__(self):
        self.asc_heap = []
        self.desc_heap = []
        self.deleted_prob = defaultdict(int) # 삭제된 문제 번호 
        self.not_deleted_prob = defaultdict(int) # 삭제된 뒤 문제 추가된 경우, level 기록

    def recommend(self, is_acs):
        self._adjust(is_acs)
        print(self.asc_heap[0][1] if is_acs else -self.desc_heap[0][1])

    def add(self, p, l):
        if self.deleted_prob[p] > 0:
            self.not_deleted_prob[p] = l

        heappush(self.asc_heap, (l, p))
        heappush(self.desc_heap, (-l, -p))

    def solve(self, p):
        self.deleted_prob[p] += 1
        if p in self.not_deleted_prob:
            del(self.not_deleted_prob[p])

    def _adjust(self, is_acs):
        if is_acs:
            while len(self.asc_heap) > 0:
                l, p = self.asc_heap[0]
                if self.deleted_prob[p] <= 0 or self.not_deleted_prob[p] == l:
                    break
                self.deleted_prob[p] -= 1
                heappop(self.asc_heap)
        else:
            while len(self.desc_heap) > 0:
                l, p = self.desc_heap[0]
                if self.deleted_prob[-p] <= 0 or self.not_deleted_prob[-p] == -l:
                    break
                self.deleted_prob[-p] -= 1
                heappop(self.desc_heap)

dh = DoubleHeap()

n = int(input())
for _ in range(n):
    p, l = map(int, input().rstrip().split(" "))
    dh.add(p, l)

m = int(input())
for _ in range(m):
    c, *args = input().rstrip().split(" ")

    if c == "recommend":
        dh.recommend(True if args[0] == "-1" else False)
    elif c == "add":
        dh.add(*map(int, args))
    elif c == "solved":
        dh.solve(int(args[0]))
