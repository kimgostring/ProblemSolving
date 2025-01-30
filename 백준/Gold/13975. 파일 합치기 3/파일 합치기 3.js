const fs = require("fs");
const path = process.platform === "linux" ? 0 : "BOJ/input.txt";

const input = fs.readFileSync(path, encoding = "utf8").trim().split("\n")[Symbol.iterator]();

class MinHeap {
  constructor(arr) {
    this.size = arr.length; // last index
    this.arr = [0].concat(arr);
    this.heapify();
  }

  push(value) {
    let i = ++this.size;
    let parent = Math.floor(i / 2);
    while (parent > 0 && this.arr[parent] > value) {
      this.arr[i] = this.arr[parent];

      i = parent;
      parent = Math.floor(i / 2);
    }

    this.arr[i] = value;
  }

  pop() {
    [this.arr[1], this.arr[this.size]] = [this.arr[this.size], this.arr[1]];
    const value = this.arr[this.size--];

    this._adjust(1);
    return value;
  }

  heapify() {
    for (let i = Math.floor(this.size / 2); i > 0; i--)
      this._adjust(i);
  }

  _adjust(i) {
    const value = this.arr[i];

    let child = i * 2;
    while (child <= this.size) {
      if (child + 1 <= this.size && this.arr[child + 1] < this.arr[child]) child++;
      if (value <= this.arr[child]) break;

      this.arr[i] = this.arr[child];

      i = child;
      child = i * 2;
    }
    
    this.arr[i] = value;
  }
}

const T = Number(input.next().value);
for (let _ = 0; _ < T; _++) {
  const K = Number(input.next().value);
  const h = new MinHeap(input.next().value.split(" ").map(e => Number(e)));

  let ans = 0;
  while (h.size > 1) {
    const price = h.pop() + h.pop();
    ans += price;

    h.push(price);
  }

  console.log(ans);
}