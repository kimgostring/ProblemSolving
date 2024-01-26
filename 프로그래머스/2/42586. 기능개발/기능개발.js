function solution(progresses, speeds) {
    const answer = [];
    const len = progresses.length;
    for (let day = 1, index = 0; index < len; day++) {
        let cnt = 0;
        while (progresses[index] + speeds[index] * day >= 100) {
            cnt++;
            index++;
        }
        if (cnt) answer.push(cnt);
    }
    
    return answer;
}