n, m, k = map(int, input().split());
stickers = [];
for _ in range(k):
    r, c = map(int, input().split());
    sticker = [];
    for _ in range(r):
        sticker.append(list(map(int, input().split())));
        
    stickers.append(sticker);
    
def putOn(x, y, sticker, labtap):
    r, c = len(sticker), len(sticker[0]);
    canPutOn = True;
    for dx in range(r):
        for dy in range(c):
            if sticker[dx][dy] == 1 and labtap[x + dx][y + dy] == 1:
                canPutOn = False;
                break;
        if not canPutOn:
            break;

    answer = 0;
    if canPutOn:
        for dx in range(r):
            for dy in range(c):
                if sticker[dx][dy] == 1:
                    answer += 1;
                    labtap[x + dx][y + dy] = 1;
                
    return answer;
    
def rotate(sticker):
    r, c = len(sticker), len(sticker[0]);
    new = [[0] * r for _ in range(c)];
    for i in range(r):
        for j in range(c):
            new[j][r - 1 - i] = sticker[i][j];
    
    return new;
    
def simulation():
    answer = 0;
    labtap = [[0] * m for _ in range(n)];
    for sticker in stickers:
        cur = 0;
        for _ in range(4):
            r, c = len(sticker), len(sticker[0]);
            for x in range(n - r + 1):
                for y in range(m - c + 1):
                    cur = putOn(x, y, sticker, labtap);
                    if cur:
                        break;
                if cur:
                    break;
            if cur:
                answer += cur;
                break;
            else:
                sticker = rotate(sticker);
            
    return answer;

print(simulation());