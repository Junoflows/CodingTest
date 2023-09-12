def solution(n, arr1, arr2):
    # 이진수로 바꾸는 함수 생성
    def bin(x):
        li = []
        while True:
            if x == 0: break
            else:
                li.append(x % 2)
                x = x // 2
        return li[::-1]
    
    # arr1 이진수로 바꾸기
    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])
        if len(arr1[i]) < len(arr1):
            tmp = [0 for x in range(len(arr1)-len(arr1[i]))]
            tmp.extend(arr1[i])
            arr1[i] = tmp

    # arr2 이진수로 바꾸기   
    for i in range(len(arr2)):
        arr2[i] = bin(arr2[i])
        if len(arr2[i]) < len(arr2):
            tmp = [0 for x in range(len(arr2)-len(arr2[i]))]
            tmp.extend(arr2[i])
            arr2[i] = tmp
    
    # arr1 의 길이의 n*n 배열을 만듦
    Map = [[0 for _ in range(len(arr1))] for _ in range(len(arr1))]
    
    # arr1, arr2 중 1이 있으면 #, 다 0 이면 ' ' 으로 바꿔줌
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i][j] == 1 or arr2[i][j] == 1:
                Map[i][j] = '#'
            else:
                Map[i][j] = ' '
    
    # Map 의 i번째 인덱스를 str로 변경
    return [''.join(Map[i]) for i in range(len(arr1))]