const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const [[n, m], ...inputs] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .map((v) => v.split(" ").map(Number));

const edges = Array.from(Array(n + 1), () => []);
const indegree = Array(n + 1).fill(0);
for (const [s, e] of inputs) {
    edges[s].push(e);
    indegree[e]++;
};

let res = "";
const q = Array.from(Array(n), (v, i) => i + 1).filter((i) => !indegree[i]);
while (q.length) {
    const now = q.shift();
    res += `${now} `;

    for (const next of edges[now]) {
        indegree[next]--;
        if (!indegree[next]) q.push(next);
    }
}

console.log(res);