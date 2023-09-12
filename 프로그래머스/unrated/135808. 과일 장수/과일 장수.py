def solution(k, m, score):
    score = sorted(score)
    tmp = []
    answer = 0
    
    while True:

        if len(score) < m:
            return answer
        tmp = [score.pop() for i in range(m)]
        answer += min(tmp) * m

    