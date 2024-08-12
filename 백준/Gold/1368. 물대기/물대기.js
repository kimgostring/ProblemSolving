const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const inputs = fs.readFileSync(path, "utf8").trim().split("\n");
const n = Number(inputs[0]);
const edges = [];
for (let i = 0; i < n; i++) {
    edges.push([Number(inputs[i + 1]), i, n]);

    const prices = inputs[i + n + 1].split(" ").map(Number);
    for (let j = 0; j < n; j++) {
        if (i !== j) edges.push([prices[j], i, j]);
    }
}
edges.sort((a, b) => a[0] - b[0]);

class UnionFind {
    constructor(n) {
        this.parent = Array.from(Array(n), (v, i) => i);
    }

    find(a) {
        const shouldUpdated = [];        
        while (a !== this.parent[a]) shouldUpdated.push(a = this.parent[a]);
        shouldUpdated.forEach((v) => this.parent[v] = a);

        return a;
    }

    isInSameSet(a, b) {
        return this.find(a) === this.find(b);
    }

    union(a, b) {
        if (this.isInSameSet(a, b)) return;

        let [pa, pb] = [this.find(a), this.find(b)];
        if (pa > pb) [pa, a, pb, b] = [pb, b, pa, a];

        this.parent[pb] = pa;
        this.find(b);
        return;
    }
}

let cnt = 0;
let res = 0;
const uf = new UnionFind(n);
for (const e of edges) {
    const [p, a, b] = e;
    if (uf.isInSameSet(a, b)) continue;
    
    uf.union(a, b);
    res += p;
    if (++cnt === n) break;
}

console.log(res);