def solution(n):
    # sum = 0
    # for i in range(8,-1, -1):
    #     q = n // (10**i)
    #     n = n % (10**i)
    #     sum += q
    # return sum
    
    return sum([int(i) for i in str(n)])