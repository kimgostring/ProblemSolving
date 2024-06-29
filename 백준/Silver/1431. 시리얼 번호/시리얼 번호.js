const fs = require("fs");
const path = process.platform === "linux" ? 0 : 'input.txt';

const [n, ...serials] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
    .map((val, ind) => {
        if (ind == 0) return Number(val);
        return val;
    });

const sumDigits = (str) => str
    .split('')
    .filter((val) => '0' <= val && '9' >= val)
    .reduce((acc, cur) => acc + Number(cur), 0);

console.log(
    serials.sort((a, b) => {
        return (a.length - b.length)
            || (sumDigits(a) - sumDigits(b))
            || (a <= b ? -1 : 1);
    }).reduce((acc, cur) => acc += cur + "\n", "")
);