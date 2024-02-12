function solution(citations) {
    const h = citations.sort((a, b) => b - a).findIndex((val, ind) => val <= ind);
    return h >= 0 ? h : citations.length;
}