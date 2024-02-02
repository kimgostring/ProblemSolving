function solution(routes) {
    const LEN = routes.length;

    // sort 
    routes.sort((a, b) => {
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[0] - b[0];
    });
    
    // greedy 
    let answer = 0;
    let temp = -30001; // 마지막 설치 위치 
    for (let i = 0; i < LEN; i++) {
        if (routes[i][0] > temp) {
            // 하나 더 설치 필요
            answer++;
            temp = routes[i][1];
        }
    }
    
    return answer;
}