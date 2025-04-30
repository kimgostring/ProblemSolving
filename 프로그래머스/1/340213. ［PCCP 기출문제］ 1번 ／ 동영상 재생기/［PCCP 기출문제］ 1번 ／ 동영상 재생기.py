def str_to_time(s):
    mm, ss = map(int, s.split(":"))
    return mm * 60 + ss
    
def time_to_str(t):
    mm = t // 60
    ss = t % 60
    return f'{"0" if mm < 10 else ""}{mm}:{"0" if ss < 10 else ""}{ss}'

def solution(video_len, pos, op_start, op_end, commands):
    video_len = str_to_time(video_len)
    op_start = str_to_time(op_start)
    op_end = str_to_time(op_end)
    
    now = str_to_time(pos)
    if op_start <= now <= op_end:
        now = op_end
        
    for c in commands:
        if c == "prev":
            now = 0 if now < 10 else now - 10
        elif c == "next":
            now = video_len if now + 10 > video_len else now + 10
        
        if op_start <= now <= op_end:
            now = op_end

    return time_to_str(now)