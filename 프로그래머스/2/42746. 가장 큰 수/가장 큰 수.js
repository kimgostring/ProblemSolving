function solution(numbers) {
    numbers.sort((a, b) => {
        a = String(a);
        b = String(b);
        
        const LEN_A = a.length;
        const LEN_B = b.length;
        const LEN_MAX = Math.max(LEN_A, LEN_B)
        for (let i = 0; i < LEN_MAX; i++) {
            if ((a[i % LEN_A]) > (b[i % LEN_B])) return -1;
            else if ((a[i % LEN_A]) < (b[i % LEN_B])) return 1;
        }
        
        let avgA = 0;
        let avgB = 0;
        for (let i = 0; i < LEN_A; i++) avgA += Number(a[i]);
        for (let i = 0; i < LEN_B; i++) avgB += Number(b[i]);
        avgA /= LEN_A;
        avgB /= LEN_B;
        return avgB - avgA;
    });

    const answer = numbers.join("");
    if (answer[0] === "0") return "0";
    return answer;
}