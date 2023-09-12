def solution(dartResult):
    scores = []
    dartli = []
    for i in dartResult:
        if len(dartli) >= 1:
            if i == '0' and dartli[-1] == '1':
                dartli[-1] = '10'
                continue 
        dartli.append(i)
        
    while dartli != []:
        
        score = int(dartli[0])
        dartli.pop(0)
        
        if dartli[0] == 'S': score = score ** 1
        elif dartli[0] == 'D': score = score ** 2
        elif dartli[0] == 'T': score = score ** 3
            
        dartli.pop(0)
        
        if dartli == []:
            scores.append(score)
            break

        if dartli[0] == '*':
            score *= 2
            scores.append(score)
            if len(scores) > 1:
                scores[-2] *= 2
            dartli.pop(0)
            
        elif dartli[0] == '#':
            score *= -1
            scores.append(score)
            dartli.pop(0)
            
        else :
            scores.append(score)
            continue

    return sum(scores)