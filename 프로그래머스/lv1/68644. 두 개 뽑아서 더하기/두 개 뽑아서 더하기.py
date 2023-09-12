def solution(numbers):  
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            print(i,j)
            answer.append(numbers[i] + numbers[j])
    result = list(set(answer))
    result.sort()
    return result