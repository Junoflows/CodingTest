def solution(n, left, right):
    if left // n < right // n:
        mid_li = []
        for i in range(left // n + 1, right // n):
            li = [i+1 for _ in range(i)] + [j+1 for j in range(i,n)]  
            mid_li += li
        
        idx = left // n
        left_li = [idx+1 for _ in range(idx)] + [j+1 for j in range(idx,n)]

        idx = right // n
        right_li = [idx+1 for _ in range(idx)] + [j+1 for j in range(idx,n)]

        return left_li[left % n:] + mid_li + right_li[:right % n + 1]
    
    elif left // n == right // n:
        idx = left // n
        left_li = [idx+1 for _ in range(idx)] + [j+1 for j in range(idx,n)]
        
        return left_li[left % n : right % n + 1]
