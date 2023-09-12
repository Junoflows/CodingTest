def solution(s, n):
    li = list(s)
    for i in range(len(li)):
        if li[i].isupper():
            li[i] = chr((ord(li[i]) - ord('A')+n) % 26 + ord("A"))
        elif li[i].islower():
            li[i] = chr((ord(li[i]) - ord('a')+n) % 26 + ord("a"))
                
    return ''.join(li)