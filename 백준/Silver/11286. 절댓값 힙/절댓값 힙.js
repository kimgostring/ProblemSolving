const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";
const [n, ...inputs] = fs.readFileSync(path, encoding="utf8").trim().split("\n").map(Number);

class AbsMinHeap {
    constructor(size) {
        this.l = 0;
        this.arr = Array(size);
    }

    push(v) {
        this.arr[++this.l] = [Math.abs(v), v];

        let i = this.l;
        while (i > 0) {
            const pi = i >> 1;
            if (pi <= 0) break;
            if (this.arr[i][0] > this.arr[pi][0] || 
                (this.arr[i][0] == this.arr[pi][0] && this.arr[i][1] >= this.arr[pi][1])) break;

            ([this.arr[i], this.arr[pi]] = [this.arr[pi], this.arr[i]]);
            i = pi;
        }
    }

    pop() {
        if (!this.l) return 0;

        const top = this.arr[1][1];
        this.arr[1] = this.arr[this.l--];
        
        let i = 1;
        while (i <= this.l) {
            let ci = i << 1;
            if (ci > this.l) break;
            if (ci + 1 <= this.l && (this.arr[ci + 1][0] < this.arr[ci][0] || 
                (this.arr[ci + 1][0] == this.arr[ci][0] && this.arr[ci + 1][1] < this.arr[ci][1]))) ci++;

            if (this.arr[i][0] < this.arr[ci][0] || 
                (this.arr[i][0] == this.arr[ci][0] && this.arr[i][1] <= this.arr[ci][1])) break;

            ([this.arr[i], this.arr[ci]] = [this.arr[ci], this.arr[i]]);
            i = ci;
        }

        return top;
    }
}

const h = new AbsMinHeap(n);
const answer = [];
for (const v of inputs) {
    if (v) { // push
        h.push(v);
    } else { // pop
        answer.push(h.pop());
    }
}

console.log(answer.join("\n"));