def solution(s, skip, index):
    answer = ''
    for i in range(len(s)):
        cnt = 0
        tmp = ord(s[i])
        while cnt != index:
            if chr(tmp+1) <= 'z':
                if chr(tmp+1) not in skip:
                    cnt += 1
                tmp += 1
                
            elif chr(tmp+1) > 'z':
                if chr(tmp+1-26) not in skip:
                    cnt += 1
                tmp = tmp - 25
                
        answer += chr(tmp)
    return answer