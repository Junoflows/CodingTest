def solution(t, p):
    li = [t[i:i+len(p)] for i in range(len(t)-len(p)+1)]
    return len([x for x in li if x <= p])