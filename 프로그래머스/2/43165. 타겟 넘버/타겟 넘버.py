from collections import deque 

def solution(numbers, target):
    LEN = len(numbers);
    answer = 0;
    
    h = deque([(1, -numbers[0]), (1, numbers[0])]);
    while len(h):
        now = h.popleft();
        
        if now[0] == LEN:
            if now[1] == target:
                answer += 1;
        else:
            next1 = (now[0] + 1, now[1] - numbers[now[0]]);
            next2 = (now[0] + 1, now[1] + numbers[now[0]]);
            h.append(next1);
            h.append(next2);
            
    return answer;