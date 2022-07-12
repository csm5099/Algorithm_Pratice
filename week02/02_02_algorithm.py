def solution(a, b):
    answer = 0
    #calculate each values from a and b 
    for i,j in zip(a,b):
        answer+=i*j
    return answer