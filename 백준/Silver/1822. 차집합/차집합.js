const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

let [[na, nb], a, b] = fs
  .readFileSync(path, (encoding = "utf8"))
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map((ee) => parseInt(ee)));
b.sort((e1, e2) => e1 - e2);

const binarySearch = (e) => {
  let l = 0, r = nb - 1, mid;

  while (l <= r) {
    mid = Math.floor((l + r) / 2);

    if (b[mid] < e) l = mid + 1;
    else if (b[mid] > e) r = mid - 1;
    else return true;
  }

  return false;
};

const ans = [];
a.forEach((e) => {
  if (!binarySearch(e)) ans.push(e);
});
ans.sort((e1, e2) => e1 - e2);

console.log(ans.length);
if (ans.length) console.log(ans.join(" "));
