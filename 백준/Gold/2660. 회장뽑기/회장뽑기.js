const fs = require("fs");
const path = process.platform === "linux" ? 0 : "input.txt";

// 1. 인풋 입력받기, 그래프 생성
const [N, ...edges] = fs
  .readFileSync(path, (encoding = "utf8"))
  .trim()
  .split("\n")
  .map((e, i) => (i ? e.split(" ").map(Number) : Number(e)));
edges.pop();

const dp = Array.from({ length: N }, () => Array(N).fill(Infinity));
for (let i = 0; i < N; i++) dp[i][i] = 0;
edges.forEach(([s, e]) => {
  s--, e--;
  dp[s][e] = 1;
  dp[e][s] = 1;
});

// 플로이드 워셜
for (let k = 0; k < N; k++)
  for (let s = 0; s < N; s++)
    for (let e = 0; e < N; e++)
      dp[s][e] = Math.min(dp[s][e], dp[s][k] + dp[k][e]);


const all = dp
  .map((e, i) => [Math.max(...e), i + 1])
  .sort((a, b) => a[0] - b[0]);
const minScore = all[0][0];
const candidates = all.filter(e => e[0] === minScore).map((e) => e[1]);

console.log(minScore, candidates.length);
console.log(candidates.join(" "));
