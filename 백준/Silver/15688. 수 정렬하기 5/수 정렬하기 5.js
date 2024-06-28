const fs = require("fs");

const MAX_ABS = 1000000;
const arr = new Array(MAX_ABS * 2 + 1).fill(0);
const [n] = fs.readFileSync(0, encoding="utf8").trim().split("\n")
    .map((val, ind) => {
        if (ind == 0) return Number(val);
        arr[Number(val) + MAX_ABS]++; 
    });

console.log(
    arr.reduce((acc, cnt, val) => {
        for (let i = 0; i < cnt; i++) acc += (val - MAX_ABS) + "\n";
        return acc;
    }, "")
);