def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        for i in target:
            li = []
            for key in keymap:
                if i in key:
                    li.append(key.index(i)+1)
                elif i not in key:
                    continue

            if li == []:
                cnt = -1
                break
            else: cnt += min(li)

        answer.append(cnt)
        
    return answer