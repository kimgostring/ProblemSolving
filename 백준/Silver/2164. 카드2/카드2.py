from collections import deque

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    queue = deque(list(range(2, n + 1, 2)))

    if n % 2 == 0:
        queue.popleft()
    while len(queue) > 1:
        now = queue.popleft()
        queue.append(now)
        queue.popleft()

    print(queue[0])
