const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const inputs = fs.readFileSync(path, "utf8").trim().split("\n");
const n = Number(inputs[0]);
const nodes = [];
const edges = [];
for (let i = 0; i < n; i++) {
    nodes.push([Number(inputs[i + 1]), i]);

    const prices = inputs[i + n + 1].split(" ").map(Number);
    for (let j = 0; j < n; j++) {
        if (i !== j) edges.push([prices[j], i, j]);
    }
}
nodes.sort((a, b) => a[0] - b[0]);
edges.sort((a, b) => a[0] - b[0]);

// 다 순회했음을 표시 
nodes.push([Infinity]);
edges.push([Infinity]);

class UnionFind {
    constructor(n) {
        this.parent = Array.from(Array(n), (v, i) => i)
        this.watered = Array(n).fill(false); 
        this.cnt = Array(n).fill(1);
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
        if (this.isInSameSet(a, b)) return 0;
        if (this.isWatered(a) && this.isWatered(b)) return 0;

        let [pa, pb] = [this.find(a), this.find(b)];
        if (pa > pb) [pa, a, pb, b] = [pb, b, pa, a];

        let cnt = 0;
        if (this.isWatered(pa)) cnt = this.cnt[pb];
        else if (this.isWatered(pb)) cnt = this.water(pa);

        this.parent[pb] = pa;
        this.find(b);
        this.cnt[pa] += this.cnt[pb]; 
        return cnt;
    }

    isWatered(a) {
        return this.watered[this.find(a)];
    }

    water(a) {
        if (this.isWatered(a)) return 0;

        const pa = this.find(a);
        this.watered[pa] = true;
        return this.cnt[pa];
    }
}

const uf = new UnionFind(n);
const [nl, el] = [nodes.length - 1, edges.length - 1];
let [ni, ei, cnt, res] = [0, 0, 0, 0];
while (cnt < n) {
    while (ni < nl && uf.isWatered(nodes[ni][1])) ni++;
    while (
        ei < el && (uf.isInSameSet(edges[ei][1], edges[ei][2]) || 
        (uf.isWatered(edges[ei][1]) && uf.isWatered(edges[ei][2]))
    )) ei++;
        
    const [node, edge] = [nodes[ni], edges[ei]];
    if (node[0] <= edge[0]) {
        cnt += uf.water(node[1]);
        res += node[0];
        ni++;
    } else {
        cnt += uf.union(edge[1], edge[2]);
        res += edge[0];
        ei++;
    }
}

console.log(res);