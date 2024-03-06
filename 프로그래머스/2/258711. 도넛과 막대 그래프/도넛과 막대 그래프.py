from collections import defaultdict

def solution(edges):
    # 0. 그래프 자료구조 생성
    graph = defaultdict(list);
    indegree = defaultdict(int);
    for edge in edges:
        start, end = edge;
        graph[start].append(end);
        indegree[end] += 1;
    LEN = max(graph.keys()) + 1;
    
    # 1. 나가는 간선만 있는 경우, new node 후보
    # 이 중 나가는 간선이 2개 이상이면 무조건 new node
    newCandidateNodes = [];
    for node in range(LEN):
        if indegree[node] != 0:
            continue;
        
        if len(graph[node]) > 1:
            newNode = node;
            break;
        newCandidateNodes.append(node);
    
    newNode = newCandidateNodes[0] if newNode == -1 else newNode;
    startNodes = graph[newNode]; # 새 node에서 도달 가능한 모든 노드들에서부터 
    answer = [newNode, 0, 0, 0];
    for start in startNodes:
        answer[getGraphType(start, graph)] += 1;
        
    return answer;

# 그래프 종류에 따라 1(도넛 모양), 2(막대 모양), 3(8자 모양) return 
def getGraphType(start, graph):
    DONUT = 1;
    STICK = 2;
    EIGHT = 3;
    
    if len(graph[start]) == 0: # 갈 수 있는 노드 X -> 막대 그래프의 끝
        return STICK;
    elif len(graph[start]) > 1: # 갈 수 있는 노드 2개 -> 8자 그래프의 중간
        return EIGHT;
    
    # 갈 수 있는 노드 1개
    graphType = DONUT;
    now = graph[start][0];
    while now != start:
        if len(graph[now]) == 0:
            graphType = STICK;
            break;
        elif len(graph[now]) > 1:
            graphType = EIGHT;
            break;
        now = graph[now][0];
    # while 탈출하지 않고 그냥 순환 -> 도넛 모양
    
    return graphType;