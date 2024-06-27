n, m = map(int, input().split());
homes = [];
chickens = [];
for x in range(n):
    tmp = map(int, input().split());
    for y, val in enumerate(tmp):
        if val == 1:
            homes.append((x, y));
        elif val == 2:
            chickens.append((x, y));
            
chickenD = [];
for cx, cy in chickens:
    tmp = [];
    for hx, hy in homes:    
        tmp.append(abs(hx - cx) + abs(hy - cy));
    chickenD.append(tmp);
    

def combinations(now, cnt, selected):
    if cnt == 0:
        selectedChickenD = [d for i, d in enumerate(chickenD) if i in selected];
        return sum(map(min, zip(*selectedChickenD)));
    elif now == -1:
        return 10e6;
    
    return min(combinations(now - 1, cnt, selected), combinations(now - 1, cnt - 1, selected + [now]));
        
print(combinations(len(chickenD) - 1, m, []));