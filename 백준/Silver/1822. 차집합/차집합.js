const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

let [[na, nb], a, b] = fs
  .readFileSync(path, (encoding = "utf8"))
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map((ee) => parseInt(ee)));
b = new Set(b);

const ans = [];
a.forEach((e) => {
  if (!b.has(e)) ans.push(e);
});
ans.sort((e1, e2) => e1 - e2);

console.log(ans.length);
if (ans.length) console.log(ans.join(" "));
