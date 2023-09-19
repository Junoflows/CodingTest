def solution(n, k):
    # 총 n!의 경우의 수를 갖고있음
    # 맨 앞의 수가 정해지면 (n - 1)! 의 경우의 수를 가짐
    # k에서 (n - 1)!을 나눴을 때의 몫이 첫번째 오는 자리
    # k에서 (n - 1)!을 나눴을 때의 나머지가 다시 k로 오는 자리
    result = []
    li = [i for i in range(1, n + 1)]
    while(n != 0):
        mul = 1
        for i in range(1,n):
            mul *= i

        idx = k // mul
        k = k % mul
        if k == 0:
            result.append(li.pop(idx - 1))
        else:
            result.append(li.pop(idx))
        n -= 1
    return result