const path = process.platform === "linux" ? 0 : "input.txt";
const [n, m] = require("fs").readFileSync(path, encoding="utf8").trim().split(" ").map(Number);

const permWithRept = (n, m) => {
    const res = [];

    function gen(selected) {
        if (selected.length === m) res.push(selected.join(" "));
        else for (let i = 1; i <= n; i++) gen([...selected, i]);
    }
    gen([]);

    return res;
};

console.log(permWithRept(n, m).join("\n"));