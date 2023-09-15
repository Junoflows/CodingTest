def solution(progresses, speeds):
    li = []
    # for _ in range(9):
    while progresses != []:
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                continue
            progresses[i] += speeds[i]

        cnt = 0
        while True:
            if len(progresses) != 0 and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                if cnt == 0:
                    break
                else:
                    li.append(cnt)
                    break
    
        print(progresses, speeds, li)
    
    return li