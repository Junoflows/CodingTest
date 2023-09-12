from itertools import combinations
def solution(nums):
    li = list(combinations(nums, 3))
    cnt = 0
    haps = [sum(x) for x in li if sum(x) % 2 != 0]
    for num in haps:
        tmp = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                tmp += 1
            
        if tmp == 1:
            cnt += 1
        
    return cnt