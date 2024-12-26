const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

const students = fs.readFileSync(path, encoding="utf8").trim().split("\n");
const [K, L] = students.shift().split(" ").map(e => Number(e));

const map = new Map();
for (const [i, student] of students.entries()) map.set(student, i);

const ans = [];
for (const [i, student] of students.entries()) {
    if (map.get(student) === i) ans.push(student);
    if (ans.length === K) break;
}
console.log(ans.join("\n"));