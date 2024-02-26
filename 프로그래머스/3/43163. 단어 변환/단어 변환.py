from collections import deque

def solution(begin, target, words):
    LEN = len(words);
    answer = 0;
    
    visited = [False for _ in range(LEN)];
    q = deque([(begin, 0)]);
    while q:
        now, count = q.popleft();
        
        if now == target:
            answer = count;
            break;
        
        for i in range(LEN):
            if not visited[i] and checkIsChangable(now, words[i]):
                visited[i] = True;
                q.append((words[i], count + 1));
               
    return answer;

def checkIsChangable(a, b):
    count = 0;
    for i in range(len(a)):
        if a[i] != b[i]: 
            count += 1;
            if count > 1:
                break;

    return True if count == 1 else False; 