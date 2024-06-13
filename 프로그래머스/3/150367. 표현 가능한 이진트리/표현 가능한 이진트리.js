function solution(numbers) {
    return numbers.map((num) => {
        const binStr = num.toString(2);
        const height = Math.ceil(Math.log2(binStr.length) || 1);
        
        const bin = new Array(2 ** height - binStr.length)
            .fill(0)
            .concat([...binStr].map((el) => Number(el)));
        
        return canBeTree(bin.length / 2, height, bin) !== -1 ? 1 : 0;
    });
}

// return 0 -> 모든 subtree가 0
// return 1 -> 가능
// return -1 -> 불가능
function canBeTree(node, height, bin) { 
    // leaf
    if (height === 1) return bin[node];
    
    // nonleaf
    const left = node - 2 ** (height - 2);
    const right = node + 2 ** (height - 2);
    
    if (bin[node] === 0) {
        // 모든 자식이 0이어야 함
        if (canBeTree(left, height - 1, bin) === 0 && canBeTree(right, height - 1, bin) === 0) 
            return 0;
    } else {
        // 모든 자식이 -1이 아니어야 함
        if (canBeTree(left, height - 1, bin) !== -1 && canBeTree(right, height - 1, bin) !== -1) 
            return 1;
    }
        
    // 트리 형성 불가
    return -1;
}