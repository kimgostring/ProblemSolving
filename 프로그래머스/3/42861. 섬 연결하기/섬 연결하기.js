function solution(n, costs) {
    // init
    const LEN = costs.length;
    const forest = new Forest(n);
    let answer = 0;
    
    costs.sort((a, b) => a[2] - b[2]);
    
    // kruskal
    for (let i = 0; i < LEN; i++) {
        const [a, b, cost] = costs[i];
        if (forest.union(a, b)) answer += cost;
    }
    
    return answer;
}

class Forest {
    constructor(n) {
        this.roots = Array.from(Array(n), (val, ind) => ind);
        this.ranks = Array(n).fill(0);
    }
    
    find(a) {
        let root = this.roots[a];
        if (a !== root) {
            root = this.find(root);
            this.roots[a] = root;
            this.ranks[a] = 1;
        }
        
        return root;
    }
    
    union(a, b) {
        const rootA = this.find(a);
        const rootB = this.find(b);
        if (rootA === rootB) return false;

        if (this.ranks[rootA] < this.ranks[rootB]) this.roots[rootA] = rootB;
        else if (this.ranks[rootA] > this.ranks[rootB]) this.roots[rootB] = rootA;
        else { // 임의로 붙이고, rank + 1
            this.roots[rootB] = rootA;
            this.ranks[rootB]++;
        }
        
        return true;
    }
}