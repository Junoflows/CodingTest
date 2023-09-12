def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            cnt = 1
            while True:
                if s[i] == s[:i][-cnt]:
                    answer.append(cnt)
                    break
                else:
                    cnt += 1
            continue
        else:
            answer.append(-1)
        
    return answer