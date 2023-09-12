def solution(array, commands):
    answer = []
    for command in commands:
        li = array[command[0]-1:command[1]]
        li.sort()
        answer.append(li[command[2]-1])
    
    return answer