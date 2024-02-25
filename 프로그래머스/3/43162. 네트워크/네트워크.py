from collections import deque 

def solution(n, computers):
    answer = 0;
    visited = [False for _ in range(n)];
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited, n);
            answer += 1;
    
    return answer;

def bfs(start, path, visited, n):
    q = deque([start]);
    
    while q:
        now = q.popleft();
        
        for i in range(n):
            if path[now][i] and not visited[i]:
                visited[i] = True;
                q.append(i);
