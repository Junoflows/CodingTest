from collections import Counter
def solution(nums):
    dic = Counter(nums)
    keys = list(dic.keys())
    return len(keys) if len(nums)/2 >= len(keys) else len(nums)/2