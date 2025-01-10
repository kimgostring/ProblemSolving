const fs = require("fs");
const path = process.platform === "linux" ? 0 : "BOJ/input.txt";

const [[n, m], nums] = fs
  .readFileSync(path, (encoding = "utf8"))
  .trim()
  .split("\n")
  .map(e => e.split(" ").map(Number));

let q = Array.from({ length: n }, (_, i) => n - i);
const ans = nums.reduce((acc, cur) => {
  const i = q.findIndex(e => e === cur);
  const cnt = Math.min(i + 1, q.length - (i + 1));
  q = [...q.slice(i + 1), ...q.slice(0, i)];

  return acc + cnt;
}, 0);

console.log(ans);