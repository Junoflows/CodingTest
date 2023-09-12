def solution(number, limit, power):
    div_cnt = []
    for num in range(1, number+1):
        if num == 1:
            div_cnt.append(1)
        else:
            cnt = 0
            for div in range(1, int(num**0.5)+1):
                if num % div == 0:
                    cnt += 2
            if num % (num**0.5) == 0:
                cnt -= 1
            div_cnt.append(cnt)
    
    li = [x if x <= limit else power for x in div_cnt ]
    return sum(li)