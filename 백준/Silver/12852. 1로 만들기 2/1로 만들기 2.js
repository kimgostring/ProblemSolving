const fs = require("fs");

const path = process.platform === "linux" ? 0 : "input.txt";
const n = Number(fs.readFileSync(path, encoding="utf8"));

const dp = Array(n + 1);
const prev = Array(n + 1).fill(-1);
dp[1] = 0;
for (let i = 2; i <= n; i++) {
    candidates = [ [dp[i - 1] + 1, [i - 1]] ];
    if (i % 2 === 0) candidates.push([dp[i / 2] + 1, i / 2]); 
    if (i % 3 === 0) candidates.push([dp[i / 3] + 1, i / 3]); 

    candidates.sort((a, b) => a[0] - b[0]);
    dp[i] = candidates[0][0];
    prev[i] = candidates[0][1];
}

let i = n;
let way = "";
while (i !== -1) {
    way += `${i} `;
    i = prev[i];
}

console.log(`${dp[n]}\n${way}`);