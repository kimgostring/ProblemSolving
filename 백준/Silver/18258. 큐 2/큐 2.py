import sys
input = sys.stdin.readline

n = int(input())

front = rear = -1
queue = [0] * n
for i in range(n):
    command = list(input().split())
    match command[0]:
        case 'push':
            rear += 1
            queue[rear] = int(command[1])
            # print(queue[rear])
        case 'pop':
            if front == rear:
                print(-1)
            else:
                front += 1
                print(queue[front])
        case 'size':
            print(rear - front)
        case 'empty':
            print(1 if front == rear else 0)
        case 'front':
            print(-1 if front == rear else queue[front + 1])
        case 'back':
            print(-1 if front == rear else queue[rear])
