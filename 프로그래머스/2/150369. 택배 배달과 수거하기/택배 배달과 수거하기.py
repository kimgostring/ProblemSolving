def solution(cap, n, deliveries, pickups):
    answer = 0;
    
    # 최대한 가장 마지막 집부터 방문 + 최대한 많은 박스 수거
    delInd = n - 1;
    pickInd = n - 1;
    while delInd >= 0 or pickInd >= 0:
        # 배달할 택배 싣기
        maxDelInd, delInd = calcInd(cap, deliveries, delInd);
        # 빈 박스 수거
        maxPickInd, pickInd = calcInd(cap, pickups, pickInd);
        
        answer += (max(maxDelInd, maxPickInd) + 1) * 2;
        
    return answer;

# 현재 집에서부터 박스 싣기/수거
def calcInd(cap, arr, ind): 
    maxInd = -1;
    nowCap = cap;
    while nowCap > 0 and ind >= 0:
        if arr[ind] > 0: 
            if maxInd == -1:
                maxInd = ind;
            boxCnt = min(arr[ind], nowCap);

            arr[ind] -= boxCnt;
            nowCap -= boxCnt;
    
        if arr[ind] == 0:
            ind -= 1;
    
    return maxInd, ind;
    