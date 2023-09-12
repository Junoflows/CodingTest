def solution(n):
    li = []
    while True :
        
        li.append(n % 3)
        if n // 3 == 0:
            break
        n = n // 3
    
    deci = 0
    for i in range(len(li)):
        deci += 3**i*li.pop()
    
    return deci