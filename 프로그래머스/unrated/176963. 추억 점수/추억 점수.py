def solution(name, yearning, photo):
    results = []
    scores = {person:int(score) for person, score in zip(name, yearning)}
    for i in range(len(photo)):
        result = 0
        for j in photo[i]:
            if j in name:
                result += scores[j]
            elif j not in name:
                continue
        results.append(result)
        
    return results
    
