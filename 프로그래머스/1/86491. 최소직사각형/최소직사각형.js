function solution(sizes) {
    const size = sizes
        .map((size) => {
            if (size[1] > size[0]) return [size[1], size[0]];
            return size;
        }).reduce((acc, cur) => {
            if (cur[0] > acc[0]) acc[0] = cur[0];
            if (cur[1] > acc[1]) acc[1] = cur[1];
            return acc;
        }, [0, 0]);
    
    return size[0] * size[1];
}