def solution(a, b):
    return sum([a[idx]*b[idx] for idx in range(len(a))])