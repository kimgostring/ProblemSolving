import copy

def solution(tickets):
    LEN = len(tickets);
    
    edges = dict();
    used = dict();
    for ticket in tickets:
        start, end = ticket;
        if start in edges:
            edges[start].append(end);
            if end in used[start]:
                used[start][end] += 1;
            else:
                used[start][end] = 1;
        else:
            edges[start] = [end];
            used[start] = {end: 1};

    for start in edges.keys():
        edges[start].sort(reverse=True);

    return dfs("ICN", LEN, edges, used);

def dfs(start, LEN, edges, used):
    q = [(-1, start, [], used)];
    
    while q:
        prev, now, answer, visited = q.pop();
        
        if prev != -1 and visited[prev][now] <= 0:
            continue;
        
        answer.append(now);
        if prev != -1:
            visited[prev][now] -= 1;
    
        if len(answer) == LEN + 1: # 종료조건
            return answer;
        
        if now in edges:
            for next in edges[now]:
                if visited[now][next] <= 0:
                    continue;

                nextVisited = copy.deepcopy(visited);
                q.append((now, next, answer[:], nextVisited));