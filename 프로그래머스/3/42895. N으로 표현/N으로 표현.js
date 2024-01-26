function solution(N, number) {
    const MAX_NUMBER = 32000
    const dp = Array.from(Array(9), () => new Set());
    
    for (let n = 1; n <= 8; n++) { // N을 n번 사용
        const nNum = N * Number("1".repeat(n));
        if (number === nNum) return n;
        dp[n].add(nNum);

        for (let k = 1; k < n; k++) {
            // dp_n = dp_k +-*/ dp_m-k or N...N
            for (const val1 of dp[k]) {
                for(const val2 of dp[n - k]) {
                    for (const op of ["+", "-", "*", "/"]) {
                        let result;
                        if (op === "+") result = val1 + val2;
                        else if (op === "-") result = val1 - val2;
                        else if (op === "*") result = val1 * val2;
                        else if (op === "/") result = Math.floor(val1 / val2);
                        
                        if (number === result) return n;
                        dp[n].add(result);
                    }
                }
            }
        } 
    }
    
    return -1;
}