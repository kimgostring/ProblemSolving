const fs = require("fs");
const path = process.platform === "linux" ? 0 : "BOJ/input.txt";

const [[n, m], nums] = fs.readFileSync(path, encoding="utf8").trim().split("\n")
  .map(e => e.split(" ").map(Number));

class ShiftableQueue {
  constructor(n) {
    // 구현체의 맨 뒤가 맨 앞 
    this.q = Array.from({ length: n }, (_, i) => n - i);
  }

  findAndShift(target) {
    // 1. target index 찾기
    const end = this.q.findIndex(e => e === target);

    // 2. target이 구현체의 마지막 위치에 오도록 shift
    const cnt = this.shift(end);

    // 3. 제거 (pop)
    this.q.pop();

    // 리턴값 = shift 횟수
    return cnt;
  }

  // end가 n - 1 위치에 오도록 shift
  shift(end) {
    // shift 필요 없음 
    if (end === n - 1) return 0;

    // shift 필요
    this.q = [...this.q.slice(end + 1), ...this.q.slice(0, end + 1)];
    return Math.min(end + 1, this.q.length - (end + 1));
  }
}

const q = new ShiftableQueue(n);
const ans = nums.reduce((acc, cur) => acc + q.findAndShift(cur), 0);

console.log(ans);