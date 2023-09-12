def solution(n, m, section):
    cnt = 0
    if m == 1:
        return len(section)
    while True:
        if section == []:
            return cnt
        tmp = section[0] + m - 1
        section = [x for x in section if x > tmp]
        cnt += 1