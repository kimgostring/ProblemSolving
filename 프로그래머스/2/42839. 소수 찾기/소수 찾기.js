function solution(numbers) {
    // 가능한 숫자 조합 다 만들기
    numbers = numbers.split("");
    const permutations = mkPermutations(numbers);
    
    // 에라토스테네스의 체 
    const max = Math.max(...permutations);
    const isPrime = new Array(max + 1).fill(true);
    isPrime[0] = false;
    isPrime[1] = false;
    
    for (let i = 2; i <= max; i++) {
        if (isPrime[i]) { // 소수인 경우, 이 소수의 배수들을 소수에서 제외 
            let j = 2;
            while (i * j <= max) {
                isPrime[i * j] = false;
                j++;
            }
        }
    }
    
    // 가능한 숫자 조합에서, 소수 개수 check
    return permutations.reduce((acc, cur) => {
        if (isPrime[cur]) return acc + 1;
        return acc;
    }, 0);
}

const mkPermutations = (numbers) => {
    const LEN = numbers.length;
    let permutations = new Set();
    
    // init
    const q = numbers.map((val, ind) => {
        const isVisited = new Array(LEN).fill(false);
        isVisited[ind] = true;
        return [val, isVisited];
    });
    
    // bfs
    while (q.length) {
        const [now, isVisited] = q.shift();
        permutations.add(Number(now));
        
        if (now.length >= LEN) continue;
        for (let i = 0; i < LEN; i++) {
            if (!isVisited[i]) {
                const newVisited = [...isVisited];
                newVisited[i] = true;
                q.push([now + numbers[i], newVisited]);
            }
        }
    }
    
    return new Array(...permutations);
}