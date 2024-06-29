const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";
console.log(
    fs.readFileSync(path, encoding="utf8").trim().split("\n")
        .slice(1)
        .map((cord) => cord.split(" ").map((e) => Number(e)))
        .sort((a, b) => a[1] - b[1] || a[0] - b[0])
        .reduce((acc, cur) => `${acc}${cur[0]} ${cur[1]}\n`, "")
);