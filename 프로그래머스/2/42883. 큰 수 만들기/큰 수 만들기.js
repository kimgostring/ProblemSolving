function solution(number, k) {
    const LEN = number.length;
    number = number.split("").map((val, ind) => Number(val));

    const stack = [];
    let i = 0;
    while (i < LEN && k > 0) {
        while (stack.length 
               && stack[stack.length - 1] < number[i]
               && k) {
            stack.pop();
            k--;
        }
        
        stack.push(number[i]);        
        i++;
    }    
    
    const answer = stack.concat(number.slice(i)).slice(0, LEN - k);
    return answer.join("");
}