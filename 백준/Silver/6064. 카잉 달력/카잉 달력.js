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
    if (!(m % n)) [m, n, x, y] = [n, m, y, x];

    if (m === x && n === y) {
        answers += `${lcm(m, n)}\n`;
        continue;
    } 

    const remain = x === m ? 0 : x;
    let answer = -1;
    for (let i = 0; i < lcm(m, n); i += n) {
        const year = i + y;
        if (year % m === remain) {
            answer = year;
            break;
        }
    }
    answers += `${answer}\n`;
}

console.log(answers);