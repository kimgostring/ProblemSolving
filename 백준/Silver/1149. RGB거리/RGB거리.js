const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const [n, ...homes] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .map((e, i) => i === 0 ? Number(e) : e.split(" ").map(Number));

const dp = Array.from(Array(n), () => Array(3).fill(0));
dp[0] = homes[0];
homes.forEach((home, i) => {
    if (i !== 0) 
        home.forEach((c, j) => dp[i][j] = Math.min(...dp[i - 1].filter((e, k) => j !== k)) + c)
});

console.log(Math.min(...dp[n - 1]));