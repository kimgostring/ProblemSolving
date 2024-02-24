function solution(word) {
    return word.split("").reduce((acc, cur, ind) => {
        acc += 1; // 자릿수 증가 시마다 +1
        if (cur === "A") return acc;
        
        let now = 1;
        now += (((5 ** (5 - ind)) - 1) >> 2) - 1; // 등비수열의 합 - 1
        if (cur === "I") now = now << 1;
        else if (cur === "O") now *= 3;
        else if (cur === "U") now = now << 2;
        
        return acc + now;
    }, 0);
}