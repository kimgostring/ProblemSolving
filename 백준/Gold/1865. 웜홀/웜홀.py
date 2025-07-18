import sys
input = sys.stdin.readline

# constant
INF = 10005

# global
n = 0
edges = []

def can_go_back_to_the_past(s):
    time = [INF] * (n + 1)
    time[s] = 0

    for i in range(n):
        for s, e, t in edges:
            if time[e] > time[s] + t:
                time[e] = time[s] + t
                if i == n - 1:
                    return True

    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().rstrip().split(" "))
    edges = []
    for i in range(m):
        s, e, t = map(int, input().rstrip().split(" "))
        edges.append((s, e, t))
        edges.append((e, s, t))
    for i in range(w):
        s, e, t = map(int, input().rstrip().split(" "))
        edges.append((s, e, -t))

    print("YES" if can_go_back_to_the_past(1) else "NO")
