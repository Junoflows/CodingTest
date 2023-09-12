def solution(arr1, arr2):
#     li2 = []
#     length = len(arr1)

#     for i in range(len(arr1)):
#         li = []
#         for j in range(len(arr1[i])):
#             li.append(arr1[i][j] + arr2[i][j])
        
#         li2.append(li)
    
#     return li2
    # zip 을 활용해서 풀기
    li = []
    for c,d in zip(arr1, arr2):
        li.append([c[x]+d[x] for x in range(len(c))])
    
    return li
    