def solution(wallpaper):
    wallpaper = [x.replace('.','0') for x in wallpaper]
    wallpaper = [x.replace('#','1') for x in wallpaper]
    col_min = []
    col_max = []
    row = []
    for i in wallpaper:
        if '1' in i:
            col_min.append(i.index('1'))
            col_max.append(len(i) - i[::-1].index('1'))
        elif '1' not in i:
            col_min.append('A')
            col_max.append('A')
            continue

    for i in range(len(col_min)):
        if 'A' != col_min[i] and 'A' != col_max[i]:
            row.append(i)

    col_min = [x for x in col_min if x != 'A']
    col_max = [x for x in col_max if x != 'A']
    
    return [min(row), min(col_min), max(row)+1, max(col_max)]
        
        