function solution(answers) {
    const stus = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ];
    const count = [0, 0, 0];
    
    for (let i = 0; i < answers.length; i++) {
        for (let j = 0; j < stus.length; j++) {
            if (stus[j][i % stus[j].length] === answers[i]) count[j]++;
        }
    }
    
    let answer = [];
    let max = 0;
    for (let i = 0; i < stus.length; i++) {
        if (count[i] > max) {
            answer = [i + 1];
            max = count[i];
        } else if (count[i] === max) {
            answer.push(i + 1);
        }
    }
    
    return answer;
}