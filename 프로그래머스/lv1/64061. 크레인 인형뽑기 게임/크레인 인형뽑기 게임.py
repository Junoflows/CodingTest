def solution(board, moves):
    basket = []
    cnt =  0
    for idx in moves:
        idx -= 1
        for i in range(len(board)):
            # i 번째 인덱스에서 처음 0이 아닌 거 
            # 결과에 추가하고 0을 만듦
            if board[i][idx] != 0:
                basket.append(board[i][idx])
                board[i][idx] = 0
                break
                
        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            cnt += 2
    
    return cnt
