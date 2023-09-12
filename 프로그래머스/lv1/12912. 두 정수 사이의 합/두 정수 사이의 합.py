def solution(a, b):
    if a == b:
        return a
    elif a < b:
        tmp = b - a
        return sum([a+i for i in range(tmp+1)])
    else:
        tmp = a - b
        return sum([b+i for i in range(tmp+1)])