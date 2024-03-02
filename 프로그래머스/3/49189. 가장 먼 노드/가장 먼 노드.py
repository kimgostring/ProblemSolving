from collections import deque

def solution(n, edge):
    links = [[] for _ in range(n + 1)];
    for e in edge:
        start, end = e;
        links[start].append(end);
        links[end].append(start);

    return bfs(1, links);

def bfs(nodeNum, links):
    q = deque([nodeNum]);
    cnt = [0] * len(links);
    
    while q:
        now = q.popleft();
        
        for e in links[now]:
            if e != nodeNum and cnt[e] == 0: # 방문 가능
                q.append(e);
                cnt[e] = cnt[now] + 1;
    
    cnt.sort();
    return cnt.count(cnt[-1]);