def solution(s):
    s = list(s)
    
    x = s.pop(0)
    x_cnt, cnt, s_cnt = 1, 0, 0
        
    while True:
        if len(s) <= 1:
            return s_cnt+1
        
        if s.pop(0) == x:
            x_cnt += 1
        else: cnt += 1

        if x_cnt == cnt:
            s_cnt += 1
            x = s.pop(0)
            x_cnt, cnt = 1, 0