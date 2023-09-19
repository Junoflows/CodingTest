def solution(s):
    stack = []
    # s = list(s)
    for i in range(len(s)):
         
        if s[i] == '(':
            stack.append(s[i])

        else:
            if stack == []:
                return False
            else:
                stack.pop()
            # else: return False
    
    if stack == []:
        return True
    else: return False