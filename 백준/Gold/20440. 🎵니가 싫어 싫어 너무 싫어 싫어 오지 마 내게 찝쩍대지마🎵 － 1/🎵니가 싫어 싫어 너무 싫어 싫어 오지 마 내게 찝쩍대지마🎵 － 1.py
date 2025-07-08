import sys
input = sys.stdin.readline
from heapq import heapify, heappush, heappop

END = 2100000010

n = int(input())
mosquitoes_not_in_yet = [tuple(map(int, input().rstrip().split(" "))) for _ in range(n)]
heapify(mosquitoes_not_in_yet)

now = 0
ans_num = 0 # 마지막에 -1 해주기  
ans_term = [-1, -1]
mosquitoes_in = [END]
while now != END:
    while mosquitoes_not_in_yet and mosquitoes_not_in_yet[0][0] < mosquitoes_in[0]:
        now, e = heappop(mosquitoes_not_in_yet)
        heappush(mosquitoes_in, e)
        if len(mosquitoes_in) == ans_num and now == ans_term[1]:
            # now 시간에 한 모기가 나가고 다른 모기가 바로 들어온 case
            edit_end_term_flag = True
        elif len(mosquitoes_in) > ans_num:
            edit_end_term_flag = True
            ans_num = len(mosquitoes_in)
            ans_term[0] = now

    while mosquitoes_in and (
        not mosquitoes_not_in_yet or mosquitoes_in[0] <= mosquitoes_not_in_yet[0][0]
    ):
        now = heappop(mosquitoes_in)
        if ans_num == len(mosquitoes_in) + 1 and edit_end_term_flag:
            edit_end_term_flag = False
            ans_term[1] = now

print(ans_num - 1)
print(*ans_term, sep=" ")
