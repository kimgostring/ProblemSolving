const fs = require("fs");

const path = process.platform === "linux" ? 0 : "input.txt";
const [t, ...ls] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .map((e, i) => {
        if (i === 0) return Number(e);
        else return e.split(" ").map(Number);
    });

const gcd = (a, b) => {
    const r = a % b;
    if (!r) return b 
    return gcd(b, r);
};
const lcm = (a, b) => a / gcd(a, b) * b;

let answers = "";
for (const l of ls) {
    let [m, n, x, y] = l;
    if (m < n) [m, n, x, y] = [n, m, y, x];
    if (x === m) x = 0;
    if (y === n) y = 0;
    
    let answer = -1;
    const lastYear = lcm(m, n);
    for (let i = x || m; i <= lastYear; i += m) {
        if (i % n === y) {
            answer = i;
            break;
        }
    }
    answers += `${answer}\n`;
}

console.log(answers);