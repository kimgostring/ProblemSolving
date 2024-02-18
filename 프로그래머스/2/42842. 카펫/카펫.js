function solution(brown, yellow) {
    const SUM = brown / 2 - 2;
    const MAX_H = SUM / 2;
    
    let w, h;
    for (h = 1, w = SUM - h; h <= MAX_H; h += 1, w -= 1) { 
        if (h * w === yellow) break;
    }
    
    return [w + 2, h + 2];
}