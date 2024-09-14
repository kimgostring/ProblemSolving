const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const [n, ...input] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .map((v, i) => {
        if (!i) return Number(v);
        return v.split(" ").map((e) => Number(e));
    });

dp = [];
input.forEach((line, i) => {
    dp[i] = i 
        ? line.map((e, j) => {
            if (j === 0) return dp[i - 1][0] + e;
            else if (j === i) return dp[i - 1][i - 1] + e;
            else return Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + e; 
        })
        : line;
});

console.log(Math.max(...dp[n - 1]));