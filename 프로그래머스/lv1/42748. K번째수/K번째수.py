# def solution(array, commands):
#     answer = []
#     for command in commands:
#         li = array[command[0]-1:command[1]]
#         li.sort()
#         answer.append(li[command[2]-1])
    
#     return answer


def solution(array, commands):
    result = []
    for command in commands:
        li = sorted([array[i] for i in range(command[0]-1, command[1])])
        print(li)
        result.append(li[command[-1]-1])
        
    print(result)
    return result
        
        