function solution(array, commands) {
    const answer = [];
    for (const command of commands) {
        const [start, end, ind] = command;
        const arr = array.slice(start - 1, end);
        arr.sort((a, b) => a - b);
        answer.push(arr[ind - 1]);
    }
    
    return answer;
}