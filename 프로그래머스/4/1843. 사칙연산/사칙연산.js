function solution(arr) {
    const LEN = Math.ceil(arr.length / 2); // 숫자 총 개수   
    const dp_max = Array.from(Array(LEN), () => []);
    const dp_min = Array.from(Array(LEN), () => []);
    
    // init
    const init = arr.filter((val, ind) => !(ind % 2)).map((val) => Number(val));
    dp_max[0] = init;
    dp_min[0] = init;
    
    // dp
    for (let n = 1; n < LEN; n++) { 
        for (let k = 0; k < LEN - n; k++) { // k번째 숫자부터 n개 연산자로 연산했을 때 최대/최소
            const max = [];
            const min = [];
            for (let i = 0; i < n; i++) { // i번째 연산자를 이전 계산 결과들을 이용해 계산
                if (arr[(k + i) * 2 + 1] === "+") {
                    max.push(dp_max[i][k] + dp_max[n - i - 1][k + i + 1]);
                    min.push(dp_min[i]?.[k] + dp_min[n - i - 1]?.[k + i + 1]);
                } else { // -
                    max.push(dp_max[i][k] - dp_min[n - i - 1]?.[k + i + 1]);
                    min.push(dp_min[i]?.[k] - dp_max[n - i - 1][k + i + 1]);
                }
            }
            
            dp_max[n].push(Math.max(...max));
            dp_min[n].push(Math.min(...min));
        }
    }
    
    return Math.max(...dp_max[LEN - 1]);
}