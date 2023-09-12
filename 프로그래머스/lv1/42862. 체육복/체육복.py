def solution(n, lost, reserve):
    lost.sort()
    losts = lost.copy()
    reserves = reserve.copy()
    
    # 여벌 체육복이 있는데 도난 당했을 경우 lost 와 reserve 에서 제거
    # 원본에 영향 안주게 복사본 생성
    for x in lost:
        if x in reserve:
            losts.remove(x)
            reserves.remove(x)
        print(losts, reserves)
    
    cnt = 0
    for i in range(len(losts)):
        # i-1 일 때 reserves 에 있으면 제거하고 cnt ++    
        if losts[i]-1 in reserves:
            reserves.remove(losts[i]-1)
            cnt += 1
        # i+1 일 때 reserves 에 있으면 제거하고 cnt ++
        elif losts[i]+1 in reserves:
            reserves.remove(losts[i]+1)
            cnt += 1
    
    return n - len(losts) + cnt