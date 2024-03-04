import math

def solution(arrows):
    DIRS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)];
    
    v = set();
    e = set();

    answer = 0;
    x, y = 0, 0;
    v.add((x, y));
    for d in arrows:  
        dx, dy = DIRS[d];
        
        for i in range(2):
            x2, y2 = x + dx, y + dy;
            v.add((x2, y2));
            e.add(((x, y), (x2, y2)) if d < 4 else ((x2, y2), (x, y)));
            x, y = x2, y2;
            
    return 1 - len(v) + len(e); # v - e + f = 1

            
            
    