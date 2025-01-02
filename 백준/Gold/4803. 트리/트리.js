const fs = require("fs");
const path = process.platform === "linux" ? 0 : "BOJ/input.txt";

class Forest {
  constructor(n) {
    this.parents = Array.from({ length: n + 1 }, (_, i) => i);
    this.isGraphNotTree = new Set([0]);
  }

  find(a) {
    let root = a;
    while (root !== this.parents[root]) root = this.parents[root];

    while (a !== this.parents[a]) {
      a = this.parents[a];
      this.parents[a] = root;
    }

    return root;
  }

  union(a, b) {
    let rootOfA = this.find(a);
    let rootOfB = this.find(b);

    // 이미 같은 tree인 경우
    if (rootOfA === rootOfB) {
      this.isGraphNotTree.add(rootOfA);
      return;
    }

    // 둘 중 하나가 이미 tree가 아닌 경우, 합쳐진 tree 또한 더는 tree가 아니게 됨
    if (this.isGraphNotTree.has(rootOfA) || this.isGraphNotTree.has(rootOfB)) {
      this.isGraphNotTree.add(rootOfA);
      this.isGraphNotTree.add(rootOfB);
      return;
    }

    // A와 B가 모두 tree이고, rootOfA !== rootOfB 인 경우
    if (rootOfA > rootOfB) [a, rootOfA, b, rootOfB] = [b, rootOfB, a, rootOfA];
    this.parents[rootOfB] = rootOfA;
  }

  flatten() {
    this.parents = this.parents.map(a => this.find(a));
  }

  calcNumOfTrees() {
    this.flatten();
    return new Set(this.parents).size - this.isGraphNotTree.size;
  }
}

const inputs = fs
  .readFileSync(path, (encoding = "utf8"))
  .trim()
  .split("\n")
  .map(e => e.split(" ").map(Number))
  [Symbol.iterator]();

let tc = 1;
while (true) {
  const [n, m] = inputs.next().value;
  if (!n && !m) break;

  const forest = new Forest(n);
  for (let i = 0; i < m; i++) forest.union(...inputs.next().value);

  const numOfTrees = forest.calcNumOfTrees();
  let ans = `Case ${tc++}: `;
  if (numOfTrees === 0) ans += "No trees.";
  else if (numOfTrees === 1) ans += "There is one tree.";
  else ans += `A forest of ${numOfTrees} trees.`;
  console.log(ans);
}
