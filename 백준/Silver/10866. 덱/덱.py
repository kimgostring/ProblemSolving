from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])

for i in range(n):
    arr = list(input().split())
    match arr[0]:
        case 'push_front':
            q.appendleft(int(arr[1]))
        case 'push_back':
            q.append(int(arr[1]))
        case 'pop_front':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        case 'pop_back':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop())
        case 'size':
            print(len(q))
        case 'empty':
            print(1 if len(q) == 0 else 0)
        case 'front':
            print(-1 if len(q) == 0 else q[0])
        case 'back':
            h = len(q)
            print(-1 if h == 0 else q[h - 1])
