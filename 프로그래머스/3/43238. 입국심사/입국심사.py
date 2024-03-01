from collections import deque

def solution(n, times):
    times.sort();
    return find(0, times[-1] * n, n, times);

def find(startTime, endTime, n, times):
    midTime = (startTime + endTime) // 2;
    peopleCnt = sum([midTime // time for time in times]);
    print(startTime, endTime, peopleCnt)
        
    if peopleCnt == n: # 정상 종료조건
        return midTime - min([midTime % time for time in times]);
    
    elif startTime > endTime: # 탐색 실패 case
        return startTime;
    
    elif peopleCnt < n: # time이 좀 더 뒤여야
        return find(midTime + 1, endTime, n, times);
        
    else: # time이 좀 더 앞이어야 함 
        return find(startTime, midTime - 1, n, times);