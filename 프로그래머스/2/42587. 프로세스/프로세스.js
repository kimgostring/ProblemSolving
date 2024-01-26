function solution(priorities, location) {
    const len = priorities.length;
    const orders = [...priorities].sort((a, b) => b - a);
    
    let front_o = 0;
    for (let front_p = 0; front_p <= location; front_p++) {
        if (priorities[front_p] < orders[front_o]) {
            priorities.push(priorities[front_p]);
            if (location === front_p) location = priorities.length - 1;
        } else {
            front_o++; // 실행
            if (location === front_p) break;
        }
    }
    
    return front_o;
}