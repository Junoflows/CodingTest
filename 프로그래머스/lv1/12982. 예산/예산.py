def solution(d, budget):
    d.sort()
    print(d)
    hap = 0
    for i in range(len(d)):
        hap += d[i]
        if hap > budget:
            return i
    
    return i+1
        