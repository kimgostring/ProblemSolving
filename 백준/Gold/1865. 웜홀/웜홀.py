import sys
input = sys.stdin.readline

# global
n = 0
edges = []

def can_go_back_to_the_past(s):
    time = [0] * (n + 1)

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

    # 가상의 정점 0에서 출발, 모든 정점과 연결되어 있음
    print("YES" if can_go_back_to_the_past(0) else "NO")
