# def solution(price, money, count):
#     # hap = sum([price*counts for counts in range(1, count+1)])
#     # return hap - money if hap > money else 0
    
#     # 등차수열의 합 이용
#     return max(0, price*count*(count+1)//2 - money)
def solution(price, money, count):
    hap = 0
    for i in range(1, count+1):
        hap += price*i
    
    return max(0, hap - money)