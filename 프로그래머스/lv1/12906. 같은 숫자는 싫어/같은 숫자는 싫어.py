def solution(arr):

    answer = [arr[x] for x in range(1, len(arr)) if arr[x] != arr[x-1]]

    if answer == [] or answer[0] != arr[0]:
        return [arr[0]] + answer
    return answer