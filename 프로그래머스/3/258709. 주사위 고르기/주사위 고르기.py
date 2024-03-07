from itertools import combinations
from collections import deque
from bisect import bisect_right

def solution(dice):
    LEN_DICE = len(dice);
    
    # 모든 주사위 조합  
    comsOfDice = list(combinations(range(LEN_DICE), LEN_DICE // 2));
    LEN_COMS_OF_DICE = len(comsOfDice);
    
    # 각 주사위 조합에서 나올 수 있는 모든 합 계산 
    sumsOfEachCom = [0] * LEN_COMS_OF_DICE;
    for indA in range(LEN_COMS_OF_DICE):
        sumsOfEachCom[indA] = mkAllSums([dice[i] for i in comsOfDice[indA]]);
    LEN_SUMS_OF_COM = len(sumsOfEachCom[0]);
    
    # 이길 수 있는 횟수 cnt
    maxWinCnt = 0;
    answer = 0;
    for indA in range(LEN_COMS_OF_DICE):
        indB = LEN_COMS_OF_DICE - 1 - indA; # 대칭이 되는(B가 선택한) 주사위 조합
        nowWinCnt = 0;
        for sumA in sumsOfEachCom[indA]:
            nowWinCnt += bisect_right(sumsOfEachCom[indB], sumA - 1);
            
        if nowWinCnt > maxWinCnt:
            maxWinCnt = nowWinCnt;
            answer = comsOfDice[indA];
    
    # 이길 수 있는 횟수가 가장 많은 조합 return
    return [x + 1 for x in answer];

def mkAllSums(dices):
    LEN_DICE = len(dices);
    answer = []; 
    q = deque([(1, dices[0][i]) for i in range(6)]);
    
    while q:
        diceCnt, nowSum = q.popleft();
        if diceCnt == LEN_DICE:
            answer.append(nowSum);
            continue;
        
        for i in range(6):
            q.append((diceCnt + 1, nowSum + dices[diceCnt][i]));
    
    answer.sort();
    return answer;
    