from bisect import bisect_right

def solution(tickets):
    sortedTickets = sorted(tickets, key=lambda x: (x[0], x[1]));
    starts, ends = list(zip(*sortedTickets));
    
    return dfs("ICN", starts, ends);

def dfs(start, starts, ends):
    LEN = len(starts);
    # (now, index of tickets, answer, used) 
    q = [(start, LEN, [start], [False for _ in range(LEN + 1)])];

    while q:
        now, index, answer, used = q.pop();
        
        # 방문 처리
        if used[index]:
            continue; 
        used[index] = True;
        
        # 종료 조건 (정답 찾음)
        if len(answer) == LEN + 1: 
            return answer;
    
        # 큰 알파벳 순으로 stack에 넣어야, 가장 작은 값부터 탑색 가능
        i = bisect_right(starts, now) - 1;
        while i < LEN and starts[i] == now:
            if not used[i]:
                next = ends[i];
                nextUsed = used[:];

                q.append((next, i, answer + [next], nextUsed));
            i -= 1;
            
    