function solution(n, wires) {
    // tree 구조 생성
    const tree = Array.from(new Array(n + 1), () => new Array());
    wires.forEach((wire) => {
        const [start, end] = wire;
        
        tree[start].push(end);
        tree[end].push(start);
    });
    
    // wire 자르기
    let answer = n;
    for (const wire of wires) {
        const [start, end] = wire;
        const visited = new Array(n + 1);
        visited[end] = true;
        
        const now = Math.abs(n - 2 * countNodes(start, tree, visited));
        
        if (now < answer) answer = now;
        if (answer < 2) break; // 최선의 case
    }
    
    return answer;
}

const countNodes = (root, tree, visited) => {
    if (visited[root]) return 0;
    
    let cnt = 1; // root node 방문
    visited[root] = true;
    for (const child of tree[root]) { // 자식들 방문
        cnt += countNodes(child, tree, visited);
    }
    
    return cnt;
};