def solution(left, right):
    return sum([-n if n == int(n ** 0.5)**2 else n for n in range(left, right+1) ])
        