def solution(a, b):
    li = [31 if x in [1,3,5,7,8,10,12] else 30 for x in range(1,13)]
    li[1] = 29
    days = sum(li[:a-1]) + b - 1
    
    if days % 7 == 0: return 'FRI'
    elif days % 7 == 1: return 'SAT'
    elif days % 7 == 2: return 'SUN'
    elif days % 7 == 3: return 'MON'
    elif days % 7 == 4: return 'TUE'
    elif days % 7 == 5: return 'WED'
    else: return 'THU'