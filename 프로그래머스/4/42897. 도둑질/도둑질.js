function solution(money) {
    const LEN = money.length;
    const dp_1 = [money[0], money[0], money[0]]; // 첫 번째 집 색칠 O
    const dp_0 = [0, money[1], Math.max(money[1], money[2])]; // 첫 번째 집 색칠 X
    
    for (i = 3; i < LEN; i++) {
        dp_1.push(Math.max(dp_1[i - 1], dp_1[i - 2] + money[i - 1]));
        dp_0.push(Math.max(dp_0[i - 1], dp_0[i - 2] + money[i]));
    }
    
    return Math.max(dp_1[LEN - 1], dp_0[LEN - 1]);
}