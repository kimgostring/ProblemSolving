const fs = require("fs");

const path = process.platform == "linux" ? 0 : "input.txt";
const countMap = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .slice(1)
    .reduce((acc, cur) => {
        if (acc.has(cur)) acc.set(cur, acc.get(cur) + 1);
        else acc.set(cur, 1);

        return acc;
    }, new Map());

console.log([...countMap].sort((a, b) => b[1] - a[1] || (BigInt(a[0]) <= BigInt(b[0]) ? -1 : 1))[0][0]);