def solution(k, score):
    answer = []
    for i in range(len(score)):
        li = sorted(score[:i+1])
        if len(li) <= k:
            answer.append(li[0])
        else:
            answer.append(li[-k])
    return answer