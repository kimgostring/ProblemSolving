from collections import deque

def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)];
    for result in results:
        winner, loser = result;
        graph[winner][loser] = 1;
        
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = 1 if graph[i][k] == graph[k][j] == 1 else graph[i][j];
    
    answer = 0;
    reversedGraph = list(map(list, zip(*graph)));
    for i in range(1, n + 1):
        if graph[i].count(1) + reversedGraph[i].count(1) == n - 1:
            answer += 1;

    return answer
