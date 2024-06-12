function solution(users, emoticons) {
    const sales = emoticons
        .map((el) => [
            [10, Math.round(el * 0.9)], 
            [20, Math.round(el * 0.8)], 
            [30, Math.round(el * 0.7)], 
            [40, Math.round(el * 0.6)]
        ]);
    
    return dfs(0, emoticons.length, [], users, sales)
        .reduce((acc, cur) => {
            if (cur[0] > acc[0]
               || (cur[0] >= acc[0] && cur[1] > acc[1])) {
                return cur;
            }
            return acc;
        }, [0, 0]);
}

function dfs(cnt, max, now, users, sales) {
    if (cnt === max) 
        return [calc(users, now.map((el, ind) => sales[ind][el]))];
    
    return [0, 1, 2, 3]
        .map((el) => dfs(cnt + 1, max, [...now, el], users, sales))
        .flat(1);
}

function calc(users, sale) {
    return users.reduce((answer, user) => {
        const totalPrice = sale
            .reduce((totalPrice, emoticon) => {
                if (user[0] <= emoticon[0]) totalPrice += emoticon[1];
                return totalPrice;
            }, 0); 
        
        if (user[1] > totalPrice) answer[1] += totalPrice;
        else answer[0]++;

        return answer;
    }, [0, 0]);
}