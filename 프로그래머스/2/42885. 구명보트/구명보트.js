function solution(people, limit) {
    people.sort((a,b) => a - b);
    
    let cnt = 0;
    let start = 0;
    let end = people.length - 1;
    while (start < end && people[start] !== people[end]) {
        if (people[start] + people[end] <= limit) start++;
        
        end--;
        cnt++;
    }
    
    if (start <= end) {
        if (people[start] * 2 <= limit) cnt += Math.ceil((end - start + 1) / 2);
        else cnt += (end - start + 1);
    }
    
    return cnt;
}