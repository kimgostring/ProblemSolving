function solution(triangle) {
    const DEPTH = triangle.length;
    
    for (let i = 1; i < DEPTH; i++) {
        for (let j = 0; j <= i; j++) {
            triangle[i][j] = Math.max(triangle[i - 1][j - 1] ?? 0, triangle[i - 1][j] ?? 0) 
             + triangle[i][j];
        }
    }
    
    return Math.max(...triangle[DEPTH - 1]);
}