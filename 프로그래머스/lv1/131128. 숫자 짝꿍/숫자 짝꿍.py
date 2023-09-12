import collections
def solution(X, Y):
    li_x = list(X)
    li_y = list(Y)
    dict_x = collections.Counter(li_x)
    dict_y = collections.Counter(li_y)
    key_x = list(dict_x.keys())
    key_y = list(dict_y.keys())
    temp = []
    i = 0
    while i < len(key_x):
        if key_x[i] in key_y:
            tmp = key_x[i]
            if dict_x[tmp]>0 and dict_y[tmp]>0:
                dict_x[tmp] -= 1
                dict_y[tmp] -= 1
                temp.append(tmp)
            else:
                i += 1
                continue
        else:
            i += 1
    
    # for i in range(len(X)):
    #     tmp = li_x.pop()
    #     if tmp in li_y :
    #         li_y.remove(tmp)
    #         temp.append(tmp)
    
    temp.sort(reverse = True)
    if len(temp) == 0:
        return '-1'
    if temp.count('0') == len(temp):
        return '0'
    return (''.join(temp))