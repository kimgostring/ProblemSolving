function solution(clothes) {
    const map = new Map();
    for (const [name, type] of clothes) {
        if (map.has(type)) map.set(type, map.get(type) + 1);
        else map.set(type, 1);
    }
    
    return [...map.values()].reduce((acc, cur) => acc * (cur + 1), 1) - 1;
}