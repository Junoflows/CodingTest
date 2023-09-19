def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start = [i,j]
                break
    
    for route in routes:
        if route[0] == 'E':
            for j in range(1,int(route[-1])+1):
                if start[1]+j == len(park[i]):
                    break
                if park[start[0]][start[1]+j] == 'X':
                        break
                if j == int(route[-1]):
                    start[1] = start[1] + j

        elif route[0] == 'W':
            for j in range(1,int(route[-1])+1):
                if start[1]-j == -1:
                    break
                if park[start[0]][start[1]-j] == 'X':
                        break
                if j == int(route[-1]):
                    start[1] = start[1] - j

        elif route[0] == 'N':
            for j in range(1,int(route[-1])+1):
                if start[0]-j == -1:
                    break
                if park[start[0]-j][start[1]] == 'X':
                        break
                if j == int(route[-1]):
                    start[0] = start[0] - j

        else:
            for j in range(1,int(route[-1])+1):
                if start[0]+j == len(park):
                    break
                if park[start[0]+j][start[1]] == 'X':
                        break
                if j == int(route[-1]):
                    start[0] = start[0] + j
                
    return start
    