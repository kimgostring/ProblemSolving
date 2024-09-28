const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const [n, m] = fs.readFileSync(path, encoding="utf8").trim().split(" ").map(Number);

const combination = (n, m) => {
    const res = [];

    function gen(selected, start) {
        if (selected.length === m) res.push(selected.join(" "));
        else for (let i = start; i <= n; i++) gen([...selected, i], i + 1);
    }
    gen([], 1);

    return res;
};

console.log(combination(n, m).join("\n"));