from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    def make_cond_str(l, j, e, f):
        return f'{l} and {j} and {e} and {f}'
    
    # key가 가능한 cond 조합, value가 코테 점수 list인 map
    score_list_by_cond = defaultdict(list)    
    for i in info:
        lang, job, experience, food, score = i.split(" ")
        score = int(score)
        for l in [lang, "-"]:
            for j in [job, "-"]:
                for e in [experience, "-"]:
                    for f in [food, "-"]:
                        score_list_by_cond[make_cond_str(l, j, e, f)].append(score)
    for k in score_list_by_cond:
        score_list_by_cond[k].sort()
        
    ans = []
    for q in query:
        cond, score = q.rsplit(" ", 1)
        score = int(score)
        
        score_list = score_list_by_cond[cond]
        ans.append(len(score_list) - bisect_left(score_list, score))
    
    return ans