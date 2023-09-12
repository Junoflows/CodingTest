def solution(arr, divisor):
    answer = sorted([x for x in arr if x % divisor == 0])
    if answer == []:
        return [-1]
    else:
        return answer