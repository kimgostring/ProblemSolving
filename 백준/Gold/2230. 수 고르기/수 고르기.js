const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const inputs = fs.readFileSync(path, encoding="utf8").trim().split("\n");
const [n, m] = inputs[0].split(" ").map(Number);
const arr = inputs.slice(1).map(Number).sort((a, b) => a - b);

let answer = Infinity;
let [start, end] = [0, 0];
while (start <= end && end < arr.length) {
    const now = arr[end] - arr[start];
    if (now >= m) {
        answer = Math.min(now, answer);
        if (answer === m) break;
        start++;
    } else end++;
}

console.log(answer);