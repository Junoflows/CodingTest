def solution(players, callings):
    rank = {player:int(idx) for idx, player in enumerate(players)}
    
    for x in callings:      
        idx = rank[x]
        rank[players[idx]] -= 1
        rank[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players

