def solution(babbling):
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace('aya', '1')
        babbling[i] = babbling[i].replace('ye', '2')
        babbling[i] = babbling[i].replace('woo', '3')
        babbling[i] = babbling[i].replace('ma', '4')
        
    cnt = 0
    for x in babbling:
        for i in range(len(x)):
            if x[i] not in ['1','2','3','4']:
                break
            
            if i < len(x)-1:
                if x[i] == x[i+1]:
                    break
            
            if i == len(x) - 1:
                cnt += 1
                
    return cnt