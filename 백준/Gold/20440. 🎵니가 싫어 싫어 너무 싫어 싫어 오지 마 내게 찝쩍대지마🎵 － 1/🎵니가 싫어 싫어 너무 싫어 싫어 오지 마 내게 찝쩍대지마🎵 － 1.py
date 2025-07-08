import sys
input = sys.stdin.readline
from heapq import heappush, heappop

END = 2100000010

n = int(input())
mosquitoes = [tuple(map(int, input().rstrip().split(" "))) for _ in range(n)]
mosquitoes.sort()

m_idx = 0
now_t = 0
ans_num = 0 # 마지막에 -1 해주기
ans_term = [-1, -1]
mosquitoes_in = [END]
while now_t != END:
    while m_idx < n and mosquitoes[m_idx][0] < mosquitoes_in[0]:
        now_t, end_t = mosquitoes[m_idx]
        m_idx += 1
        
        heappush(mosquitoes_in, end_t)
        if len(mosquitoes_in) == ans_num and now_t == ans_term[1]:
            # now 시간에 한 모기가 나가고 다른 모기가 바로 들어온 case
            edit_end_term_flag = True
        elif len(mosquitoes_in) > ans_num:
            edit_end_term_flag = True
            ans_num = len(mosquitoes_in)
            ans_term[0] = now_t

    while mosquitoes_in and (m_idx >= n or mosquitoes_in[0] <= mosquitoes[m_idx][0]):
        now_t = heappop(mosquitoes_in)
        if ans_num == len(mosquitoes_in) + 1 and edit_end_term_flag:
            edit_end_term_flag = False
            ans_term[1] = now_t

print(ans_num - 1)
print(*ans_term, sep=" ")
