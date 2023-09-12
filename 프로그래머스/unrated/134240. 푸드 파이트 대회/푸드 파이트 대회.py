def solution(food):
    l_li = ''
    for i in range(1,len(food)):
        cnt = food[i] // 2
        for j in range(cnt):
            l_li += str(i)
        
    answer = l_li + '0' + l_li[::-1]
    return answer
        