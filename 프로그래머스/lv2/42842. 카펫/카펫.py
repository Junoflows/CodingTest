def solution(brown, yellow):
    # yellow 홀수일 때
    # return [yellow+2, 3]
    
    li = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            li.append([i, yellow // i])
            print(li)
    
    li2 = [(x[0]+x[1])*2+4 for x in li]
    print(li2)
    print(li2.index(brown))
    
    return [li[li2.index(brown)][1]+2, li[li2.index(brown)][0]+2]