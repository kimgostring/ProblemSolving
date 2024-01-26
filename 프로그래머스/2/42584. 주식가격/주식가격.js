function solution(prices) {
    const LEN = prices.length;
    const PRICE_LEN = 10001;
    const answer = Array(LEN);

    const stack = [];
    prices.forEach((price, index) => {
        while (stack.length && price < stack[stack.length - 1][1]) {
            const priv = stack.pop();
            answer[priv[0]] = index - priv[0];
        }
        
        stack.push([index, price]);
    });
    
    while (stack.length) {
        const priv = stack.pop();
        answer[priv[0]] = LEN - 1 - priv[0];
    }
                   
    return answer;
}