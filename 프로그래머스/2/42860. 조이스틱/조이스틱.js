function solution(name) {
    const LEN = name.length;
    const ALPHA_LEN = 'Z'.charCodeAt(0) - 'A'.charCodeAt(0);
    const ASCII_A = 'A'.charCodeAt(0);

    let answer = 0;
    const indArr = [0]; // A가 아닌 곳의 ind + 배열 시작/끝 ind 추가 
    Array(...name).forEach((val, ind) => {
        const diff = val.charCodeAt(0) - ASCII_A;
        if (diff) {
            // 위아래 계산
            answer += diff <= ALPHA_LEN / 2 ? diff : ALPHA_LEN - diff + 1;
            indArr.push(ind);
        }
    });
    indArr.push(LEN);
    
    // 양옆 계산
    const IND_LEN = indArr.length;
    let max = -1000000; // 안 지나가는 길이를 최대로 
    for (let i = 0; i < IND_LEN - 1; i++) {
        const now = indArr[i + 1] - indArr[i] - Math.min(indArr[i] - 0, LEN - indArr[i + 1]);
        if (now > max) max = now;
    }
    answer += (LEN - max);
    
    return answer;
}