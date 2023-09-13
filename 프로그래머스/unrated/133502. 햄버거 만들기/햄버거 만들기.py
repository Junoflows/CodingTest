from collections import deque
def solution(ingredient):
    # string = ''.join([str(x) for x in ingredient])
    stack  = []
    cnt = 0
    for s in ingredient:
        stack.append(s)
        if len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            # stack = stack[:-4]
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            cnt += 1
            
    return cnt
#     cnt = 0
#     while True:
#         if '1231' not in string:
#             break

#         string = string.replace('1231','',1)
#         cnt += 1
        
#     return cnt

    # li = []
    # cnt = 0
    # while True:
    #     try:
    #         li.append(ingredient.pop(0))
    #         if li[::-1][:4] == [1,3,2,1]:
    #             li = li[::-1][4:][::-1]
    #             cnt += 1
    #     except:
    #         return cnt
    cnt = 0
    string = string.replace('13','')
    while True:
        num = string.find('1231')
        if num == -1:
            return cnt
        else:
            string = string[:num]+string[num+4:]
            string = string.replace('13','')