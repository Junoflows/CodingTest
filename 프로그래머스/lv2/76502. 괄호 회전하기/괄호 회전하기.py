def solution(s):
    cnt = 0
    for _ in range(len(s)):
        s = s[1:] + s[0]
        stack = []
        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])
            else : 
                if stack == []: break
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                else: break

            if i == len(s) - 1 and stack == []:
                cnt += 1
        
    print(stack, cnt)
    return cnt
#     for _ in range(len(s)):
#         s = s[1:]+s[0]
    
#     print(cnt)