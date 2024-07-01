const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const [n, ...arr] = fs.readFileSync(path, encoding="utf8").trim().split("\n").map(Number);
const dp = new Array(n).fill(0);
const dp2 = new Array(n).fill(0);

arr.forEach((score, i) => {
    if (i == 0) dp[i] = score;
    else if (i == 1) {
        dp[i] = Math.max(dp[i - 1], score);
        dp2[i] = dp[i - 1] + score;
    }
    else {
        dp[i] = Math.max(dp[i - 2] + score, dp2[i - 2] + score);  
        dp2[i] = dp[i - 1] + score;
    }
});

console.log(Math.max(dp[n - 1], dp2[n - 1]));