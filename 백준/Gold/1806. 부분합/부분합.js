const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const [[n, s], arr] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .map(val => val.split(" ").map(Number));
const prefixSum = arr.reduce((acc, cur, ind) => {
        acc.push(cur + acc[ind]);
        return acc;
    }, [0]);

let answer = Infinity;
let [start, end] = [0, 1];
while (start <= end) {
    while (end < prefixSum.length && prefixSum[end] - prefixSum[start] < s) end++;
    if (end >= prefixSum.length) break;
    
    answer = Math.min(answer, end - start);
    start++;
}

console.log(Number.isFinite(answer) ? answer : 0);