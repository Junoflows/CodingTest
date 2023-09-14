def solution(n, left, right):
    mid_li = []
    for i in range(left // n + 1, right // n):
        li = [i+1 for _ in range(i)] + [j for j in range(i+1,n+1)]  
        mid_li += li
    
    if left // n < right // n:
        idx = left // n
        left_li = [idx+1 for _ in range(idx)] + [j for j in range(idx+1,n+1)]

        idx = right // n
        right_li = [idx+1 for _ in range(idx)] + [j for j in range(idx+1,n+1)]

        return left_li[left % n:] + mid_li + right_li[:right % n +1]
    
    elif left // n == right // n:
        idx = left // n
        left_li = [idx+1 for _ in range(idx)] + [j for j in range(idx+1,n+1)]
        
        return left_li[left % n : right % n + 1]