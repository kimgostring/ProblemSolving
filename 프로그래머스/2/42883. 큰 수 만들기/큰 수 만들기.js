function solution(number, k) {
    const LEN = number.length;
    number = number.split("").map((val) => Number(val));

    let answer = Array(LEN - k);
    let i = 0;
    let cnt = 0;
    while (i < LEN && k > 0) {
        let nextInd = i;
        for (let j = i; j < i + k + 1; j++) {
            if (number[j] > number[nextInd]) nextInd = j;
            if (j === LEN - 1) break;
        }
        
        if (nextInd !== i) {
            k -= (nextInd - i);
            answer[cnt] = number[nextInd];
            i = nextInd + 1;
        } else {
            if (i + k + 1 > LEN) break;
            else {
                answer[cnt] = number[i];
                i++;
            }
        }
        
        cnt++;
    }    
    
    answer = answer.concat(number.slice(i, LEN - k));
    return answer.join("");
}