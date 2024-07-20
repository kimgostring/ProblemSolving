const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const [[n, s], arr] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .map(val => val.split(" ").map(Number));

let answer = Infinity;
let sum = arr[0];
let [start, end] = [0, 0];
while (start <= end) {
    while (end < n && sum < s) sum += arr[++end];
    if (end >= n) break;
    
    answer = Math.min(answer, end - start + 1);
    sum -= arr[start++];
}

console.log(Number.isFinite(answer) ? answer : 0);