def solution(N, stages):
    rate = []
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        if length == 0:
            rate.append(0)
        else:
            rate.append(stages.count(i) / length)
            length -= stages.count(i)
    
    dic = {index : value for index, value in enumerate(rate)}
    SET = set(dic.values())
    while True:
        if len(SET) == 0:
            break
        li = [key for key, value in dic.items() if dic[key] == max(SET)]
        answer.extend(li)
        SET.remove(max(SET))
        
    return [x+1 for x in answer]