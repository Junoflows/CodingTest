def solution(sizes):
    maxi = [max(sizes[i]) for i in range(len(sizes))]
    mini = [min(sizes[i]) for i in range(len(sizes))]

    return max(maxi) * max(mini)