def solution(distance, rocks, n):
    rocks.sort();
    rocks = [0] + rocks + [distance];
    LEN = len(rocks) - 1;
    
    # 1. 각 바위 사이의 거리 구하기
    distances = [];
    for i in range(LEN):
        distances.append(rocks[i + 1] - rocks[i]);
    
    # 2. 파라메트릭 서치
    start, end = 0, distance;
    answer = 0;
    while start <= end:
        mid = (start + end) // 2;
        
        i = 0;
        deletedCnt = 0;
        afterDistances = [];
        while i < LEN: # 바위 부수기
            now = distances[i];
            
            while now < mid: # mid만큼의 거리로 만들기
                if i == LEN - 1: # 마지막이 길이 부족 -> 직전 거리와 합치기
                    now += afterDistances.pop();
                    deletedCnt += 1;
                    break;
                    
                i += 1;
                deletedCnt += 1;
                now += distances[i];
            
            afterDistances.append(now);
            i += 1;
        
        # 너무 많은 바위를 부숴야 하는 경우 -> 더 작은 최솟값 만들어야 함 
        if deletedCnt > n: 
            end = mid - 1; 
            
        # 바위를 너무 조금 or 알맞게 부숴야 하는 경우 -> 일단 현재의 최솟값 저장, but 더 큰 최솟값 가능할 수도
        else: 
            start = mid + 1;
            answer = min(afterDistances);
        
    return answer;