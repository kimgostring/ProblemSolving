function solution(phone_book) {
    return !phone_book.sort().some((now, i, arr) => {
       return i !== arr.length - 1 && arr[i + 1].startsWith(now);
    });
}