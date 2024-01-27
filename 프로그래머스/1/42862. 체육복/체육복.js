function solution(n, lost, reserve) {
    const reserveSet = new Set(reserve);
    const filteredLost = lost.filter((val) => {
        if (reserveSet.delete(val)) return false;
        return true;
    }).sort();
    
    return filteredLost.reduce((acc, cur) => {
        if (reserveSet.delete(cur - 1) || reserveSet.delete(cur + 1)) acc++;
        return acc;
    }, n - filteredLost.length); 
}