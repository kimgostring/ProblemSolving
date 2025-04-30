def solution(diffs, times, limit):
    l = len(diffs)
    def calc_tot_time(level):
        tot_time = 0
        
        for i in range(l):
            if diffs[i] <= level:
                tot_time += times[i]
            else:
                tot_time += (times[i - 1] + times[i]) * (diffs[i] - level) + times[i]
                
        return tot_time
    
    # parametric_search
    start = 1
    end = max(diffs)
    while start < end:
        mid = (start + end) // 2
        tot_time = calc_tot_time(mid)
        
        if tot_time <= limit:
            end = mid
        else: # 해결 불가 
            start = mid + 1
    
    return end