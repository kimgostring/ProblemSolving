function solution(word) {
    return word.split("").reduce((acc, cur, ind) => {
        acc += 1; // 자릿수 증가 시마다 +1
        if (cur === "A") return acc;
        
        let now = 1;
        if (ind !== 4) {
            for (let i = 4 - ind; i > 0; i--) now += 5 ** i;
            if (cur === "I") now *= 2;
            else if (cur === "O") now *= 3;
            else if (cur === "U") now *= 4;
        } else {
            if (cur === "I") now += 1;
            else if (cur === "O") now += 2;
            else if (cur === "U") now += 3;
        }
        
        return acc + now;
    }, 0);
}