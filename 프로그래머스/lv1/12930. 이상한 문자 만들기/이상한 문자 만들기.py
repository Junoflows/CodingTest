def solution(s):
    li = s.split(' ')
    answer = []
    for a in li:
        str = ''.join([a[i].upper() if i % 2 ==0 else a[i].lower() for i in range(len(a))])
        answer.append(str)
    
    return ' '.join(answer)