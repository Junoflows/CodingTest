def solution(a, b, n):
    cnt = 0
    while True:
        cnt += (n // a) * b
        n = (n // a) * b + n % a
        
        if n < a:
            break

    return cnt