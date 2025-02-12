const fs = require("fs");
const path = process.platform === "linux" ? 0 : "BOJ/input.txt";

class UnionFind {
  constructor(n) {
    this.parents = Array.from(Array(n), (_, i) => i);
  }

  find(x) {
    if (this.parents[x] !== x) this.parents[x] = this.find(this.parents[x]);
    return this.parents[x];
  }

  union(a, b) {
    let pa = this.find(a);
    let pb = this.find(b);
    if (pa === pb) return false;

    if (pa > pb) [a, b, pa, pb] = [b, a, pb, pa];
    this.parents[pb] = pa;

    return true;
  }
}

// input
const [n, ...input] = fs.readFileSync(path, encoding = "utf8").trim().split("\n")
  .map((e, i) => !i ? Number(e) : e.split(" ").map(Number));

const subtrees = new UnionFind(n);
const edges = [];
for (let i = 0; i < n; i++) {
  for (let j = 0; j < i; j++) {
    edges.push([input[i][j], i, j]);
  }
}
edges.sort((a, b) => a[0] - b[0]);

// kruskal
let ans = 0;
let cnt = 0;
for (const edge of edges) {
  const [price, s, e] = edge;
  if (!subtrees.union(s, e)) continue;
  
  ans += price;
  if (cnt >= n - 1) break;
}
console.log(ans);