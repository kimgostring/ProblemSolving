const fs = require("fs");

const path = process.platform === "linux" ? 0 : "input.txt";
const [n, m] = fs.readFileSync(path, encoding="utf8").trim().split(" ").map(Number);

// 각각 0, 90, 180, 270 회전한 모양
const UNIT = [
    [[0, 0], [0, 1], [1, 1], [1, 0]],
    [[0, 0], [1, 0], [1, 1], [0, 1]],
    [[1, 1], [1, 0], [0, 0], [0, 1]],
    [[1, 1], [0, 1], [0, 0], [1, 0]],
];
const rotate = (dir, clockwise=true) => clockwise ? (dir + 1) % 4 : (dir + 3) % 4;

function calcCords(k, steps, x, y, dir) { // x, y는 가장 왼쪽 아래 좌표 
    if (k === 1) {
        const [dx, dy] = UNIT[dir][steps];
        return [x + dx, y + dy];
    };

    k--;
    const nl = 2 ** k;
    const nSize = nl ** 2;
    const nFractal = Math.floor(steps / nSize);
    
    const [dx, dy] = UNIT[dir][nFractal];
    x += dx * nl;
    y += dy * nl;

    // 현재 조각이 0, 180도로 돌아가 있는 경우, 0일 때 시계방향 90도, 3일 때 270도 돌려야 함 
    // 현재 조각이 90, 270 돌아가 있는 경우, 방향 반대 (반시계)
    if (nFractal === 0) dir = rotate(dir, dir % 2 === 0);
    else if (nFractal === 3) dir = rotate(dir, dir % 2 !== 0);

    return calcCords(k, steps % nSize, x, y, dir);
}

console.log(calcCords(Math.log2(n), m - 1, 1, 1, 0).join(" "));
