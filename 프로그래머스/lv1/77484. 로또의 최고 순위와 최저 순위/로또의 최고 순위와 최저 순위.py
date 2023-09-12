def solution(lottos, win_nums):
    tmp = len([x for x in lottos if x in win_nums])
    cnt = lottos.count(0)
    cnt_li = [tmp+cnt, tmp]
    return [6 if x < 2 else 7-x for x in cnt_li]