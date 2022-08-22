def solution(n, arr1, arr2):
    answer=[format((i | j),'b').zfill(n) for i, j in zip(arr1,arr2)]
    for i in range(n):
        answer[i]=answer[i].replace('1','#')
        answer[i]=answer[i].replace('0',' ')
    return answer