function solution(arr) {
    return arr.filter((value, index) => index === 0 || arr[index - 1] !== value);
}