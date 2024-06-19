const fs = require("fs");
const path = process.platform === "linux" ? '/dev/stdin' : 'input.txt';
const [n, ...board] = fs.readFileSync(path).toString().trim().split("\n")
    .map((val, ind) => {
        if (ind == 0) return Number(val);
        else return val.split("");
    });

console.log(cntArea(board, false), cntArea(board, true));

function cntArea(board, isColorBlind) {
    const n = board.length;
    const visited = Array.from(Array(n), () => Array(n).fill(false));
    function bfs(cord, isColorBlind) {
        const D = [[0, 1], [0, -1], [1, 0], [-1, 0]];

        const BLIND_COLOR = ["R", "G"];
        const color = board[cord[0]][cord[1]];
        if (!BLIND_COLOR.includes(color)) isColorBlind = false;

        const q = Array(n * n);
        let head = 0, tail = 0;
        q[tail++] = cord;
        visited[cord[0]][cord[1]] = true;
        while (head !== tail) {
            const [x, y] = q[head++];
    
            for (const [dx, dy] of D) {
                const [nextX, nextY] = [x + dx, y + dy];
    
                if (nextX < 0 || nextX >= n || nextY < 0 || nextY >= n) continue;
                if (visited[nextX][nextY]) continue;
                if (board[nextX][nextY] !== color
                    && !(isColorBlind && BLIND_COLOR.includes(board[nextX][nextY]))) continue;
    
                visited[nextX][nextY] = true;
                q[tail++] = [nextX, nextY];
            }
        } 
    }; 

    let answer = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (visited[i][j]) continue;    
            bfs([i, j], isColorBlind);
            answer++;
        }
    }

    return answer; 
}