const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

console.log(
    fs.readFileSync(path, encoding="utf8").trim().split("\n")
        .slice(1)
        .sort((a, b) => Number(b) - Number(a))
        .join("\n")
);