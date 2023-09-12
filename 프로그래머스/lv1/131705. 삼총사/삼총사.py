def solution(number):
    cnt = 0
    for i in range(len(number)):
        for j in range(i,len(number)):
            if j == i :
                continue
            for k in range(j,len(number)):
                if k == i or k == j:
                    continue
                
                if number[i] + number[j] + number[k] == 0:
                    cnt += 1
                    
    return cnt