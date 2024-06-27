from itertools import combinations;

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
    
answer = 10e6;
for selectedI in list(combinations(range(len(chickens)), m)):
    selectedChickenD = [d for i, d in enumerate(chickenD) if i in selectedI];
    answer = min(answer, sum(map(min, zip(*selectedChickenD))));
    
print(answer);