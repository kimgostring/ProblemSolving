from collections import defaultdict

def move(x, y, ex, ey):
    if x != ex: # r부터 변경
        return (x - 1 if x > ex else x + 1, y)
    return (x, y - 1 if y > ey else y + 1)

def solution(points, routes):
    ans = 0
    
    n = len(points)
    m = len(routes[0])
    
    # robot = ((현재 x, 현재 y), robot index, 현재 목적지 route index)
    robots = [(points[routes[i][0] - 1], i, 1) for i, j in enumerate(routes)]
    
    while robots:
        moved_robots = []
        check_crash = defaultdict(int)
        for (x, y), i, j in robots:
            # 충돌 check
            if check_crash[(x, y)] == 1:
                ans += 1
            check_crash[(x, y)] += 1
            
            ex, ey = points[routes[i][j] - 1]
            if x == ex and y == ey: 
                j += 1
                
                if j == m: # 이동 끝 
                    continue
                else: # 다음 route의 좌표
                    ex, ey = points[routes[i][j] - 1]
            
            nx, ny = move(x, y, ex, ey)               
            moved_robots.append(((nx, ny), i, j))
        robots = moved_robots

    return ans