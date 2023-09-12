def solution(n):
    return True if n % sum([int(x) for x in str(n)]) == 0 else False
