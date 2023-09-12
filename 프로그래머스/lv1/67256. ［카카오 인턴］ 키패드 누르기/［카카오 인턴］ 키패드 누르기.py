def solution(numbers, hand):
    answer = ''
    number = [[x+y for x in range(1,4)] for y in range(0,9,3)] + [['*', 0, '#']]
    left = [3,0]
    right = [3,2]
    for i in range(len(numbers)):
        col, row = (numbers[i] - 1) // 3, (numbers[i] - 1) % 3
        if numbers[i] in [1,4,7]:
            left[0], left[1] = col, row
            answer += 'L'
        elif numbers[i] in [3,6,9]:
            right[0], right[1] = col, row
            answer += 'R'
        elif numbers[i] in [2,5,8]:
            if abs(left[0] - col) + abs(left[1] - row) > abs(right[0] - col) + abs(right[1] - row):
                right[0], right[1] = col, row
                answer += 'R'

            elif abs(left[0] - col) + abs(left[1] - row) < abs(right[0] - col) + abs(right[1] - row):
                left[0], left[1] = col, row
                answer += 'L'
            elif abs(left[0] - col) + abs(left[1] - row) == abs(right[0] - col) + abs(right[1] - row):
                if hand == 'left' : 
                    left[0], left[1] = col, row
                    answer += 'L'

                elif hand == 'right': 
                    right[0], right[1] = col, row
                    answer += 'R'

        elif numbers[i] == 0:
            if abs(left[0] - 3) + abs(left[1] - 1) > abs(right[0] - 3) + abs(right[1] - 1):
                right = [3,1]
                answer += 'R'
            elif abs(left[0] - 3) + abs(left[1] - 1) < abs(right[0] - 3) + abs(right[1] - 1):
                left = [3,1]
                answer += 'L'
            elif abs(left[0] - 3) + abs(left[1] - 1) == abs(right[0] - 3) + abs(right[1] - 1):
                if hand == 'left': 
                    left = [3,1]
                    answer += 'L'
                elif hand == 'right': 
                    right = [3,1]
                    answer += 'R'
            
    return answer