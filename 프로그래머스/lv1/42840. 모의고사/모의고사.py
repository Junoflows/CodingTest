def solution(answers):
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    man1 = man1 * ((len(answers)-1) // len(man1) +1)
    man2 = man2 * ((len(answers)-1) // len(man2) +1)
    man3 = man3 * ((len(answers)-1) // len(man3) +1)
    cnt = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == man1[i]:
            cnt[0] += 1
        if answers[i] == man2[i]:
            cnt[1] += 1
        if answers[i] == man3[i]:
            cnt[2] += 1
            
    result = []
    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            result.append(i+1)
            
    return result
    
    
    # if cnt.count(max(cnt)) == 1:
    #     return [cnt.index(max(cnt))+1]
    # elif cnt.count(max(cnt)) == 2:
    #     li = [1,2,3]
    #     li.pop(cnt.index(min(cnt)))
    #     return li
    #     # return [1,2,3].pop(cnt.index(min(cnt)))
    # elif cnt.count(max(cnt)) == 3:
    #     return [1,2,3]
    